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
folder = Path("/home/checa/FotosUniversidad/algoritmica")
images = sorted(list(folder.glob("*.HEIC")), key=natural_sort_key)

print(f"Cargando {len(images)} imágenes de Algorítmica...")
contents = [
    """Eres un profesor experto de la asignatura Algorítmica (UGR).
Te paso una colección de 12 fotografías de folios de un alumno.
Tu tarea es analizar y clasificar cada una:
1. Identificar si hay enunciados de exámenes oficiales (parciales, convocatorias).
2. Agrupar los folios de apuntes en BLOQUES TEMÁTICOS coherentes de la asignatura (ej: "Eficiencia y Ecuaciones de Recurrencia", "Divide y Vencerás", "Algoritmos Voraces (Greedy)", "Programación Dinámica", "Backtracking / Ramificación y Poda", etc.).
3. Para cada folio individual, indicar su contenido específico y si continúa de la página anterior.

Responde con un JSON estructurado:
{
  "examenes": [
    {
      "archivo": "IMG_XXXX.HEIC",
      "titulo": "...",
      "descripcion": "..."
    }
  ],
  "bloques_apuntes": [
    {
      "nombre_bloque": "Bloque X: ...",
      "descripcion": "...",
      "archivos": ["IMG_XXXX.HEIC", "IMG_YYYY.HEIC"]
    }
  ],
  "detalle_por_archivo": [
    {
      "archivo": "IMG_XXXX.HEIC",
      "tipo": "EXAMEN" o "APUNTES" o "EJERCICIOS",
      "tema": "...",
      "resumen_contenido": "..."
    }
  ]
}
"""
]

for idx, img_path in enumerate(images, 1):
    print(f"  Preparando [{idx:02d}/{len(images)}] {img_path.name}")
    img = Image.open(img_path).convert("RGB")
    img.thumbnail((1800, 1800))
    contents.append(f"FOTO {idx}: {img_path.name}")
    contents.append(img)

print("\nConsultando a Gemini para clasificación de Algorítmica...")
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=contents,
    config=types.GenerateContentConfig(
        temperature=0.1,
        response_mime_type="application/json"
    )
)

out_file = Path("/home/checa/Projects/javiercheca10.github.io/tools/digitalizar/clasificacion_algoritmica.json")
with open(out_file, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"\n✅ Clasificación completada y guardada en {out_file}")
