# Digitalizador de Apuntes Manuscritos con IA 📝

Convierte lotes de fotos de folios manuscritos o archivos PDF a **Markdown con fórmulas LaTeX (`$...$`)** o **LaTeX puro**.

---

## 🚀 Requisitos

Tener instalado `uv` (ya instalado en tu sistema) y una API Key de Gemini (gratuita e instantánea en [aistudio.google.com/apikey](https://aistudio.google.com/apikey)).

Puedes exportar tu API Key en tu terminal o crear un archivo `.env`:
```bash
export GEMINI_API_KEY="tu_clave_aqui"
```

---

## 📸 Cómo usarlo con una carpeta de fotos

1. Haz fotos a tus folios (con buena luz) y guárdalas en una carpeta, por ejemplo:
   ```
   ~/Downloads/calculo_tema1/
     ├── 1.jpg
     ├── 2.jpg
     ├── 3.jpg
     └── 4.jpg
   ```
   *(El script ordena automáticamente `1.jpg`, `2.jpg`... `10.jpg` de forma natural)*.

2. Ejecuta el digitalizador con `uv`:
   ```bash
   cd ~/Projects/javiercheca10.github.io/tools/digitalizar
   uv run digitalizar.py ~/Downloads/calculo_tema1/ --asignatura CAL --tema "Tema 1: Límites y Continuidad"
   ```

3. El script generará un archivo `calculo_tema1_apuntes.md` con:
   - Todo el texto manuscrito transcrito en limpio.
   - Fórmulas matemáticas en sintaxis estricta de LaTeX (`$f(x) = \lim \dots$`).
   - Teoremas, demostraciones y ejemplos destacados.
   - Tablas de contabilidad o matrices empresariales formateadas.

---

## 📄 Cómo usarlo con un PDF escaneado

También puedes pasarle directamente un archivo PDF escaneado:

```bash
uv run digitalizar.py /ruta/a/apuntes_escaneados.pdf -o Tema2_EDO.md
```
