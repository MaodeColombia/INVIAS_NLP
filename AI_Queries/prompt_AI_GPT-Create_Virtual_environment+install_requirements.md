

# **Cómo crear un entorno virtual**

### Actualizar `pip`

- Simplemente ejecuta el siguiente comando en tu terminal:

  ```sh
  python -m pip install --upgrade pip
  ```

- Después de la actualización, verifica la versión instalada con:

  ```sh
  pip --version
  ```


### Crear entorno virtual  

- Crea el entorno virtual en `C:\Users\mmartinezo\.virtualenvs`:

  ```sh 
  python -m venv C:/Users/mmartinezo/.virtualenvs/NLP_Congreso
  ```

  Esto creará un entorno virtual en `C:/Users/mmartinezo/.virtualenvs/NLP_Congreso`.


### Activar el entorno virtual  

- En Git Bash o PowerShell:
  ```sh
  source C:/Users/mmartinezo/.virtualenvs/NLP_Congreso/Scripts/activate
  ```


### Instalar las dependencias del proyecto

- **Asegúrate de estar en la raíz del repositorio** y luego instala los paquetes:
   ```sh
   pip install -r requirements.txt
   ```


### Verificar que todo está correctamente instalado

- **Lista los paquetes instalados**:
  ```sh
  pip list
  ```

- **Confirma que estás en el entorno correcto**:
  ```sh
  where python
  ```

   📌 **Debería mostrar** algo como:
   ```
   C:\Users\mmartinezo\.virtualenvs\TU_REPOSITORIO_ENV\Scripts\python.exe
   C:\Users\mmartinezo\AppData\Local\Programs\Python\Python312\python.exe
   ```