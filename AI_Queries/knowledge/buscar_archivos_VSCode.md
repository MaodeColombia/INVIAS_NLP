# Buscar archivos por nombre de forma muy eficiente en **Visual Studio Code (VSCode)**

## ✅ 1. **Buscar archivo por nombre (rápido)**

### ⌨️ **Atajo de teclado (recomendado):**

* **Windows/Linux**: `Ctrl + P`
* **macOS**: `Cmd + P`

Luego escribe el nombre del archivo (o parte de él). Ejemplos:

```
main.py
index
2024S-VBOG
```

VSCode te irá mostrando coincidencias en tiempo real.

---

## ✅ 2. **Buscar por nombre exacto (incluyendo subcarpetas)**

Presiona `Ctrl + P` o `Cmd + P`, y usa un patrón como:

* `./subcarpeta/mi_archivo.txt`
* `**/mi_archivo.txt` → busca el archivo en cualquier subcarpeta

---

## ✅ 3. **Buscar dentro de archivos (contenido)**

Si en lugar del nombre quieres buscar contenido **dentro de los archivos**:

* Presiona `Ctrl + Shift + F` (Windows/Linux)
* O `Cmd + Shift + F` (macOS)

Escribe el texto que estás buscando (por ejemplo: `radicado` o `VBOG-056845`) y VSCode te mostrará en qué archivos aparece.

---

## ✅ 4. **Filtrar por extensión o patrón**

En `Ctrl + P`, puedes usar:

* `*.pdf` para ver todos los PDFs
* `*VBOG*` para ver todos los archivos cuyo nombre contenga "VBOG"
* `!*.test.js` para excluir archivos que coincidan

