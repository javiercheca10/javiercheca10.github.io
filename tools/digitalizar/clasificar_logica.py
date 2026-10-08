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

FOTOS_DIR = Path("/home/checa/FotosUniversidad/logica")
files = sorted([f for f in os.listdir(FOTOS_DIR) if f.upper().endswith(".HEIC")])

print(f"Detectadas {len(files)} fotos en {FOTOS_DIR}:")
print(files)

# Vamos a enviar las fotos a Gemini indicando las reglas precisas del usuario:
# Reglas de agrupación:
# 1. "formulario, tema 1 y examen NO tienen clip"
# 2. "ejercicios de examen: clip ARRIBA A LA DERECHA"
# 3. "tema 2: clip ARRIBA A LA IZQUIERDA"
# 4. "tema 3: clip ABAJO A LA IZQUIERDA"
#
# Para los que NO tienen clip:
# - Formulario (resumen sintáctico / semántico, tablas de verdad, reglas de deducción natural / resolución)
# - Tema 1 (Lógica Proposicional o introducción formal)
# - Examen oficial (enunciado de examen con puntuaciones, preguntas numeradas o convocatoria)

PROMPT_CLASIFICACION = """
Actúa como un profesor universitario y clasificador experto de documentos académicos de la asignatura 'Lógica y Métodos Discretos' (ETSIIT UGR).

El alumno ha organizado sus folios manuscritos de la siguiente manera usando la POSICIÓN DEL CLIP (o la ausencia de él) y el contenido:
1. 'SIN CLIP':
   - 'Formulario': Hojas resumen de sintaxis, semántica, equivalencias notables, reglas de deducción natural o cálculo de resolución.
   - 'Tema 1': Apuntes de teoría del Tema 1 (Lógica de Proposiciones / cálculo proposicional).
   - 'Examen': Enunciado formal de examen con ejercicios oficiales, puntuaciones por pregunta o fecha/convocatoria.
2. 'CLIP ARRIBA A LA DERECHA':
   - 'Ejercicios de Examen': Colección de problemas y ejercicios resueltos de examen.
3. 'CLIP ARRIBA A LA IZQUIERDA':
   - 'Tema 2': Apuntes de teoría del Tema 2 (Lógica de Primer Orden / Predicados, formalización, semántica de primer orden, etc.).
4. 'CLIP ABAJO A LA IZQUIERDA':
   - 'Tema 3': Apuntes de teoría del Tema 3 (Métodos de Demostración, Deducción Natural, Resolución, etc.).

Observa cada imagen detalladamente:
- Inspecciona si tiene clip metálico y en qué esquina está (arriba-dcha, arriba-izq, abajo-izq, o si no hay clip).
- Lee los encabezados, títulos, temas y fórmulas del folio.
- Determina el orden de lectura correcto de las páginas dentro de cada grupo para que la transcripción sea fluida y secuencial.

Devuelve EXCLUSIVAMENTE un objeto JSON válido con la siguiente estructura:
{
  "grupos": [
    {
      "id": "formulario",
      "nombre": "Formulario y Resumen de Reglas",
      "posicion_clip": "SIN CLIP",
      "archivos": ["IMG_xxxx.HEIC"],
      "descripcion": "..."
    },
    {
      "id": "tema-1",
      "nombre": "Tema 1: Lógica Proposicional",
      "posicion_clip": "SIN CLIP",
      "archivos": ["IMG_xxxx.HEIC", "..."],
      "descripcion": "..."
    },
    {
      "id": "tema-2",
      "nombre": "Tema 2: Lógica de Primer Orden",
      "posicion_clip": "CLIP ARRIBA A LA IZQUIERDA",
      "archivos": ["IMG_xxxx.HEIC", "..."],
      "descripcion": "..."
    },
    {
      "id": "tema-3",
      "nombre": "Tema 3: Métodos de Demostración y Resolución",
      "posicion_clip": "CLIP ABAJO A LA IZQUIERDA",
      "archivos": ["IMG_xxxx.HEIC", "..."],
      "descripcion": "..."
    },
    {
      "id": "ejercicios-examen",
      "nombre": "Ejercicios Resueltos de Examen",
      "posicion_clip": "CLIP ARRIBA A LA DERECHA",
      "archivos": ["IMG_xxxx.HEIC", "..."],
      "descripcion": "..."
    },
    {
      "id": "examen",
      "nombre": "Examen Oficial",
      "posicion_clip": "SIN CLIP",
      "archivos": ["IMG_xxxx.HEIC"],
      "descripcion": "..."
    }
  ],
  "detalle_por_archivo": [
    {
      "archivo": "IMG_xxxx.HEIC",
      "clip_detectado": "ninguno / arriba-derecha / arriba-izquierda / abajo-izquierda",
      "clasificacion": "formulario / tema-1 / tema-2 / tema-3 / ejercicios-examen / examen",
      "titulo_pagina": "...",
      "resumen": "..."
    }
  ]
}
"""

def main():
    parts = []
    print("\nProcesando y optimizando imágenes para clasificación...")
    for f_name in files:
        p = FOTOS_DIR / f_name
        img = Image.open(p)
        img = img.convert("RGB")
        max_size = 1400
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=82)
        jpeg_bytes = buf.getvalue()
        
        parts.append(f"ARCHIVO: {f_name}")
        parts.append(types.Part.from_bytes(data=jpeg_bytes, mime_type="image/jpeg"))

    parts.append(PROMPT_CLASIFICACION)

    models_to_try = [
        "gemini-3.5-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash-lite",
        "gemini-flash-latest",
        "gemini-3.8-flash",
        "gemini-2.5-pro",
        "gemini-2.5-flash"
    ]
    res = None
    for attempt in range(3):
        for model_name in models_to_try:
            try:
                print(f"Intento {attempt+1} - Consultando clasificación con {model_name}...")
                res = client.models.generate_content(
                    model=model_name,
                    contents=parts,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json"
                    )
                )
                if res.text:
                    print(f"✅ Respuesta recibida con éxito de {model_name}")
                    break
            except Exception as e:
                print(f"Error con {model_name}: {e}")
                time.sleep(2)
        if res and res.text:
            break
        print("Esperando 6 segundos antes de reintentar...")
        time.sleep(6)

    if not res or not res.text:
        raise RuntimeError("No se obtuvo respuesta de Gemini")

    out_json = Path("/home/checa/Projects/javiercheca10.github.io/tools/digitalizar/clasificacion_logica.json")
    with open(out_json, "w", encoding="utf-8") as f:
        f.write(res.text)

    print(f"\n✅ Clasificación guardada exitosamente en {out_json}")

if __name__ == "__main__":
    main()
