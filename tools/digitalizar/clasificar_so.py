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

FOTOS_DIR = Path("/home/checa/FotosUniversidad/Sistemas operativos")
files = sorted([f for f in os.listdir(FOTOS_DIR) if f.upper().endswith(".HEIC")])

print(f"Detectadas {len(files)} fotos en {FOTOS_DIR}:")
print(files)

PROMPT_CLASIFICACION = """
Actúa como un profesor catedrático universitario de Sistemas Operativos en la ETSIIT de la Universidad de Granada (UGR).

Examina esta colección de 33 fotos manuscritas de apuntes y ejercicios de la asignatura 'Sistemas Operativos'.
Tu objetivo es organizar estas hojas en bloques temáticos coherentes, lógicos y naturales según su temario (procesos, hilos, planificación de CPU, sincronización/concurrencia, gestión de memoria/paginación, sistemas de archivos/E-S, llamadas al sistema POSIX como fork/wait/exec/pipe, etc.), así como identificar si alguna hoja corresponde a enunciados o exámenes.

REGLAS DE CLASIFICACIÓN:
1. Agrupa por afinidad temática y continuidad de apuntes (los folios que tratan el mismo tema deben estar juntos y en su orden natural de lectura).
2. Si hay ejercicios resueltos de exámenes o problemas típicos (ej. diagramas de Gantt de planificación, algoritmos de reemplazo de páginas FIFO/LRU/Óptimo, problemas de sincronización de semáforos, trazas de fork/pipe), agrúpalos como ejercicios prácticos o en su tema respectivo.
3. Ignora y descarta cualquier mención a "Escaneado con CamScanner", "CamScanner" o marcas de agua de digitalización.

Devuelve EXCLUSIVAMENTE un objeto JSON válido con la siguiente estructura:
{
  "bloques": [
    {
      "id": "identificador_bloque",
      "titulo": "Título formal del bloque temático",
      "tipo": "TEORÍA / EJERCICIOS / EXAMEN",
      "archivos": ["IMG_xxxx.HEIC", "..."],
      "descripcion": "Resumen conciso del contenido que cubre este bloque."
    }
  ],
  "detalle_por_archivo": [
    {
      "archivo": "IMG_xxxx.HEIC",
      "tema_identificado": "...",
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
        max_size = 1300
        if max(img.size) > max_size:
            ratio = max_size / max(img.size)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=80)
        jpeg_bytes = buf.getvalue()
        
        parts.append(f"ARCHIVO: {f_name}")
        parts.append(types.Part.from_bytes(data=jpeg_bytes, mime_type="image/jpeg"))

    parts.append(PROMPT_CLASIFICACION)

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
                print(f"Intento {attempt+1} - Consultando clasificación con {model_name}...")
                res = client.models.generate_content(
                    model=model_name,
                    contents=parts,
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json"
                    )
                )
                if res.text:
                    print(f"✅ Clasificación recibida de {model_name}")
                    break
            except Exception as e:
                print(f"Error con {model_name}: {str(e)[:120]}")
                time.sleep(2)
        if res and res.text:
            break
        print("Esperando 5s antes de reintentar...")
        time.sleep(5)

    if not res or not res.text:
        raise RuntimeError("No se obtuvo respuesta de Gemini para la clasificación de Sistemas Operativos")

    out_json = Path("/home/checa/Projects/javiercheca10.github.io/tools/digitalizar/clasificacion_so.json")
    with open(out_json, "w", encoding="utf-8") as f:
        f.write(res.text)

    print(f"\n✅ Clasificación de Sistemas Operativos guardada en {out_json}")

if __name__ == "__main__":
    main()
