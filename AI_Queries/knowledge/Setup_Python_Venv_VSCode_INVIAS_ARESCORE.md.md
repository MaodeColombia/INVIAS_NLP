---
tags:
  - VSCode
  - EntornoVirtual
  - Jupyter
  - GitBash
  - Configuración
  - ARESCORE
aliases:
  - Configuración VSCode Venv
  - Restablecimiento VSCode
  - Entorno Virtual INVIAS_ARESCORE
---
# Memoria de Configuración: Nuevo Entorno Virtual y Restablecimiento de VS Code

Este documento detalla los pasos para restablecer Visual Studio Code a su configuración de fábrica y configurar un nuevo entorno virtual de Python llamado `INVIAS_ARESCORE` para el proyecto.

---

## **Parte 1: Restablecer Visual Studio Code a Fábrica**

Este proceso eliminará todas tus configuraciones, temas, atajos de teclado y extensiones instaladas en VS Code, dejándolo como una instalación nueva.

1.  **Cierra completamente Visual Studio Code.** Asegúrate de que no haya ninguna instancia en ejecución.
2.  **Elimina las carpetas de configuración y datos de usuario de VS Code:**
    * Abre el Explorador de Archivos de Windows.
    * Navega a la siguiente ruta: `C:\Users\<Tu_Usuario>\AppData\Roaming\`
    * **Borra la carpeta llamada `Code`.**
    * Navega a la siguiente ruta: `C:\Users\<Tu_Usuario>\`
    * **Borra la carpeta llamada `.vscode`.** (Esta es una carpeta oculta; asegúrate de tener la opción "Mostrar elementos ocultos" activada en el Explorador de Archivos si no la ves).

    > **¡Advertencia!** Al borrar estas carpetas, perderás todas tus configuraciones personalizadas y extensiones. Tus entornos virtuales existentes (por ejemplo, `UNAD-dBjyLoWd`) **no se verán afectados ni se borrarán**.

---

## **Parte 2: Crear un Nuevo Entorno Virtual (`INVIAS_ARESCORE`) Fuera del Repositorio**

Crearemos el nuevo entorno virtual en tu ubicación centralizada para `venv`s (`.virtualenvs`).

1.  **Abre una terminal nueva de Git Bash.** (No la terminal integrada de VS Code, por ahora). Verifica que el prompt no tenga ningún prefijo de entorno virtual como `(UNAD)`.
2.  **Navega al directorio donde guardas tus entornos virtuales:**
    * La ruta común es `C:\Users\<Tu_Usuario>\.virtualenvs\`. Ajusta `<Tu_Usuario>` por tu nombre de usuario real (por ejemplo, `devel` o `Mao Martin`).
    ```bash
    cd /c/Users/<Tu_Usuario>/.virtualenvs/
    ```
3.  **Crea el nuevo entorno virtual con el nombre `INVIAS_ARESCORE`:**
    ```bash
    python -m venv INVIAS_ARESCORE
    ```
    Esto creará una nueva carpeta `INVIAS_ARESCORE` dentro de `C:\Users\<Tu_Usuario>\.virtualenvs\`.
4.  **Activa el nuevo entorno virtual:**
    ```bash
    cd INVIAS_ARESCORE/Scripts
    source activate
    ```
    Ahora tu prompt debería mostrar `(INVIAS_ARESCORE)`.
5.  **Instala los paquetes esenciales en este nuevo entorno virtual:**
    ```bash
    pip install jupyter notebook ipykernel chromadb pypdf python-dotenv
    ```
    Estos paquetes son necesarios para que tu notebook funcione correctamente con ChromaDB y para la interacción con Jupyter.
6.  **Registra explícitamente el nuevo entorno como un kernel de Jupyter:**
    ```bash
    python -m ipykernel install --user --name=INVIAS_ARESCORE --display-name="INVIAS NLP"
    ```
    > Registro del Entorno como Kernel de Jupyter:
    >
    > El comando `python -m ipykernel install --user --name=INVIAS_ARESCORE --display-name="Python (INVIAS ARESCORE Venv)"` tiene como objetivo principal registrar tu entorno virtual `INVIAS_ARESCORE` como un **kernel de Jupyter**. Esto permite que herramientas como Jupyter Notebook, JupyterLab y la extensión de Jupyter en VS Code puedan detectar y utilizar este entorno Python específico para ejecutar tus notebooks.
    >
    > **¿Qué hace y dónde se registra?**
    >
    > Cuando ejecutas este comando con la opción `--user`, se crea una nueva carpeta de configuración para el kernel dentro del directorio de kernels de Jupyter de tu usuario. Por ejemplo, en Windows, esto típicamente ocurre en `C:\Users\<Tu_Usuario>\AppData\Roaming\jupyter\kernels\INVIAS_ARESCORE\`. Dentro de esta carpeta, se genera un archivo `kernel.json`, que contiene las instrucciones para Jupyter sobre cómo iniciar el intérprete de Python de tu entorno virtual cuando seleccionas este kernel. Esto asegura que las librerías instaladas en tu `venv` sean las que realmente se utilicen en tus sesiones de Jupyter.
    >
    > Esto asegura que VS Code y Jupyter detecten este entorno como un kernel disponible.
7.  **Desactiva el entorno virtual en esta terminal por ahora:**
    ```bash
    deactivate
    ```
    El prefijo `(INVIAS_ARESCORE)` debería desaparecer de tu prompt.

---

## **Parte 3: Configurar Visual Studio Code para el Nuevo Entorno**

Con VS Code restablecido, lo configuraremos para usar tu nuevo entorno.

1.  **Inicia Visual Studio Code.** Se iniciará con las configuraciones predeterminadas de fábrica.
2.  **Instala las extensiones esenciales:**
    * Ve al icono de Extensiones (cuadrados en la barra lateral izquierda, o `Ctrl + Shift + X`).
    * Busca e instala la extensión **"Python" de Microsoft**.
    * Busca e instala la extensión **"Jupyter" de Microsoft**.
3.  **Abre tu carpeta de proyecto existente en VS Code:**
    * Ve a `File > Open Folder...`
    * Navega y selecciona la **carpeta raíz de tu proyecto** (por ejemplo, `C:\Users\devel\UNAD\INVIAS\INVIAS_NLP`).
4.  **Selecciona el intérprete Python para tu espacio de trabajo:**
    * Abre la **Paleta de Comandos** de VS Code presionando `Ctrl + Shift + P`.
    * En la barra de búsqueda, escribe `Python: Select Interpreter` y selecciona el comando.
    * VS Code escaneará tu sistema y presentará una lista de intérpretes. Busca y selecciona tu nuevo entorno virtual: **`INVIAS NLP`**. La ruta que se muestra debería apuntar a `C:\Users\<Tu_Usuario>\.virtualenvs\INVIAS_ARESCORE\Scripts\python.exe`.
5.  **Abre una nueva terminal integrada en VS Code:**
    * Ve a `Terminal > New Terminal`.
    * **Verifica que tu nuevo entorno virtual `(INVIAS_ARESCORE)` se active automáticamente en el prompt de Git Bash.** Si VS Code está configurado correctamente, debería hacerlo.
