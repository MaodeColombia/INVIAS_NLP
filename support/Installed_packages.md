# Paquetes instalados

Comandos para listar los paquetes instalados en tu entorno de Python desde la terminal o consola Bash

- Opción principal (recomendada)

  ```bash
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

[Installed_packeges_log/tensorflow_success.txt](installed_packeges_log/tensorflow_success.txt)  
[requirements.txt](requirements.txt)  

Comandos ejecutados

- `pip install tensorflow > ./support/installed_packeges_log/stdout.txt 2> ./support/installed_packeges_log/stderr.txt`  
  
- La estrucura de este resgistro es `<package>_success.txt`

- `pip freeze > ./support/requirements.txt`  

- [./AI_Queries/knowledge/stdout_stderr_logging](../AI_Queries/knowledge/stdout_stderr_logging.md)
  

## `pipdeptree`

Se instaló para generar y visualizar el árbol de dependencias de los paquetes Python instalados. **pipdeptree** es una herramienta esencial para entender cómo se relacionan las librerías en tu entorno, facilitar la detección de conflictos y optimizar la gestión de dependencias en proyectos de Machine Learning y desarrollo en Python.

- [installed_packeges_log/pipdeptree_success.txt](installed_packeges_log/pipdeptree_success.txt)  
- [requirements.txt](requirements.txt)  

**Comandos ejecutados**

- ""

Disculpa la confusión, ¡tienes toda la razón! Mi error fue no ser lo suficientemente preciso.

Lo que se instala es la librería **`python-dotenv`**. La función `load_dotenv()` es una parte específica (y la más utilizada) de esa librería. Es como decir que instalaste Microsoft Office, y luego usas Word. No instalaste "Word" de forma independiente, instalaste el paquete Office que lo incluye.

## `load_dotenv` de `python-dotenv`

Se instaló la librería **`python-dotenv`** para facilitar la gestión segura de **variables de entorno** en el proyecto. Esta herramienta permite cargar configuraciones sensibles, como claves de API y contraseñas, desde un archivo dedicado llamado `.env`. Al no incluir este archivo en el control de versiones (como Git), se mantiene la seguridad de las credenciales, evitando que queden expuestas en el código fuente o en repositorios públicos.

La función principal de esta librería, **`load_dotenv()`**, es la que se encarga de leer el contenido del archivo `.env` y de inyectar esas variables en el entorno de ejecución del script de Python. Esto es crucial para el desarrollo colaborativo, ya que cada desarrollador puede tener su propia configuración local sin modificar el código base. Además, garantiza que el despliegue en entornos de producción sea más seguro y manejable, ya que las variables pueden ser gestionadas externamente al código.
