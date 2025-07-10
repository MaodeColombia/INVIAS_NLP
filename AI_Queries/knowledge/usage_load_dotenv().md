---
title: Uso del package load_dotenv() para guardar la OPENAI_API_KEY
---

# Uso del package load_dotenv() para guardar la OPENAI_API_KEY

## Explíqueme load_dotenv()

En pocas palabras, `load_dotenv()` **carga variables de configuración** desde un archivo de texto llamado **`.env`** y las hace disponibles para tu script de Python como si fueran **variables de entorno del sistema**.

Es una de las **mejores prácticas** para manejar "secretos" (como claves de API, contraseñas de bases de datos, etc.) sin tener que escribirlos directamente en tu código.

### ¿Cómo Funciona? (Ejemplo Práctico)

Imagina que tienes esta estructura de archivos en tu proyecto:

```plaintext
INVIAS_NLP/
├── .env
├── .gitignore
└── ingest_documents.py
```

#### Paso 1: Crear el archivo `.env`

Este es un simple archivo de texto donde defines tus variables sensibles. Cada línea es una variable.

**Archivo:** `.env`

```plaintext
# Este es un comentario. Las líneas en blanco y los comentarios se ignoran.
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
DATABASE_USER="admin_invias"
```

#### Paso 2: Usarlo en tu script de Python

En tu script `ingest_documents.py`, primero debes instalar la librería: `pip install python-dotenv`.

Luego, el código se ve así:

**Archivo:** `ingest_documents.py`

```python
import os
from dotenv import load_dotenv

# 1. LLAMAR A load_dotenv()
# Esto busca un archivo .env en el directorio actual (o superiores)
# y carga las variables que encuentre en el entorno del sistema.
load_dotenv()

# 2. ACCEDER A LAS VARIABLES
# Ahora puedes acceder a las variables como si las hubieras configurado
# manualmente en tu sistema operativo, usando la librería `os`.
api_key = os.environ.get("OPENAI_API_KEY")
db_user = os.environ.get("DATABASE_USER")

# Verificación para asegurarnos de que funcionó
if api_key:
    print("¡Clave de API de OpenAI cargada con éxito!")
    # print(f"La clave empieza con: {api_key[:5]}...") # Descomentar para depurar
else:
    print("Error: No se encontró la OPENAI_API_KEY. Asegúrate de que esté en tu archivo .env.")

if db_user:
    print(f"Usuario de la base de datos: {db_user}")
```

#### Paso 3: Proteger tus secretos con `.gitignore`

El paso más importante para la seguridad es asegurarte de que tu archivo `.env` **NUNCA** se suba a un repositorio de código como GitHub. Para ello, simplemente añades `.env` a tu archivo `.gitignore`.

**Archivo:** `.gitignore`

```plaintext
# Ignorar el archivo con las variables de entorno
.env

# Otras carpetas y archivos a ignorar
__pycache__/
chroma_db/
*.pyc
```

### ¿Por qué es tan importante?

- **Seguridad**: Evita que tus claves de API y contraseñas queden expuestas en tu código fuente. Si tu código es público, cualquiera podría robarlas.

- **Flexibilidad**: Diferentes personas de tu equipo pueden tener diferentes claves o configuraciones (desarrollo vs. producción) en sus propios archivos `.env` sin tener que modificar el código.

- **Organización**: Centraliza toda la configuración sensible de tu aplicación en un solo lugar, fácil de encontrar y modificar.

En resumen, `load_dotenv()` es una herramienta simple pero poderosa que te ayuda a escribir código más **seguro, flexible y profesional**. En tu proyecto, la estás usando de la manera correcta para gestionar tu `OPENAI_API_KEY`.

## ¿`load_dotenv()` crea variables de entorno permanentes?

La respuesta corta es: **No**, `load_dotenv()` no crea una variable de entorno **permanente** en tu sistema operativo (como las que configuras en el panel de control de Windows).

Lo que hace es algo más sutil e inteligente:

`load_dotenv()` carga las variables del archivo `.env` en el **entorno de ejecución únicamente para el script de Python que se está ejecutando en ese momento.**

Déjame desglosarlo:

- **Tu Sistema Operativo (Windows)**: Tiene su propio conjunto de **variables de entorno globales**. Cuando dices "actualmente tengo la apikey en las variables de entorno", te refieres a estas. Son persistentes y están disponibles para cualquier programa que inicies.

- **Tu Script de Python**: Cuando ejecutas `python mi_script.py`, el script recibe una **copia** de las variables de entorno de tu sistema en ese instante.

- **La Magia de `load_dotenv()`**: Al llamar a `load_dotenv()` al inicio de tu script, la librería:

  - Busca y lee el archivo `.env`.

  - Añade las variables que encuentra en `.env` a la **copia** del entorno que tiene tu script.

### ¿Qué pasa si la variable ya existe en el sistema?

Aquí viene la parte más importante para tu caso: **Por defecto, `load_dotenv()` NO sobrescribirá una variable de entorno que ya exista en el sistema.**

Esto significa que tu configuración actual es **perfecta y segura**.

- Cuando `os.environ.get("OPENAI_API_KEY")` se ejecute, primero encontrará la variable que ya tienes configurada en Windows y la usará.

