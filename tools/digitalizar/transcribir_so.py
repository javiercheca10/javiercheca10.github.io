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
PUBLIC_SO = Path("/home/checa/Projects/javiercheca10.github.io/public/subjects/SO")

PROMPT_TRANSCRIBIR = """
Eres un profesor catedrático universitario de Sistemas Operativos e Ingeniería de Software en la ETSIIT de la Universidad de Granada (UGR).

Estás transcribiendo un bloque de apuntes manuscritos técnicos de la asignatura 'Sistemas Operativos': '{titulo_bloque}'.

DIRECTRICES EDITORIALES Y DE CALIDAD:
1. Formato de Salida: Markdown técnico impecable con soporte completo de código C/POSIX, diagramas de texto y fórmulas KaTeX.
2. REGLA ESTRICTA DE LIMPIEZA:
   - NUNCA incluyas frases como "Escaneado con CamScanner", "CamScanner" o marcas de agua procedentes de digitalización física en el texto final. Elimínalas por completo.
3. Estructuras de Datos y Kernel Internals:
   - Cuando se describan estructuras del kernel de Linux (`task_struct`, `mm_struct`, `vm_area_struct`, `struct page`, `kmem_cache`, `super_block`, `inode`, `dentry`, `file`), represéntalas con bloques de código ```c o diagramas de memoria.
4. Diagramas de Traducción y Memoria:
   - Muestra esquemas claros de traducción de direcciones (Paginación con RBTP, Segmentación con RBTS/STLR, Tablas multinivel PGD/PMD/PTE, Asignación indexada y Superbloque/inodos de Ext2) usando tablas Markdown o diagramas ASCII estructurados.
5. Algoritmos y Trazas:
   - Para políticas de sustitución de páginas (Óptimo, FIFO, LRU, Algoritmo del Reloj), métodos de asignación de espacio (FAT, i-nodos) y DMA/Interrupciones, presenta trazas paso a paso bien formateadas.
6. Redacción Técnica:
   - Mantén un tono académico riguroso, formal y preciso en español.

Estructura tu respuesta empezando directamente con el título de nivel 1:
# {titulo_bloque}
"""

def transcribir_bloque(subpath_destino, titulo_bloque, lista_archivos):
    out_file = PUBLIC_SO / subpath_destino
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
        print("  Esperando 6s antes de reintentar...")
        time.sleep(6)

    if not res or not res.text:
        raise RuntimeError(f"No se pudo transcribir {subpath_destino}")

    # Limpieza preventiva por si el LLM dejó escapar algún CamScanner
    texto_limpio = res.text
    for linea in ["Escaneado con CamScanner", "Escaneado con Camscanner", "CamScanner", "Scanned with CamScanner"]:
        texto_limpio = texto_limpio.replace(linea, "")

    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(texto_limpio, encoding="utf-8")
    print(f"  ✅ Guardado en {out_file} ({len(texto_limpio)} caracteres)")

def main():
    # Orden coherente para el Bloque 1: Arquitectura de Computador (IMG_1075, IMG_1076, IMG_1077)
    # y luego Estructuras y Arquitecturas de S.O. (IMG_1045, IMG_1046, IMG_1047, IMG_1048)
    transcribir_bloque(
        "bloque1_arquitectura_y_estructuras_so.md",
        "Tema 1: Arquitectura de Computadores y Estructuras del Sistema Operativo",
        ["IMG_1075.HEIC", "IMG_1076.HEIC", "IMG_1077.HEIC", "IMG_1045.HEIC", "IMG_1046.HEIC", "IMG_1047.HEIC", "IMG_1048.HEIC"]
    )
    time.sleep(2)

    # Bloque 2: Gestión de Memoria y Memoria Virtual (IMG_1049 a IMG_1057)
    transcribir_bloque(
        "bloque2_gestion_memoria_virtual.md",
        "Tema 2: Gestión de Memoria Principal y Memoria Virtual",
        ["IMG_1049.HEIC", "IMG_1050.HEIC", "IMG_1051.HEIC", "IMG_1052.HEIC", "IMG_1053.HEIC", "IMG_1054.HEIC", "IMG_1055.HEIC", "IMG_1056.HEIC", "IMG_1057.HEIC"]
    )
    time.sleep(2)

    # Bloque 3: Gestión de Memoria en el Kernel de Linux (IMG_1058 a IMG_1062)
    transcribir_bloque(
        "bloque3_memoria_kernel_linux.md",
        "Tema 3: Gestión de Memoria a Bajo Nivel en Linux y Cachés de Páginas",
        ["IMG_1058.HEIC", "IMG_1059.HEIC", "IMG_1060.HEIC", "IMG_1061.HEIC", "IMG_1062.HEIC"]
    )
    time.sleep(2)

    # Bloque 4: Sistemas de Archivos y Ext2 en Linux (IMG_1063 a IMG_1074)
    transcribir_bloque(
        "bloque4_sistemas_archivos_y_ext2.md",
        "Tema 4: Gestión de Archivos, VFS y Estructura Interna de Ext2",
        ["IMG_1063.HEIC", "IMG_1064.HEIC", "IMG_1065.HEIC", "IMG_1066.HEIC", "IMG_1067.HEIC", "IMG_1068.HEIC", "IMG_1069.HEIC", "IMG_1070.HEIC", "IMG_1071.HEIC", "IMG_1072.HEIC", "IMG_1073.HEIC", "IMG_1074.HEIC"]
    )

    print("\n🎉 ¡Todos los bloques temáticos de Sistemas Operativos han sido transcritos con éxito!")

if __name__ == "__main__":
    main()
