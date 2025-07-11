---
title: Uso de `git mv` en lugar de `mv`
tags:
  - troubleshooting
---
# Uso de `git mv`

## Cómo Cambiar Formalmente el Nombre de un Archivo en un Repositorio Git

**Para cambiar el nombre de un archivo o carpeta dentro de un repositorio Git, la forma formal y recomendada es utilizar el comando `git mv`.** Este comando no solo renombra el archivo en tu sistema de archivos, sino que también le informa explícitamente a Git de este movimiento, asegurando que el historial del archivo se mantenga correctamente.

### Método Formal: Usar `git mv` para Renombrar Archivos

Git tiene su propio comando para mover y renombrar archivos y carpetas, lo que garantiza que el cambio se registre como tal en el historial del repositorio.

**Para renombrar un archivo:**

```bash
git mv <nombre_anterior_del_archivo> <nuevo_nombre_del_archivo>
```

**Ejemplo:** Renombrar `documento_viejo.txt` a `documento_nuevo.txt`

```bash
git mv documento_viejo.txt documento_nuevo.txt
```

## Mover archivos en un repositorio Git usando Bash

### `git mv` en lugar de `mv`

Al mover archivos en un repositorio Git usando Bash, el archivo **parece nuevo** para Git y aparece como **untracked**, mientras que el original aparece como **deleted**, **a menos que Git detecte automáticamente que fue un "rename" o "move"**. Para que Git registre correctamente ese movimiento como un cambio de ubicación (y no como eliminación + creación) o como un cambio de nombre, sigue estos pasos:

- 1. Usa `git mv` en lugar de `mv`

  Git tiene su propio comando para mover archivos y carpetas:

  ```bash
  git mv carpeta_origen/archivo.ext carpeta_destino/
  ```

  O para mover todo el contenido:

  ```bash
  mkdir -p carpeta_destino
  git mv carpeta_origen/* carpeta_destino/
  ```

  > Esto le **informa a Git explícitamente** del movimiento y lo registra  como tal en el historial.

- 2. Si ya usaste `mv` por accidente

  Si ya hiciste `mv` normal, puedes hacer que Git lo reconozca como un movimiento con:

  ```bash
  git add -A
  ```

  Git intentará detectar automáticamente los renames/moves basándose en el contenido de los archivos. Git es *heurístico* en esto (por defecto considera que un archivo movido debe tener al menos un 50% de contenido similar para que lo reconozca como "renombrado").

- 3. Verificar que lo detectó como rename

  Después de agregar, puedes verificarlo con:

  ```bash
  git status
  ```

  Y mejor aún:

  ```bash
  git diff --cached --name-status
  ```

  Si ves algo como:

  ```bash
  R100    carpeta_origen/archivo.ext    carpeta_destino/archivo.ext
  ```

  Significa que Git detectó correctamente el "rename" (`R100` = rename con 100% de contenido idéntico).

📝 En resumen:

- Usa `git mv` para que Git registre correctamente el movimiento.
- Si ya usaste `mv`, puedes usar `git add -A` y Git intentará inferir el   movimiento.
- Verifica con `git diff --cached --name-status`.
