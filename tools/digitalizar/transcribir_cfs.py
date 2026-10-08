import os
import json
import io
import time
from pathlib import Path
from PIL import Image
import pillow_heif
from google import genai
from google.genai import types
from dotenv import load_dotenv

pillow_heif.register_heif_opener()
load_dotenv("/home/checa/Projects/javiercheca10.github.io/.env")

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY no encontrada")

client = genai.Client(api_key=API_KEY)

FOTOS_DIR = Path("/home/checa/FotosUniversidad/Contabilidad financiera y de sociedades")
PUBLIC_CFS = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/CFS")

PROMPT_TRANSCRIBIR = """
Eres un catedrático universitario de Contabilidad Financiera y Contabilidad de Sociedades en la Facultad de Economía y Empresa (Universitat de València / UGR).

Estás transcribiendo un bloque de apuntes manuscritos técnicos de la asignatura: '{titulo_bloque}'.

DIRECTRICES EDITORIALES:
1. Formato de Salida: Markdown impecable con tablas de asientos contables del Plan General de Contabilidad (PGC), cuentas oficiales numeradas (ej. (190), (194), (100), (110), (103), (558), (572), (113), (6301)), Debe y Haber, y cálculos aritméticos de emisión y primas.
2. REGLA ESTRICTA DE LIMPIEZA:
   - NUNCA incluyas frases como "Escaneado con CamScanner", "CamScanner" o marcas de agua procedentes de digitalización física en el texto final. Elimínalas por completo.
3. Formato de Asientos Contables:
   - Presenta cada asiento contable en tablas Markdown limpias o bloques estructurados con las columnas:
     `Debe | Cuentas y Concepto | Haber`
   - Justifica claramente los importes calculados (Valor nominal $V_n$, Porcentaje de emisión, Prima de emisión, Desembolso mínimo legal del 25% o 30%, e impuestos diferidos de gastos de constitución imputados a reservas con efecto impositivo).
4. Redacción Técnica:
   - Mantén un tono académico riguroso, formal y preciso en español conforme a la Ley de Sociedades de Capital (LSC) y el PGC.

Estructura tu respuesta empezando directamente con el título de nivel 1:
# {titulo_bloque}
"""

def transcribir_bloque(subpath_destino, titulo_bloque, lista_archivos):
    out_file = PUBLIC_CFS / subpath_destino
    if out_file.exists() and out_file.stat().st_size > 500:
        print(f"\n--- {subpath_destino} ya existe ({out_file.stat().st_size} bytes). Saltando... ---")
        return

    print(f"\n--- Transcribiendo {subpath_destino}: {titulo_bloque} ({len(lista_archivos)} páginas) ---")
    
    parts = []
    for f_name in lista_archivos:
        img_path = FOTOS_DIR / f_name
        print(f"  Abriendo {f_name}...")
        img = Image.open(img_path)
        img = img.convert("RGB")
        max_size = 2000
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=88)
        jpeg_bytes = buf.getvalue()
        
        parts.append(f"--- PÁGINA: {f_name} ---")
        parts.append(types.Part.from_bytes(data=jpeg_bytes, mime_type="image/jpeg"))

    prompt = PROMPT_TRANSCRIBIR.format(titulo_bloque=titulo_bloque)
    parts.append(prompt)

    models_to_try = [
        "gemini-3.5-flash-lite",
        "gemini-3.1-flash-lite",
        "gemini-3-flash-preview",
        "gemini-3.6-flash"
    ]
    
    res = None
    for attempt in range(4):
        for model_name in models_to_try:
            try:
                print(f"  Intento {attempt+1} generando con {model_name}...")
                res = client.models.generate_content(
                    model=model_name,
                    contents=parts,
                )
                if res.text:
                    print(f"  ✅ Recibida respuesta de {model_name}")
                    break
            except Exception as e:
                print(f"    Fallo con {model_name}: {str(e)[:120]}")
                time.sleep(3)
        if res and res.text:
            break
        print("  Esperando 5s antes de reintentar...")
        time.sleep(5)

    if not res or not res.text:
        raise RuntimeError(f"No se pudo transcribir {subpath_destino}")

    texto_limpio = res.text
    for linea in ["Escaneado con CamScanner", "Escaneado con Camscanner", "CamScanner", "Scanned with CamScanner"]:
        texto_limpio = texto_limpio.replace(linea, "")

    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(texto_limpio, encoding="utf-8")
    print(f"  ✅ Guardado en {out_file} ({len(texto_limpio)} caracteres)")

def main():
    # 1. Teoría: Constitución de Sociedades y Formas Jurídicas (IMG_1119 a 1121)
    transcribir_bloque(
        "tema1_constitucion_sociedades_teoria.md",
        "Tema 1: Constitución de Sociedades - Formas Jurídicas, Fases y Asientos Tipo",
        ["IMG_1119.HEIC", "IMG_1120.HEIC", "IMG_1121.HEIC"]
    )
    time.sleep(2)

    # 2. Ejercicios Resueltos de Constitución: Supuestos 1, 2, 3 y 8 (IMG_1122 a 1128)
    transcribir_bloque(
        "tema1_ejercicios_constitucion_resueltos.md",
        "Supuestos Prácticos Resueltos de Constitución (Ejercicios 1, 2, 3 y 8 PGC)",
        ["IMG_1122.HEIC", "IMG_1123.HEIC", "IMG_1124.HEIC", "IMG_1125.HEIC", "IMG_1126.HEIC", "IMG_1127.HEIC", "IMG_1128.HEIC"]
    )

    print("\n🎉 ¡Todos los documentos de Contabilidad Financiera y de Sociedades han sido transcritos con éxito!")

if __name__ == "__main__":
    main()
