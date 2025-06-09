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
