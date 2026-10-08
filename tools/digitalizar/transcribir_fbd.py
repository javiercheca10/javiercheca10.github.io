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

FOTOS_DIR = Path("/home/checa/FotosUniversidad/FBD")
PUBLIC_FBD = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/FBD")

PROMPT_TRANSCRIBIR = """
Eres un profesor catedrático universitario de la asignatura 'Fundamentos de Bases de Datos' (FBD) en la ETSIIT de la Universidad de Granada (UGR).

Estás transcribiendo un bloque de apuntes manuscritos técnicos de la asignatura: '{titulo_bloque}'.

DIRECTRICES EDITORIALES Y DE CALIDAD:
1. Formato de Salida: Markdown técnico impecable con soporte completo para código SQL (```sql), operadores de Álgebra Relacional en KaTeX ($\\sigma, \\pi, \\rho, \\times, \\cup, \\cap, -, \\bowtie, \\div, \\gamma$) y tablas.
2. REGLA ESTRICTA DE LIMPIEZA:
   - NUNCA incluyas frases como "Escaneado con CamScanner", "CamScanner" o marcas de agua procedentes de digitalización física en el texto final. Elimínalas por completo.
3. Formulario y Resumen al final:
   - Si este bloque contiene hojas de formulario / chuletario de sintaxis o resumen al final, crea una sección final claramente delimitada con:
     `## 📌 Formulario & Chuletario de Resumen`
     con tablas de sintaxis, reglas mnemotécnicas y fórmulas rápidas de consulta.
4. Código SQL y Álgebra Relacional:
   - Formatea el código SQL de manera profesional con indentación limpia.
   - Emplea notación formal rigurosa para las operaciones relacionales (selección $\\sigma_{{cond}}(R)$, proyección $\\pi_{{attr}}(R)$, reunión natural $R \\bowtie S$, etc.).
5. Redacción Técnica:
   - Mantén un tono académico riguroso, formal y preciso en español.

Estructura tu respuesta empezando directamente con el título de nivel 1:
# {titulo_bloque}
"""

def transcribir_bloque(subpath_destino, titulo_bloque, lista_archivos):
    out_file = PUBLIC_FBD / subpath_destino
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
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite",
        "gemini-3.1-flash-lite",
        "gemini-3-flash-preview"
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
    # 1. Tema 1: Introducción a las Bases de Datos y SGBD (IMG_1086 a 1090 + Resumen IMG_1108 a 1110)
    transcribir_bloque(
        "tema1_introduccion_sgbd.md",
        "Tema 1: Introducción a las Bases de Datos y SGBD (con Formulario/Resumen)",
        ["IMG_1086.HEIC", "IMG_1087.HEIC", "IMG_1088.HEIC", "IMG_1089.HEIC", "IMG_1090.HEIC", "IMG_1108.HEIC", "IMG_1109.HEIC", "IMG_1110.HEIC"]
    )
    time.sleep(2)

    # 2. Tema 2: Arquitectura de 3 Niveles ANSI/SPARC y Lenguajes (IMG_1091 + Resumen IMG_1111 a 1114)
    transcribir_bloque(
        "tema2_arquitectura_sgbd.md",
        "Tema 2: Arquitectura de un SGBD (ANSI/SPARC, Lenguajes y Formulario/Resumen)",
        ["IMG_1091.HEIC", "IMG_1111.HEIC", "IMG_1112.HEIC", "IMG_1113.HEIC", "IMG_1114.HEIC"]
    )
    time.sleep(2)

    # 3. Tema 3: Formulario Maestro de SQL (DDL, DML, Consultas y Modificación) (IMG_1092 a 1096)
    transcribir_bloque(
        "tema3_formulario_sql.md",
        "SQL Completo: Formulario y Sintaxis de Creación, Consultas y Modificación",
        ["IMG_1092.HEIC", "IMG_1093.HEIC", "IMG_1094.HEIC", "IMG_1095.HEIC", "IMG_1096.HEIC"]
    )
    time.sleep(2)

    # 4. Tema 4: Nivel Interno, Almacenamiento, Índices B+ y Hashing (IMG_1097 a 1107)
    transcribir_bloque(
        "tema4_nivel_interno_almacenamiento.md",
        "Tema 4: Nivel Interno, Almacenamiento Físico, Índices (Árboles B+) y Hashing",
        ["IMG_1097.HEIC", "IMG_1098.HEIC", "IMG_1099.HEIC", "IMG_1100.HEIC", "IMG_1101.HEIC", "IMG_1102.HEIC", "IMG_1103.HEIC", "IMG_1104.HEIC", "IMG_1105.HEIC", "IMG_1106.HEIC", "IMG_1107.HEIC"]
    )
    time.sleep(2)

    # 5. Tema 5: Formulario y Chuletario de Álgebra Relacional (IMG_1115 a 1117)
    transcribir_bloque(
        "tema5_algebra_relacional.md",
        "Álgebra Relacional: Formulario Maestro de Operaciones y Restricciones",
        ["IMG_1115.HEIC", "IMG_1116.HEIC", "IMG_1117.HEIC"]
    )

    print("\n🎉 ¡Todos los bloques temáticos de FBD han sido transcritos con éxito!")

if __name__ == "__main__":
    main()
