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

FOTOS_DIR = Path("/home/checa/FotosUniversidad/PDOO")
PUBLIC_PDOO = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/PDOO")

PROMPT_TRANSCRIBIR = """
Eres un profesor universitario de Programación y Diseño Orientado a Objetos (PDOO) y de Ingeniería del Software en la ETSIIT (Universidad de Granada).

Estás transcribiendo un bloque de apuntes manuscritos técnicos de la asignatura 'Programación y Diseño Orientado a Objetos' (PDOO): '{titulo_bloque}'.

DIRECTRICES EDITORIALES:
1. Formato de Salida: Markdown impecable con soporte para diagramas de clases (Mermaid o diagramas de cajas ASCII), tablas y ejemplos de código en Java y Ruby.
2. REGLA ESTRICTA DE LIMPIEZA:
   - NUNCA incluyas frases como "Escaneado con CamScanner", "CamScanner" o marcas de agua procedentes de digitalización física. Elimínalas por completo.
3. Si el documento incluye preguntas de Verdadero/Falso (cuestionario de examen/teoría), formátalas con claridad indicando la pregunta, la respuesta correcta explicada (V o F) y la justificación técnica detallada basada en el modelo de objetos de Java y Ruby.
4. Si hay jerarquías de clases o taxonomías (Clase Abstracta, Concreta, Hoja, No Hoja), incluye un bloque Mermaid `classDiagram` o diagrama claro además de las definiciones rigurosas.
5. Mantén un tono técnico y formal en español.

Estructura tu respuesta empezando directamente con el título de nivel 1:
# {titulo_bloque}
"""

def transcribir_bloque(subpath_destino, titulo_bloque, lista_archivos):
    out_file = PUBLIC_PDOO / subpath_destino
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
    # 1. Cuestionario de Teoría PDOO (IMG_1078, IMG_1079)
    transcribir_bloque(
        "cuestionario_teoria_pdoo.md",
        "Cuestionario de Teoría y Conceptos Fundamentales de PDOO",
        ["IMG_1078.HEIC", "IMG_1079.HEIC"]
    )
    time.sleep(2)

    # 2. Resumen de Conceptos Clave (IMG_1080)
    transcribir_bloque(
        "resumen_conceptos_clave.md",
        "Resumen Técnico: Atributos, Encapsulamiento y Constructores (Java vs Ruby)",
        ["IMG_1080.HEIC"]
    )
    time.sleep(2)

    # 3. Jerarquía y Taxonomía de Clases en Java (IMG_1081)
    transcribir_bloque(
        "jerarquia_clases_java_uml.md",
        "Jerarquía y Taxonomía de Clases en Java (UML)",
        ["IMG_1081.HEIC"]
    )

    print("\n🎉 ¡Todos los documentos de PDOO han sido transcritos con éxito!")

if __name__ == "__main__":
    main()
