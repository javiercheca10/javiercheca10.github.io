# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "google-genai",
#     "pillow",
#     "python-dotenv",
# ]
# ///

"""
Script de digitalización automática de apuntes manuscritos a LaTeX / Markdown.
Acepta tanto una carpeta llena de fotos (JPG, PNG...) como un archivo PDF escaneado.

Uso:
    uv run digitalizar.py /ruta/a/carpeta_con_fotos/ --asignatura CAL --tema "Tema 1: Límites y Continuidad"
    uv run digitalizar.py /ruta/a/archivo.pdf -o salida.md
"""

import os
import re
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def natural_sort_key(path: Path):
    """Ordena nombres de archivo de forma natural (1, 2, 10 en vez de 1, 10, 2)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', path.name)]

def get_images_from_input(input_path: Path) -> list[Path]:
    """Obtiene y ordena la lista de imágenes a procesar."""
    valid_exts = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
    
    if input_path.is_dir():
        images = [p for p in input_path.iterdir() if p.suffix.lower() in valid_exts]
        images.sort(key=natural_sort_key)
        return images
    elif input_path.is_file() and input_path.suffix.lower() in valid_exts:
        return [input_path]
    elif input_path.is_file() and input_path.suffix.lower() == ".pdf":
        return [input_path]
    else:
        return []

SYSTEM_PROMPT = r"""Eres un asistente académico experto en transcripción de apuntes universitarios manuscritos para el Doble Grado en Ingeniería Informática y ADE.

Tu objetivo es transcribir fielmente las imágenes de los folios manuscritos a un documento limpio, estructurado y profesional en formato MARKDOWN con matemáticas en sintaxis estricta de LATEX.

REGLAS DE TRANSCRIPCIÓN:
1. **Fórmulas Matemáticas**:
   - Fórmulas en línea: usa `$ ... $` (ej: `$f(x) = \lim_{x \to 0} \frac{\sin x}{x} = 1$`).
   - Fórmulas en bloque / demostraciones: usa `$$ ... $$` o entornos como `\\begin{aligned} ... \\end{aligned}`.
   - Transcribe todas las operaciones, matrices, integrales, derivadas y límites con sintaxis LaTeX estándar exacta.
   - No te saltes pasos matemáticos que aparezcan en los folios.

2. **Estructura y Organización**:
   - Organiza con jerarquía clara: `# Título Principal`, `## Sección`, `### Subsección`.
   - Teoremas, lemas y definiciones: usa bloques destacados (ej: `> **Teorema 1.1 (Bolzano)**: ...`).
   - Demostraciones: `> *Demostración*: ... $\\blacksquare$`.
   - Ejemplos resueltos: `#### Ejemplo: ...`.

3. **Tablas y ADE**:
   - Si hay tablas de contabilidad (asientos del libro diario, balances), tablas de verdad, o matrices de decisión empresarial, conviértelas a tablas Markdown formateadas (`| Columna 1 | Columna 2 |`).

4. **Código y Algoritmos**:
   - Si hay pseudocódigo o fragmentos de código (C++, Python, Java, SQL), transcríbelos dentro de bloques de código con resaltado de sintaxis (```cpp, ```python).

5. **Corrección y Claridad**:
   - Si hay tachones o correcciones manuscritas en el folio, transcribe la versión final corregida.
   - Corrige erratas tipográficas obvias del autor si están claras por el contexto matemático, pero sé fiel a las explicaciones.
   - Devuelve DIRECTAMENTE el contenido Markdown final, sin saludos ni introducciones conversacionales.
"""

def main():
    parser = argparse.ArgumentParser(description="Digitalizador de apuntes manuscritos a Markdown/LaTeX con IA")
    parser.add_argument("input_path", type=Path, help="Ruta a la carpeta con fotos o archivo PDF")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Archivo de salida (por defecto: apuntes_digitalizados.md)")
    parser.add_argument("--asignatura", type=str, default="", help="Código o nombre de la asignatura (ej. CAL, EDO, FP)")
    parser.add_argument("--tema", type=str, default="", help="Título o tema de los apuntes (ej. 'Tema 1: Límites')")
    parser.add_argument("--format", choices=["md", "tex"], default="md", help="Formato de salida (md o tex)")
    args = parser.parse_args()

    input_path = args.input_path.expanduser().resolve()
    if not input_path.exists():
        print(f"❌ Error: La ruta '{input_path}' no existe.", file=sys.stderr)
        sys.exit(1)

    # Verificar API key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("\n⚠️ No se ha detectado la variable GEMINI_API_KEY.")
        print("Puedes obtener una API key gratuita e instantánea en: https://aistudio.google.com/apikey")
        api_key = input("Pega tu API Key de Gemini aquí (o presiona Enter para salir): ").strip()
        if not api_key:
            print("Operación cancelada. Configura export GEMINI_API_KEY='tu_clave' en tu terminal.")
            sys.exit(1)
        os.environ["GEMINI_API_KEY"] = api_key

    from google import genai
    from google.genai import types
    from PIL import Image

    client = genai.Client(api_key=api_key)

    images = get_images_from_input(input_path)
    if not images:
        print(f"❌ No se encontraron imágenes (JPG, PNG, WEBP) ni PDF en: {input_path}")
        sys.exit(1)

    print(f"\n📂 Procesando entrada: {input_path}")
    print(f"📄 Archivos detectados ({len(images)} página/s en orden natural):")
    for idx, img in enumerate(images, 1):
        print(f"   [{idx:02d}] {img.name}")

    output_path = args.output
    if not output_path:
        base_name = input_path.name if input_path.is_dir() else input_path.stem
        ext = ".tex" if args.format == "tex" else ".md"
        output_path = Path.cwd() / f"{base_name}_apuntes{ext}"

    # Preparar contenido para Gemini
    contents = [SYSTEM_PROMPT]
    context_info = []
    if args.asignatura:
        context_info.append(f"Asignatura: {args.asignatura}")
    if args.tema:
        context_info.append(f"Tema / Título: {args.tema}")
    if context_info:
        contents.append("INFORMACIÓN DEL DOCUMENTO:\n" + "\n".join(context_info))

    print("\n⏳ Subiendo y procesando páginas con Gemini...")
    for idx, img_path in enumerate(images, 1):
        if img_path.suffix.lower() == ".pdf":
            uploaded_file = client.files.upload(file=str(img_path))
            contents.append(uploaded_file)
        else:
            img = Image.open(img_path)
            contents.append(f"--- [PÁGINA {idx}] ---")
            contents.append(img)

    contents.append("Por favor, transcribe todas las páginas anteriores en orden cronológico siguiendo las reglas especificadas.")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
            config=types.GenerateContentConfig(
                temperature=0.2,
            )
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"\n✅ ¡Transcripción completada con éxito!")
        print(f"📁 Archivo guardado en: {output_path}")
        print(f"📊 Tamaño: {len(response.text)} caracteres.")
        print(f"\nPuedes abrirlo y revisarlo en tu editor o visor favorito.")

    except Exception as e:
        print(f"\n❌ Error durante el procesamiento: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
