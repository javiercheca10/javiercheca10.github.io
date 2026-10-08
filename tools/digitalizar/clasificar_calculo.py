# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-genai",
#     "pillow",
#     "pillow-heif",
#     "python-dotenv",
# ]
# ///

import os
import json
import re
from pathlib import Path
from dotenv import load_dotenv

load_dotenv("/home/checa/Projects/javiercheca10.github.io/.env")
from google import genai
from google.genai import types
from PIL import Image
from pillow_heif import register_heif_opener
register_heif_opener()

def natural_sort_key(path: Path):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', path.name)]

client = genai.Client()
folder = Path("/home/checa/FotosUniversidad/Calculo")
images = sorted(list(folder.glob("*.HEIC")), key=natural_sort_key)

print(f"Cargando {len(images)} imágenes...")
contents = [
    """Eres un profesor y clasificador experto de la asignatura Cálculo (UGR).
Te paso una colección de 17 fotografías de folios de un alumno.
El alumno nos avisa: "tiene dos enunciados de exámenes y varios bloques de apuntes que no van continuados, es decir, no todos los apuntes son uno detrás de otro, hay que separarlos en varios bloques".

Tu tarea es:
1. Identificar con precisión cuáles son los 2 enunciados de exámenes (o parciales/finales).
2. Para el resto de folios, agruparlos en BLOQUES TEMÁTICOS coherentes de apuntes (por ejemplo: "Bloque 1: Números Reales y Axiomas", "Bloque 2: Series y Criterios", "Bloque 3: Integrales", etc.).
3. Para cada folio individual, indicar qué contiene, su título o tema, y a qué bloque pertenece.

Responde con un JSON estructurado con este formato:
{
  "examenes": [
    {
      "archivo": "IMG_XXXX.HEIC",
      "titulo": "Enunciado Examen ... (ej. Convocatoria Ordinaria / Parcial)",
      "descripcion": "..."
    }
  ],
  "bloques_apuntes": [
    {
      "nombre_bloque": "Bloque 1: ...",
      "descripcion": "...",
      "archivos": ["IMG_XXXX.HEIC", "IMG_YYYY.HEIC"]
    }
  ],
  "detalle_por_archivo": [
    {
      "archivo": "IMG_XXXX.HEIC",
      "tipo": "EXAMEN" o "APUNTES",
      "tema": "...",
      "resumen_contenido": "..."
    }
  ]
}
"""
]

for idx, img_path in enumerate(images, 1):
    print(f"  Preparando [{idx:02d}/17] {img_path.name}")
    img = Image.open(img_path).convert("RGB")
    # Redimensionar ligeramente si es muy grande para acelerar subida
    img.thumbnail((1800, 1800))
    contents.append(f"FOTO {idx}: {img_path.name}")
    contents.append(img)

print("\nConsultando a Gemini para clasificación global...")
response = None
models_to_try = ["gemini-flash-latest", "gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.5-flash"]

for m in models_to_try:
    try:
        print(f"Probando modelo: {m}...")
        response = client.models.generate_content(
            model=m,
            contents=contents,
            config=types.GenerateContentConfig(
                temperature=0.1,
                response_mime_type="application/json"
            )
        )
        print(f"✅ Respuesta recibida con éxito de {m}!")
        break
    except Exception as e:
        print(f"⚠️ {m} falló: {e}. Probando siguiente modelo...")

if not response:
    print("❌ No se pudo clasificar con ninguno de los modelos.")
    sys.exit(1)

out_file = Path("/home/checa/Projects/javiercheca10.github.io/tools/digitalizar/clasificacion_calculo.json")
with open(out_file, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"\n✅ Clasificación completada y guardada en {out_file}")
