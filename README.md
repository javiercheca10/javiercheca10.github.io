# javiercheca10.github.io 🚀

Portfolio personal y plataforma de recursos académicos del **Doble Grado en Ingeniería Informática y ADE** en la **Universidad de Granada (UGR)**.

Diseñado con una estética moderna **Bento Grid**, temas claro/oscuro persistentes, búsqueda reactiva en tiempo real y arquitectura de alto rendimiento con **Astro** y **Tailwind CSS**.

🌐 **Sitio web:** [https://javiercheca10.github.io](https://javiercheca10.github.io)

---

## 🏛️ Estructura del Sitio

- **Inicio (`/`)**: Bento Grid interactivo con presentación, proyectos destacados, métricas académicas de la UGR, stack tecnológico (desarrollo y gestión empresarial) y contacto.
- **Universidad (`/universidad`)**: Catálogo íntegro de las **60 asignaturas** oficiales de los 5 cursos del Doble Grado (ETSIIT & FCEE) con enlaces a guías docentes oficiales, buscador instantáneo por código/nombre y filtros por curso.
- **Proyectos (`/proyectos`)**: Galería de proyectos de ingeniería del software, optimización combinatoria (Google OR-Tools CP-SAT), aplicaciones de escritorio y herramientas de análisis.

---

## 🛠️ Stack Tecnológico

- **Framework**: [Astro](https://astro.build/) (v7) — Generación estática (SSG) de máximo rendimiento (100/100 Lighthouse).
- **Estilos**: [Tailwind CSS](https://tailwindcss.com/) — Bento Grid responsivo, modo oscuro y animaciones sutiles.
- **Despliegue**: GitHub Pages con GitHub Actions (`.github/workflows/deploy.yml`).

---

## 💻 Desarrollo Local

```bash
# 1. Instalar dependencias
npm install

# 2. Iniciar servidor de desarrollo
npm run dev

# 3. Compilar para producción
npm run build

# 4. Probar la versión de producción localmente
npm run preview
```

---

## 📚 Cómo añadir o actualizar contenido

### Añadir o modificar un Proyecto:
Edita [`src/data/projects.json`](src/data/projects.json). Cada proyecto cuenta con título, descripción, tags tecnológicos, insignias y enlaces a GitHub / Demo.

### Añadir apuntes o recursos a una Asignatura:
1. Las asignaturas están definidas en [`src/data/courses.json`](src/data/courses.json).
2. Puedes colocar tus PDFs o archivos en la carpeta `public/subjects/<codigo>/` y enlazarlos en los datos.

### Modificar tu Información de Perfil:
Edita [`src/data/profile.json`](src/data/profile.json) para actualizar biografía, habilidades, redes y enlaces de contacto.

---

## 📄 Licencia

MIT © [Javier Checa](https://github.com/javiercheca10)
