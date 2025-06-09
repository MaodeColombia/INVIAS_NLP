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
  
