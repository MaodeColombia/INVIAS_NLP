---
tags:
  - jupyter
  - pandoc
  - virtualenv
  - pdf
  - windows
  - nbconvert
title: Exportar notebooks a PDF con Pandoc en entorno virtual (Windows)
created: 2025-06-28
---

# Configuración y uso de Pandoc en entorno virtual Python para exportación de Notebooks a PDF

Este documento describe el procedimiento seguido para habilitar la exportación de archivos `.ipynb` (Jupyter Notebook) a formato `.pdf` en un entorno virtual de Python en Windows 10, integrando `pandoc` y `xelatex`.

## Procedimiento

### 1. Instalación de Pandoc (versión portable)

Se descargó y descomprimió **pandoc-3.7.0.2-windows-x86_64.zip** desde [https://github.com/jgm/pandoc/releases](https://github.com/jgm/pandoc/releases) en la siguiente ruta:

```bash
C:\Users\devel\.virtualenvs\pandoc-3.7.0.2\
```

> Dentro de esa carpeta se encuentra `pandoc.exe`.

### 2. Creación de un enlace simbólico (`symlink`) dentro del entorno virtual

Para que el entorno virtual `UNAD-dBjyLoWd` pueda acceder a `pandoc`, se creó un vínculo simbólico que apunta al ejecutable real.

#### Comando utilizado (desde CMD con permisos de administrador):

```cmd
mklink "C:\Users\devel\.virtualenvs\UNAD-dBjyLoWd\Scripts\pandoc.exe" "C:\Users\devel\.virtualenvs\pandoc-3.7.0.2\pandoc.exe"
```

> Aunque inicialmente se intentó resolver el error `PandocMissing` añadiendo la ruta de instalación de `pandoc.exe` (versión portable) a la variable de entorno del sistema (`PATH`), esta solución no resultó efectiva dentro del entorno virtual de Python. Esto se debe a que los entornos virtuales aíslan su contexto de ejecución y no siempre heredan correctamente las variables de entorno globales del sistema operativo.

#### Resultado esperado

```plaintext
vínculo simbólico creado para C:\Users\devel\.virtualenvs\UNAD-dBjyLoWd\Scripts\pandoc.exe <<===>> C:\Users\devel\.virtualenvs\pandoc-3.7.0.2\pandoc.exe
```

Esto permite a `jupyter nbconvert` acceder correctamente a `pandoc.exe` desde el entorno virtual.

### 3. Confirmación del entorno

Se verificó que ambos componentes estén operativos:

```bash
pandoc --version
xelatex --version
```

Ambos comandos deben retornar versiones instaladas correctamente.

## Generación del PDF desde terminal

### Comando final usado:

```bash
jupyter nbconvert --to pdf U2F3.ipynb
```

Este comando convierte el archivo `U2F3.ipynb` a `U2F3.pdf` en el mismo directorio. Internamente utiliza:

- `pandoc` para transformar contenido Markdown/HTML a LaTeX.

- `xelatex` para compilar el `.tex` generado en un `.pdf`.

### Proceso alternativo desde Visual Studio Code

Desde la interfaz de VS Code (con la extensión Jupyter instalada):

1. Abre el archivo `.ipynb` en VS Code.
2. En la parte superior derecha, haz clic en los tres puntos `⋯`.
3. Selecciona la opción:
   **Export As > PDF**. Si `nbconvert`, `pandoc` y `xelatex` están bien configurados en el entorno activo, el PDF se generará sin errores.

## Estructura de carpetas después del proceso

```plaintext
.virtualenvs/
├── UNAD-dBjyLoWd/
│   └── Scripts/
│       └── pandoc.exe  (enlace simbólico al original)
├── pandoc-3.7.0.2/
│   └── pandoc.exe      (ejecutable real de pandoc)
```

## Lecciones aprendidas

- `nbconvert` requiere que los ejecutables externos (`pandoc`, `xelatex`) estén visibles en el entorno virtual.
- Los symlinks permiten conectar herramientas externas sin duplicar archivos.
- `mklink` es una herramienta poderosa para solucionar problemas de aislamiento en entornos virtuales.
