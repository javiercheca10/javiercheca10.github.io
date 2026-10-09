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

FOTOS_DIR = Path("/home/checa/FotosUniversidad/Gestion Fiscal de la Empresa")
PUBLIC_GFE = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/GFE")

PROMPT_TRANSCRIBIR = """
Eres un catedrático universitario de Gestión Fiscal de la Empresa y Derecho Financiero y Tributario en la Facultad de Economía y Empresa (Universitat de València / UGR).

Estás transcribiendo y formalizando un bloque de apuntes y ejercicios manuscritos técnicos de la asignatura: '{titulo_bloque}'.

DIRECTRICES EDITORIALES Y DE CALIDAD:
1. Formato de Salida: Markdown estructurado e impecable con rigor académico superior.
   - Utiliza títulos de sección `#`, `##`, `###`.
   - Incluye tablas resumen donde corresponda.
   - En fórmulas matemáticas y fiscales, utiliza notación KaTeX estándar ($...$ para inline y $$...$$ para bloques).
2. REGLA ESTRICTA DE LIMPIEZA:
   - NUNCA incluyas frases como "Escaneado con CamScanner", "CamScanner", "Scanned with CamScanner" o referencias a digitalización física.
3. Para Liquidaciones Fiscales y Asientos Contables:
   - Presenta las liquidaciones del Impuesto sobre Sociedades (IS) en tablas estructuradas con columnas claras:
     `Concepto / Ajuste | Justificación Legal (LIS) | Signo (+ / -) | Importe (€)`
   - Desglosa con claridad: Resultado Contable, Ajustes Extracontables (permanentes y temporarios), Base Imponible, Tipo impositivo, Cuota Íntegra, Deducciones (doble imposición, I+D/IT), Bonificaciones, Cuota Líquida, Retenciones y Pagos a Cuenta, Cuota Diferencial.
   - Presenta los asientos contables en tablas:
     `Debe (€) | Cuentas PGC y Concepto | Haber (€)`
     con sus códigos oficiales del PGC: (6300), (6301), (4740), (479), (473), (4752), (4709).
4. Rigor Normativo:
   - Fundamenta en la Ley General Tributaria (Ley 58/2003 LGT), la Ley del Impuesto sobre Sociedades (Ley 27/2014 LIS), la Ley del IVA (Ley 37/1992) y la LIRPF según proceda.
   - Cita límites fiscales reales (amortización acelerada en ERD multiplicador x2, límite del 1% del INCN para gastos de atenciones a clientes, deterioro de créditos, etc.).

Estructura tu respuesta empezando directamente con el título de nivel 1:
# {titulo_bloque}
"""

def transcribir_bloque(subpath_destino, titulo_bloque, lista_archivos):
    out_file = PUBLIC_GFE / subpath_destino
    if out_file.exists() and out_file.stat().st_size > 800:
        print(f"\n--- {subpath_destino} ya existe ({out_file.stat().st_size} bytes). Saltando... ---")
        return

    print(f"\n--- Transcribiendo {subpath_destino}: {titulo_bloque} ({len(lista_archivos)} páginas) ---")
    
    parts = []
    for f_name in lista_archivos:
        img_path = FOTOS_DIR / f_name
        print(f"  Abriendo {f_name}...")
        img = Image.open(img_path).convert("RGB")
        max_size = 1800
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=85)
        jpeg_bytes = buf.getvalue()
        
        parts.append(f"--- LÁMINA / HOJA: {f_name} ---")
        parts.append(types.Part.from_bytes(data=jpeg_bytes, mime_type="image/jpeg"))

    prompt = PROMPT_TRANSCRIBIR.format(titulo_bloque=titulo_bloque)
    parts.append(prompt)

    models_to_try = [
        "gemini-3.5-flash",
        "gemini-3.7-flash",
        "gemini-3.8-flash",
        "gemini-3.1-flash-lite"
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
    # 1. Tema 1: Sistema Tributario Español y Elementos Cuantitativos del Tributo (IMG_1129, IMG_1130)
    transcribir_bloque(
        "tema1_sistema_tributario_elementos.md",
        "Tema 1: El Sistema Tributario Español, Principios Constitucionales y Cuantificación de la Obligación Tributaria",
        ["IMG_1129.HEIC", "IMG_1130.HEIC"]
    )
    time.sleep(3)

    # 2. Impuesto sobre Sociedades: Marco Teórico, Amortizaciones y Ajustes (IMG_1131 a IMG_1138)
    transcribir_bloque(
        "tema2_impuesto_sociedades_teoria_liquidacion.md",
        "Impuesto sobre Sociedades (IS): Régimen Legal, Amortizaciones Deducibles, Ajustes Extracontables y Liquidación",
        [f"IMG_{i}.HEIC" for i in range(1131, 1139)]
    )
    time.sleep(3)

    # 3. Casos Prácticos de Examen: Liquidación Modelos A y B (IMG_1139 a IMG_1142)
    transcribir_bloque(
        "tema2_casos_practicos_examen_octubre2023.md",
        "Casos Prácticos de Examen Parcial: Liquidación del IS (Modelos A Gran Empresa y Modelo B ERD) con Registro Contable",
        [f"IMG_{i}.HEIC" for i in range(1139, 1143)]
    )

    print("\n🎉 ¡Todos los documentos de Gestión Fiscal de la Empresa han sido transcritos con éxito!")

if __name__ == "__main__":
    main()
