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
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv("/home/checa/Projects/javiercheca10.github.io/.env")
from google import genai
from google.genai import types
from PIL import Image
from pillow_heif import register_heif_opener
register_heif_opener()

client = genai.Client()
input_dir = Path("/home/checa/FotosUniversidad/Calculo")
output_dir = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/CAL")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "examenes").mkdir(parents=True, exist_ok=True)

PROMPT_EXAMEN = r"""Eres un profesor de la Universidad de Granada (UGR).
Transcribe este examen oficial de Cálculo a formato MARKDOWN con sintaxis estricta de LATEX ($...$ y $$...$$).
Estructura:
- Encabezado con Asignatura, Convocatoria y Fecha oficial visible.
- Enunciado de cada ejercicio / problema numerado con claridad.
- Si hay subapartados (a, b, c), sepáralos en listas.
- Puntuación de cada pregunta si aparece anotada.
Devuelve directamente el Markdown limpio sin rodeos.
"""

PROMPT_APUNTES = r"""Eres un profesor y transcriptor experto de la asignatura Cálculo (UGR).
Transcribe estos folios de apuntes manuscritos a un documento MARKDOWN estructurado con fórmulas matemáticas en LATEX ($...$ y $$...$$).
Reglas:
- Jerarquía de títulos (#, ##, ###).
- Teoremas, lemas y axiomas en bloques citados (> **Axioma**: ...).
- Demostraciones completas con todos sus pasos.
- Ejercicios resueltos y ejemplos destacados.
- Tablas si las hay formateadas en Markdown.
Devuelve directamente el Markdown limpio sin rodeos.
"""

tareas = [
    {
        "nombre": "Examen 1er Parcial 2023",
        "salida": output_dir / "examenes/examen_parcial_noviembre_2023.md",
        "archivos": ["IMG_0998.HEIC"],
        "prompt": PROMPT_EXAMEN
    },
    {
        "nombre": "Examen Convocatoria Ordinaria 2024",
        "salida": output_dir / "examenes/examen_ordinaria_enero_2024.md",
        "archivos": ["IMG_0999.HEIC"],
        "prompt": PROMPT_EXAMEN
    },
    {
        "nombre": "Bloque 1: Números Reales e Inducción",
        "salida": output_dir / "bloque1_reales_induccion.md",
        "archivos": [
            "IMG_0983.HEIC", "IMG_0984.HEIC", "IMG_0985.HEIC", "IMG_0986.HEIC",
            "IMG_0987.HEIC", "IMG_0988.HEIC", "IMG_0989.HEIC", "IMG_0990.HEIC", "IMG_0993.HEIC"
        ],
        "prompt": PROMPT_APUNTES
    },
    {
        "nombre": "Bloque 2: Sucesiones y Series Numéricas",
        "salida": output_dir / "bloque2_sucesiones_series.md",
        "archivos": [
            "IMG_0992.HEIC", "IMG_0994.HEIC", "IMG_0995.HEIC", "IMG_0996.HEIC", "IMG_0997.HEIC"
        ],
        "prompt": PROMPT_APUNTES
    },
    {
        "nombre": "Bloque 3: Límites y Polinomio de Taylor",
        "salida": output_dir / "bloque3_limites_taylor.md",
        "archivos": ["IMG_0991.HEIC"],
        "prompt": PROMPT_APUNTES
    }
]

models = ["gemini-3.5-flash", "gemini-flash-latest", "gemini-3.7-flash"]

for idx, t in enumerate(tareas, 1):
    print(f"\n==================================================")
    print(f"[{idx}/{len(tareas)}] Procesando: {t['nombre']}")
    print(f"Archivos ({len(t['archivos'])}): {', '.join(t['archivos'])}")
    
    contents = [t["prompt"]]
    for f_name in t["archivos"]:
        f_path = input_dir / f_name
        img = Image.open(f_path).convert("RGB")
        img.thumbnail((1800, 1800))
        contents.append(f"PÁGINA: {f_name}")
        contents.append(img)
    contents.append("Transcribe ahora el material anterior en orden siguiendo las instrucciones.")

    success = False
    for m in models:
        try:
            print(f"  Enviando a {m}...")
            res = client.models.generate_content(
                model=m,
                contents=contents,
                config=types.GenerateContentConfig(temperature=0.15)
            )
            with open(t["salida"], "w", encoding="utf-8") as f:
                f.write(res.text)
            print(f"  ✅ Guardado en: {t['salida']} ({len(res.text)} caracteres)")
            success = True
            break
        except Exception as e:
            print(f"  ⚠️ Error con {m}: {str(e)[:60]}. Probando siguiente...")
            time.sleep(2)

    if not success:
        print(f"  ❌ Fallaron todos los modelos para {t['nombre']}")

print("\n🎉 Todos los bloques y exámenes han sido procesados y organizados.")
