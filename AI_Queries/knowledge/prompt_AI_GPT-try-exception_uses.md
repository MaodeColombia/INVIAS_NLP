# ¿Qué es `try-except` en Python?

El bloque `try-except` es una de las herramientas más importantes en Python para el manejo de errores. Su objetivo principal es garantizar que el programa no se detenga abruptamente en caso de que ocurra un error, permitiendo gestionar esas situaciones de forma controlada.

## El propósito de `try`

- El bloque `try` encapsula el código que puede generar un error.  
- Si no ocurre ningún error, el programa ejecuta el código normalmente.  
- Si ocurre un error en cualquier línea dentro del bloque `try`, el control salta inmediatamente al bloque `except`, omitiendo el resto del código dentro del `try`.

## Estructura completa de `try`

```python
try:
    # Código que puede generar una excepción
except TipoDeExcepcion:
    # Código que se ejecuta si ocurre ese tipo de excepción
else:
    # Código que se ejecuta solo si NO ocurre ninguna excepción
finally:
    # Código que se ejecuta SIEMPRE, haya o no error
```

### Descripción de cada bloque

#### 🔹 `try`

- Aquí va el **código que se quiere intentar ejecutar**.
- Si todo funciona bien, el bloque `except` se **omite**.

```python
try:
    resultado = 10 / 0
```

#### 🔹 `except`

- Se ejecuta **solo si ocurre una excepción** dentro del bloque `try`.
- Puedes capturar tipos específicos de error (`ZeroDivisionError`, `FileNotFoundError`, etc.) o usar un `except Exception as e:` para capturar cualquier error.

```python
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
```

#### 🔹 `else` (opcional)

- Se ejecuta **si NO hubo errores** en el bloque `try`.
- Útil para separar el código "normal" del manejo de errores.

```python
else:
    print("División exitosa:", resultado)
```

#### 🔹 `finally` (opcional pero muy útil)

- Se ejecuta **siempre**, haya o no error.
- Ideal para **cerrar archivos, conexiones o liberar recursos**.

```python
finally:
    print("Finalizando operación.")
```

### Ejemplo completo:

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
else:
    print("Archivo leído correctamente.")
finally:
    if 'archivo' in locals():
        archivo.close()
        print("Archivo cerrado.")
```

## **El bloque `except`**

- El bloque `except` define qué hacer cuando ocurre un error.
- Puedes capturar errores específicos o todos los errores (usando la clase base `Exception`).
- Es una buena práctica manejar errores específicos para tener un control más fino.

### Capturar todos los errores:

```python
try:
    result = 10 / 0
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
```

Cuando usas `Exception`, capturas cualquier error. Sin embargo, esto debe usarse con precaución, ya que puede ocultar errores inesperados.

### Capturar errores específicos:

```python
try:
    value = int("abc")  # Esto genera un ValueError
except ValueError:
    print("Error: No se pudo convertir la cadena a un entero")
```

En Python, los errores (excepciones) se representan como clases. Hay **muchos tipos de excepciones**. A continuación se presenta la **lista estructurada de los errores más comunes y relevantes**, agrupados por categoría.

#### 1. **Errores de sintaxis y construcción**

| Excepción          | Descripción                                    |
| ------------------ | ---------------------------------------------- |
| `SyntaxError`      | Código mal escrito (ej. falta un paréntesis)   |
| `IndentationError` | Mala indentación (espacios o tabs incorrectos) |
| `TabError`         | Mezcla incorrecta de tabs y espacios           |

#### 2. **Errores de tipo de datos**

| Excepción           | Descripción                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `TypeError`         | Uso incorrecto de tipos (ej. sumar `int` + `str`)                     |
| `ValueError`        | Tipo correcto pero **valor inválido** (ej. convertir `"abc"` a `int`) |
| `IndexError`        | Índice fuera de rango en listas o tuplas                              |
| `KeyError`          | Clave no encontrada en un diccionario                                 |
| `AttributeError`    | Atributo no existe para un objeto                                     |
| `NameError`         | Variable no definida                                                  |
| `UnboundLocalError` | Uso de variable local antes de asignarla                              |

#### 3. **Errores de entrada/salida y archivos**

| Excepción                      | Descripción                                    |
| ------------------------------ | ---------------------------------------------- |
| `FileNotFoundError`            | Archivo no encontrado                          |
| `IOError` (alias de `OSError`) | Problema general de entrada/salida             |
| `IsADirectoryError`            | Se esperaba un archivo pero se dio una carpeta |
| `NotADirectoryError`           | Se esperaba una carpeta pero se dio un archivo |
| `PermissionError`              | No se tienen permisos para acceder al recurso  |

#### 4. **Errores matemáticos**

| Excepción            | Descripción                                                    |
| -------------------- | -------------------------------------------------------------- |
| `ZeroDivisionError`  | División por cero                                              |
| `OverflowError`      | Resultado numérico demasiado grande                            |
| `FloatingPointError` | Error de precisión con `float` (raro, pero puede configurarse) |

#### 5. **Errores de importación y módulos**

| Excepción             | Descripción                              |
| --------------------- | ---------------------------------------- |
| `ImportError`         | Error al importar un módulo              |
| `ModuleNotFoundError` | El módulo no existe o no está disponible |

#### 6. **Errores relacionados con iteración**

| Excepción            | Descripción                                            |
| -------------------- | ------------------------------------------------------ |
| `StopIteration`      | Se terminó una iteración (usado internamente en `for`) |
| `StopAsyncIteration` | Versión asincrónica del anterior                       |

#### 7. **Errores de memoria y sistema**

| Excepción           | Descripción                                                 |
| ------------------- | ----------------------------------------------------------- |
| `MemoryError`       | No hay suficiente memoria RAM disponible                    |
| `RecursionError`    | Se excedió el número máximo de llamadas recursivas          |
| `SystemExit`        | Señal de finalización del programa (usado por `sys.exit()`) |
| `KeyboardInterrupt` | Interrupción con Ctrl+C                                     |
| `OSError`           | Error general del sistema operativo (archivo, red, etc.)    |

#### 8. **Errores personalizados**

Puedes crear tus propias excepciones:

```python
class MiErrorPersonalizado(Exception):
    pass
```

## **Ventajas del manejo de errores**

- **Estabilidad**: Evita que el programa se detenga abruptamente.
- **Legibilidad**: Organiza el manejo de errores en un solo lugar.
- **Control**: Permite actuar en función del error (mostrar mensajes, reintentar operaciones, etc.).
- **Limpieza**: Ayuda a liberar recursos, como archivos o conexiones.

## **Aplicación del manejo de errores en funciones**

En el ejemplo original, se utiliza `try-except` en una función. Veamos cómo estructurar una función con manejo de errores y una descripción general del flujo:

### Estructura de la función:

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

## **Mejoras y buenas prácticas**

- **Específicos sobre generales**: Captura errores específicos antes de usar `Exception`.

- **Registros detallados**: Usa una herramienta como `logging` en lugar de `print` para registrar errores.

- **Validaciones previas**: Antes de abrir archivos, verifica su existencia con `os.path.exists()`.

- **Reintentos**: Implementa lógica para reintentar operaciones críticas si fallan.

- **Documentación**: Incluye comentarios claros sobre qué hace cada bloque.

### Ejemplo con mejoras:

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

En resumen, el manejo de errores es esencial para hacer que los programas sean robustos, fáciles de depurar y seguros. Usar estructuras como `try-except-else-finally` te permitirá manejar cualquier problema que pueda surgir sin interrumpir la ejecución del programa.
