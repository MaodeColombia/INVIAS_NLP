### Extensión: Manejo de errores en funciones con `try-except` en Python

El bloque `try-except` es una de las herramientas más importantes en Python para el manejo de errores. Su objetivo principal es garantizar que el programa no se detenga abruptamente en caso de que ocurra un error, permitiendo gestionar esas situaciones de forma controlada.

Vamos a profundizar en los aspectos clave del ejemplo que compartiste y en cómo puedes aplicarlos a otros contextos:

---

### 1. **El propósito de `try`**
   - El bloque `try` encapsula el código que puede generar un error.
   - Si no ocurre ningún error, el programa ejecuta el código normalmente.
   - Si ocurre un error en cualquier línea dentro del bloque `try`, el control salta inmediatamente al bloque `except`, omitiendo el resto del código dentro del `try`.

#### Ejemplo:
```python
try:
    result = 10 / 0  # Esto generará un error
    print("Esta línea no se ejecutará")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
```

En este caso, el programa detecta un `ZeroDivisionError` y ejecuta el bloque `except` correspondiente.

---

### 2. **El bloque `except`**
   - El bloque `except` define qué hacer cuando ocurre un error.
   - Puedes capturar errores específicos o todos los errores (usando la clase base `Exception`).
   - Es una buena práctica manejar errores específicos para tener un control más fino.

#### Capturar errores específicos:
```python
try:
    value = int("abc")  # Esto genera un ValueError
except ValueError:
    print("Error: No se pudo convertir la cadena a un entero")
```

#### Capturar todos los errores:
```python
try:
    result = 10 / 0
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
```

Cuando usas `Exception`, capturas cualquier error. Sin embargo, esto debe usarse con precaución, ya que puede ocultar errores inesperados.

---

### 3. **`else` en `try-except`**
   - Python permite agregar un bloque `else` que se ejecuta si no ocurre ningún error en el bloque `try`.
   - Útil para separar el código que debe ejecutarse solo si todo sale bien.

#### Ejemplo:
```python
try:
    num = int(input("Ingresa un número: "))
except ValueError:
    print("Error: Debes ingresar un número válido")
else:
    print(f"El número ingresado es {num}")
```

---

### 4. **`finally`: Limpieza de recursos**
   - El bloque `finally` se ejecuta siempre, sin importar si ocurrió o no un error.
   - Es útil para liberar recursos, como cerrar archivos o conexiones de red.

#### Ejemplo con `finally`:
```python
try:
    file = open("archivo.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: El archivo no existe")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("Archivo cerrado correctamente")
```

---

### 5. **Ventajas del manejo de errores**
   - **Estabilidad**: Evita que el programa se detenga abruptamente.
   - **Legibilidad**: Organiza el manejo de errores en un solo lugar.
   - **Control**: Permite actuar en función del error (mostrar mensajes, reintentar operaciones, etc.).
   - **Limpieza**: Ayuda a liberar recursos, como archivos o conexiones.

---

### 6. **Aplicación del manejo de errores en funciones**
   En el ejemplo original, se utiliza `try-except` en una función. Veamos cómo estructurar una función con manejo de errores y una descripción general del flujo:

#### Estructura de la función:
```python
def process_pdf(pdf_path):
    try:
        # Intentar abrir y procesar el archivo
        document = fitz.open(pdf_path)
        metadata = document.metadata
        return metadata
    except FileNotFoundError:
        print(f"Error: El archivo '{pdf_path}' no se encontró")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        # Liberar recursos si es necesario
        if 'document' in locals() and not document.is_closed:
            document.close()
```

---

### 7. **Mejoras y buenas prácticas**
   - **Específicos sobre generales**: Captura errores específicos antes de usar `Exception`.
   - **Registros detallados**: Usa una herramienta como `logging` en lugar de `print` para registrar errores.
   - **Validaciones previas**: Antes de abrir archivos, verifica su existencia con `os.path.exists()`.
   - **Reintentos**: Implementa lógica para reintentar operaciones críticas si fallan.
   - **Documentación**: Incluye comentarios claros sobre qué hace cada bloque.

#### Ejemplo con mejoras:
```python
import logging
import os

logging.basicConfig(level=logging.ERROR)

def process_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        logging.error(f"Archivo no encontrado: {pdf_path}")
        return None

    try:
        document = fitz.open(pdf_path)
        metadata = document.metadata
        return metadata
    except Exception as e:
        logging.error(f"Error procesando el archivo PDF: {e}")
        return None
    finally:
        if 'document' in locals() and not document.is_closed:
            document.close()
```

Este ejemplo incorpora validaciones previas, uso de `logging`, y el cierre seguro del archivo.

---

En resumen, el manejo de errores es esencial para hacer que los programas sean robustos, fáciles de depurar y seguros. Usar estructuras como `try-except-else-finally` te permitirá manejar cualquier problema que pueda surgir sin interrumpir la ejecución del programa.