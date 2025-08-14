---
title: Registro de todos los paquetes usados en el proyecto
---
```toc
```
# Paquetes instalados

Comandos para listar los paquetes instalados en tu entorno de Python desde la terminal o consola Bash

## Procedimiento de instalacion de paquetes

Pasos estandarizados para instalar un nuevo paquete de Python en el proyecto, documentando adecuadamente el proceso.

### 1. Preparación del entorno

Antes de ejecutar cualquier comando de instalación, asegúrate de cumplir con los siguientes requisitos:

- **Estar en la carpeta raíz del repositorio.**
- **El entorno virtual (`venv`) debe estar activo.**

### 2. Instalación y registro del paquete

Para instalar el paquete y registrar las salidas en un log, utiliza el siguiente comando en la terminal:

```bash
pip install <nombre_del_paquete> > ./support/installed_packeges_log/stdout.txt 2> ./support/installed_packeges_log/stderr.txt
```

***Nota:** Este comando redirige la salida estándar (`stdout`) a un archivo y los errores (`stderr`) a otro.*

### 3. Validación y gestión de logs

- **Revisión de errores:**

  - Valida el contenido del archivo `stderr.txt` ubicado en `./support/installed_packeges_log/`.
  - Si no hay errores, procede al siguiente paso.
  - Si se encuentran errores, es crucial solucionarlos antes de realizar un *commit*.

- **Renombrado del log de éxito:**

  - Si la instalación fue exitosa (sin errores), renombra el archivo `stdout.txt` con el formato `<nombre_del_paquete>_success.txt` y guárdalo en la misma carpeta (`installed_packeges_log`).

> Para más detalles sobre la gestión de `stdout` y `stderr`, consulta el archivo de referencia `stdout_stderr_logging` en la ruta `./AI_Queries/knowledge/stdout_stderr_logging`.

### 4. Actualización del archivo de dependencias

Finalmente, actualiza el archivo `requirements.txt` para registrar el nuevo paquete instalado.

```bash
pip freeze > ./support/requirements.txt
```

*Puedes consultar el archivo `requirements.txt` para verificar las dependencias del proyecto.*

## Consulta de paquetes instalados

- [requirements.txt](requirements.txt)

- [installed_packeges_log/](installed_packeges_log)

- ```bash
  pip list
  ```
  - Otras opciones útiles

    - **Con formato detallado (JSON):**
      
      ```bash
      pip list --format=json
      ```
    
    - **Para ver los paquetes y sus dependencias en árbol:**
    
      ```bash
      pipdeptree
      ```
    
      *(Necesita instalación previa con `pip install pipdeptree`)*
    
    - **Para exportar a un archivo de texto:**
    
      ```bash
      pip freeze > ./support/requirements.txt
      ```

## `gradio`

Se instaló para construir interfaces web interactivas de manera sencilla y rápida sobre modelos de Machine Learning. Permite crear demos accesibles desde el navegador sin necesidad de desarrollo frontend. Es compatible con funciones de Python y facilita la integración con los Spaces de Hugging Face, lo que resulta esencial para la experimentación práctica del curso.

## `tensorflow`

Se instaló para construir, entrenar y desplegar modelos de aprendizaje profundo. TensorFlow proporciona una API flexible y de alto rendimiento que permite definir redes neuronales de forma declarativa o imperativa, y ejecutar operaciones tanto en CPU como en GPU. Es una herramienta fundamental para experimentar con modelos de Machine Learning complejos dentro del curso, especialmente al momento de construir demos funcionales que involucren modelos entrenados previamente o personalizados. 

## `pipdeptree`

Se instaló para generar y visualizar el árbol de dependencias de los paquetes Python instalados. **pipdeptree** es una herramienta esencial para entender cómo se relacionan las librerías en tu entorno, facilitar la detección de conflictos y optimizar la gestión de dependencias en proyectos de Machine Learning y desarrollo en Python.

## `load_dotenv` de `python-dotenv`

Se instaló la librería **`python-dotenv`** para facilitar la gestión segura de **variables de entorno** en el proyecto. Esta herramienta permite cargar configuraciones sensibles, como claves de API y contraseñas, desde un archivo dedicado llamado `.env`. Al no incluir este archivo en el control de versiones (como Git), se mantiene la seguridad de las credenciales, evitando que queden expuestas en el código fuente o en repositorios públicos.

La función principal de esta librería, **`load_dotenv()`**, es la que se encarga de leer el contenido del archivo `.env` y de inyectar esas variables en el entorno de ejecución del script de Python. Esto es crucial para el desarrollo colaborativo, ya que cada desarrollador puede tener su propia configuración local sin modificar el código base. Además, garantiza que el despliegue en entornos de producción sea más seguro y manejable, ya que las variables pueden ser gestionadas externamente al código.

## `matplotlib`

Se instaló para crear gráficos 2D y figuras estáticas (líneas, barras, histogramas, scatter, etc.) en notebooks y scripts de análisis. Matplotlib actúa como la base para visualizaciones científicas y es frecuentemente usada junto a librerías de más alto nivel para producir gráficos reproducibles en informes y presentaciones del proyecto.

## `nbconvert`

Se instaló para convertir Jupyter Notebooks a formatos como HTML, PDF o Markdown, y para automatizar la exportación de notebooks como parte de la generación de documentación o reportes. Nbconvert facilita la publicación y la revisión de resultados reproducibles producidos en los notebooks del repositorio.

## `pandas`

Se instaló para la manipulación y análisis de datos en estructuras tabulares (`DataFrame`). Pandas proporciona las utilidades necesarias para limpieza, transformación, agregación y preparación de datos, y es la biblioteca principal para cualquier pipeline de preprocesamiento dentro del proyecto.

## `playwright`

Se instaló para automatización y pruebas de navegadores (Chrome, Firefox, WebKit). Playwright permite crear pruebas end-to-end (E2E), generar capturas automáticas y automatizar interacciones en demos web, lo que es útil tanto para testing como para la validación de interfaces y flujos en las demos de Gradio.

## `seaborn`

Se instaló como complemento de Matplotlib para facilitar la creación de gráficos estadísticos y mejorar la estética por defecto de las visualizaciones. Seaborn simplifica operaciones comunes de análisis exploratorio y genera visualizaciones informativas con menos líneas de código.