- El valor que puedas tener en tu archivo `.env` para `OPENAI_API_KEY` será ignorado.

Esto es una gran ventaja. Permite que el archivo `.env` sirva como una configuración por defecto o para otros desarrolladores que clonen tu proyecto, pero te permite a ti (y a los servidores de producción) usar variables del sistema, que son más seguras.

### Ejemplo para ilustrarlo

Imagina este código:

**Archivo:** `.env`

```plaintext
# Esta es la clave del archivo .env
OPENAI_API_KEY="key-desde-el-archivo-dotenv"
```

**Archivo:** `test_env.py`

```python
import os
from dotenv import load_dotenv

print("Antes de load_dotenv():")
print(f'  La clave es: {os.environ.get("OPENAI_API_KEY")}')

# Cargamos las variables del archivo .env
load_dotenv()

print("\nDespués de load_dotenv():")
print(f'  La clave es: {os.environ.get("OPENAI_API_KEY")}')
```

Cómo se comportaría:

- **Caso 1: NO tienes la variable en Windows.**

  Salida:

  ```plaintext
  Antes de load_dotenv():
    La clave es: None
  
  Después de load_dotenv():
    La clave es: key-desde-el-archivo-dotenv
  ```

- **Caso 2: SÍ tienes la variable en Windows (ej: `set OPENAI_API_KEY="key-real-del-sistema"`).**

  Salida:

  ```plaintext
  Antes de load_dotenv():
    La clave es: key-real-del-sistema
  
  Después de load_dotenv():
    La clave es: key-real-del-sistema
  ```

  Como puedes ver, la variable del sistema tiene prioridad y `load_dotenv()` no la sobrescribe.

En resumen: Estás usando la herramienta exactamente como fue diseñada. Tu variable de entorno del sistema está segura y el `.env` sirve como un excelente respaldo o configuración para desarrollo.

## Cuál serian las ventajas de una o de de la otra opción?

Es fundamental entender las ventajas de cada método para decidir cuál usar en diferentes situaciones. Ambas opciones son válidas, pero sirven para propósitos ligeramente distintos. A continuación, te explico las ventajas de cada una:

### Opción 1: Variables de Entorno del Sistema (Tu Método Actual)

Este método consiste en configurar la variable directamente en tu sistema operativo (por ejemplo, en el "Panel de Control > Sistema > Configuración avanzada del sistema > Variables de entorno..." de Windows).

#### Ventajas

- **Máxima Seguridad**: Esta es la forma más segura. La clave de API no se almacena en ningún archivo de texto dentro de tu proyecto. Esto elimina casi por completo el riesgo de que la subas accidentalmente a un repositorio público como GitHub.

- **Estándar para Producción**: En entornos de producción (servidores reales donde correrá tu aplicación), esta es la práctica estándar. Las claves se "inyectan" en el entorno del servidor, no se guardan en archivos.

- **Disponibilidad Global**: La variable está disponible para cualquier programa o script que ejecutes en tu computadora, no solo para este proyecto de Python.

### Opción 2: Archivo `.env` y la Librería `python-dotenv`

Este método consiste en crear un archivo de texto llamado `.env` en la raíz de tu proyecto y cargar las variables desde allí con `load_dotenv()`.

#### Ventajas

- **Ideal para Desarrollo y Colaboración**: Es extremadamente práctico para trabajar en equipo. Un nuevo desarrollador puede clonar el proyecto, crear su propio archivo `.env` (a partir de un archivo de ejemplo como `.env.example`) y empezar a trabajar de inmediato sin tener que configurar su sistema operativo.

- **Portabilidad y Organización**: Toda la configuración necesaria para el proyecto vive dentro de la carpeta del proyecto. Esto lo hace autocontenido y fácil de mover o compartir.

- **Facilidad de Gestión**: Es mucho más rápido y sencillo editar un archivo de texto que navegar por los menús del sistema operativo para cambiar una variable.

### Conclusión y la Mejor Práctica (¡La que ya usas!)

| Característica         | Variables del Sistema | Archivo `.env`                      |
| :--------------------- | :-------------------- | :---------------------------------- |
| Seguridad              | 🏆 **Más alta** | Buena (si `.env` está en `.gitignore`) |
| Facilidad (Desarrollo) | Regular               | 🏆 **Excelente** |
| Portabilidad (Equipo)  | Baja                  | 🏆 **Excelente** |
| Estándar de Producción | 🏆 **Sí** | No, se prefiere el del sistema      |

La mejor solución, y la que de hecho estás implementando, es un **enfoque híbrido**:

- **Para ti y para producción**: Usa las **variables de entorno del sistema**. Son más seguras.
- **En el código**: Usa `load_dotenv()` de todas formas.

#### ¿Por qué esta combinación es tan buena?

Porque `load_dotenv()` por defecto **no sobrescribe** una variable que ya existe en el sistema. Esto te da lo mejor de ambos mundos:

- Tu script usará tu clave segura del sistema operativo.
- Si otro desarrollador clona tu proyecto, puede crear su propio archivo `.env` y el mismo código funcionará para él sin problemas.

Así que, en resumen, tu configuración actual es **robusta** y sigue las **mejores prácticas** de la industria.
