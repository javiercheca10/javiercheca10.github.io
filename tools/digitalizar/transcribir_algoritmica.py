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

FOTOS_DIR = Path("/home/checa/FotosUniversidad/algoritmica")
PUBLIC_ALGO = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/ALGO")
PUBLIC_ALGO.mkdir(parents=True, exist_ok=True)

PROMPT_TRANSCRIBIR = """
Eres un profesor universitario experto en Algorítmica y Estructuras de Datos de la Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación (ETSIIT, UGR).

Estás transcribiendo un bloque de apuntes manuscritos de la asignatura 'Algorítmica'.
Se te proporciona una secuencia ordenada de páginas manuscritas que forman este bloque temático: '{titulo_bloque}'.

INSTRUCCIONES CLAVE DE FORMATO Y TRANSCRIPCIÓN:
1. Formato de Salida: Markdown impecable con soporte matemático LaTeX completo.
2. Fórmulas Matemáticas:
   - Fórmulas en línea: usa $...$ (ej: $T(n) = aT(n/b) + f(n)$, $O(n \\log n)$, $\\Theta(n^2)$).
   - Ecuaciones destacadas: usa $$...$$ con matrices, sistemas, recurrencias alineadas (`\\begin{{cases}} ... \\end{{cases}}`, `\\begin{{aligned}} ... \\end{{aligned}}`).
3. Algoritmos y Pseudocódigo / Código C++:
   - Si en los apuntes hay algoritmos, pseudocódigo o trazas de ejecución (Kruskal, Prim, Dijkstra, Algoritmo Húngaro, Cambio de moneda, Mochila, etc.), formatéalos limpiamente en bloques ```cpp o ```text.
4. Diagramas y Grafos:
   - Si hay grafos, árboles de recursión, matrices de costes o trazas de tablas (como la matriz del Algoritmo Húngaro o la tabla de Programación Dinámica), represéntalos usando tablas Markdown claras o diagramas ASCII/Mermaid.
5. Fidelidad y Claridad:
   - Transcribe íntegramente las explicaciones, teoremas, propiedades, ejemplos y ejercicios resueltos que aparezcan en los folios.
   - Si hay notas al margen o flechas explicativas, intégralas con claridad editorial (ej. bloques de notas `> **Nota:** ...`).
   - Mantén una redacción técnica, pulcra y rigurosa en español.

Estructura tu respuesta empezando directamente con el título de nivel 1:
# {titulo_bloque}
"""

def transcribir_bloque(nombre_archivo, titulo_bloque, lista_archivos):
    print(f"\n--- Transcribiendo {nombre_archivo}: {titulo_bloque} ({len(lista_archivos)} páginas) ---")
    
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

    models_to_try = ["gemini-3.5-flash", "gemini-flash-latest", "gemini-3.8-flash"]
    res = None
    for model_name in models_to_try:
        try:
            print(f"  Generando con {model_name}...")
            res = client.models.generate_content(
                model=model_name,
                contents=parts,
            )
            if res.text:
                break
        except Exception as e:
            print(f"    Fallo con {model_name}: {e}")
            time.sleep(3)

    if not res or not res.text:
        raise RuntimeError(f"No se pudo transcribir {nombre_archivo}")

    out_file = PUBLIC_ALGO / nombre_archivo
    out_file.write_text(res.text, encoding="utf-8")
    print(f"  ✅ Guardado en {out_file} ({len(res.text)} caracteres)")

def main():
    with open("/home/checa/Projects/javiercheca10.github.io/tools/digitalizar/clasificacion_algoritmica.json", "r") as f:
        data = json.load(f)

    # 1. Bloque 1: Introducción, Eficiencia y Recurrencias (IMG_1005, IMG_1006, IMG_1007)
    transcribir_bloque(
        "bloque1_eficiencia_recurrencias.md",
        "Eficiencia de Algoritmos y Resolución de Recurrencias",
        ["IMG_1005.HEIC", "IMG_1006.HEIC", "IMG_1007.HEIC"]
    )
    time.sleep(2)

    # 2. Bloque 2: Divide y Vencerás (IMG_1017 teórica primero, luego IMG_1008 ejercicios/umbral)
    transcribir_bloque(
        "bloque2_divide_y_venceras.md",
        "Diseño Divide y Vencerás y Umbral de Recursividad",
        ["IMG_1017.HEIC", "IMG_1008.HEIC"]
    )
    time.sleep(2)

    # 3. Bloque 3: Algoritmos Voraces (Greedy) (IMG_1009, IMG_1010, IMG_1011)
    transcribir_bloque(
        "bloque3_algoritmos_voraces.md",
        "Estrategia Voraz (Greedy), Mochila, Grafos y Dijkstra",
        ["IMG_1009.HEIC", "IMG_1010.HEIC", "IMG_1011.HEIC"]
    )
    time.sleep(2)

    # 4. Bloque 4: Algoritmo Húngaro de Asignación (IMG_1012)
    transcribir_bloque(
        "bloque4_algoritmo_hungaro.md",
        "Problema de Asignación y Algoritmo Húngaro",
        ["IMG_1012.HEIC"]
    )
    time.sleep(2)

    # 5. Bloque 5: Programación Dinámica (IMG_1013)
    transcribir_bloque(
        "bloque5_programacion_dinamica.md",
        "Programación Dinámica y Problema del Cambio",
        ["IMG_1013.HEIC"]
    )
    time.sleep(2)

    # 6. Bloque 6: Backtracking (IMG_1015, IMG_1016)
    transcribir_bloque(
        "bloque6_backtracking.md",
        "Backtracking (Búsqueda con Retroceso) y Restricciones",
        ["IMG_1015.HEIC", "IMG_1016.HEIC"]
    )

    print("\n🎉 ¡Todos los bloques de Algorítmica han sido transcritos con éxito!")

if __name__ == "__main__":
    main()
