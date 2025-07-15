---
title: "Uso de `git restore .`"
tags: git, comandos, obsidian
---
# Uso de `git restore .`

`git restore .` es un comando introducido en Git 2.23 para restaurar archivos en tu directorio de trabajo desde el índice o desde un commit (por defecto, `HEAD`). En particular, `git restore .` deshace todos los cambios no confirmados (staged o unstaged) y recupera eliminaciones de archivos.

## ¿Cuándo usarlo?

* **Recuperar archivos borrados accidentalmente**: Si eliminaste archivos en tu directorio pero aún no confirmaste (commit) esa eliminación.
* **Descartar cambios locales**: Si tienes modificaciones en tu directorio de trabajo que aún no deseas confirmar y quieres volver al estado de `HEAD`.

## Sintaxis básica

```bash
git restore .
```

* El punto (`.`) indica el directorio actual y sus subdirectorios.
* Sin opciones adicionales, Git restablece cada archivo al contenido de `HEAD`.

## Ejemplos prácticos

1. **Ver estado antes de restaurar**

   ```bash
   git status
   ```

   Verás listados los archivos eliminados (`deleted:`) y modificaciones pendientes.

2. **Restaurar todo**

   ```bash
   git restore .
   ```

   * Los archivos borrados reaparecen.
   * Otras modificaciones locales se descartan.

3. **Restaurar solo un archivo específico**

   ```bash
   git restore ruta/al/archivo.txt
   ```

4. **Si quieres restablecer al estado del índice (no de `HEAD`)**

   ```bash
   git restore --staged .      # Quita archivos del área de stage
   git restore .               # Luego descarta cambios en el directorio de trabajo
   ```

   Esa línea se refiere a un caso en el que quieres deshacer únicamente los cambios que ya has “staged” (los que añadiste al índice con `git add`), sin tocar aún las modificaciones que están en tu directorio de trabajo.

   1. **Restablecer al índice**:

      ```bash
      git restore --staged .
      ```
      Este comando quita del área de *staging* todos los cambios que habías preparado para el próximo commit, devolviendo esos archivos al estado que tenían en el índice (es decir, antes de hacer `git add`). Tras ejecutarlo, los archivos modificados siguen en tu carpeta, pero ya no están listos para commitear.

   2. **(Opcional) Luego descartar los cambios en el directorio**:

      ```bash
      git restore .
      ```

      Con esto, ahora sí tiras tus modificaciones locales, restaurando cada archivo al contenido exacto de `HEAD`.

   En resumen:

   * **`--staged`** apunta al índice (lo que se incluirá en el commit),
   * mientras que sin opciones (`git restore .`) se actúa sobre el directorio de trabajo y, por defecto, recupera desde el último commit (`HEAD`).


## Opciones útiles

* `--staged` : Restablece archivos solo en el área de stage (index).
* `--source <commit>` : Especifica un commit distinto de HEAD (por ejemplo, `git restore --source HEAD~1 archivo.txt`).

## Comandos relacionados

* `git checkout -- .` : Alternativa en Git <2.23 para descartar cambios.
* `git reset --hard HEAD` : Restablece índice y directorio de trabajo, pero **cuidado**, descarta también nuevos archivos no rastreados.
* `git clean -fd` : Elimina archivos no rastreados y directorios.

---

*Este archivo está pensado para integrarse en Obsidian como parte de tu base de conocimientos sobre Git.*
