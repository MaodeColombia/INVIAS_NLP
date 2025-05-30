En Python, los **tipos de salida (return type)** indican qué tipo de dato devuelve una función. Esto se define con anotaciones de tipo usando `->`.

---

### Tipos de salida en Python y ejemplos

#### 1. Booleano (`-> bool`)
```python
def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

print(es_mayor_de_edad(20))  # True
```

#### 2. Número entero (`-> int`)
```python
def suma(a: int, b: int) -> int:
    return a + b

print(suma(5, 3))  # 8
```

#### 3. Número decimal (`-> float`)
```python
def calcular_area_circulo(radio: float) -> float:
    return 3.1416 * radio ** 2

print(calcular_area_circulo(5))  # 78.54
```

#### 4. Cadena de texto (`-> str`)
```python
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}!"

print(saludar("Juan"))  # "Hola, Juan!"
```

#### 5. Listas (`-> list`)
```python
def obtener_numeros_pares(n: int) -> list[int]:
    return [i for i in range(n) if i % 2 == 0]

print(obtener_numeros_pares(10))  # [0, 2, 4, 6, 8]
```

#### 6. Tuplas (`-> tuple`)
```python
def obtener_coordenadas() -> tuple[float, float]:
    return (40.7128, -74.0060)

print(obtener_coordenadas())  # (40.7128, -74.0060)
```

#### 7. Diccionarios (`-> dict`)
```python
def obtener_estudiante() -> dict[str, int]:
    return {"Juan": 25, "Maria": 22}

print(obtener_estudiante())  # {'Juan': 25, 'Maria': 22}
```

#### 8. Conjuntos (`-> set`)
```python
def obtener_vocales() -> set[str]:
    return {"a", "e", "i", "o", "u"}

print(obtener_vocales())  # {'a', 'e', 'i', 'o', 'u'}
```

#### 9. None (`-> None`)
```python
def log_mensaje(mensaje: str) -> None:
    print(f"Log: {mensaje}")

log_mensaje("Esto es un mensaje")  # Log: Esto es un mensaje
```

#### 10. Tipos Personalizados (Clases)
```python
class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

def crear_persona(nombre: str, edad: int) -> Persona:
    return Persona(nombre, edad)

persona = crear_persona("Ana", 30)
print(persona.nombre, persona.edad)  # Ana 30
```

#### 11. Unión de tipos (`-> Union`)
```python
from typing import Union

def convertir_a_numero(valor: str) -> Union[int, float]:
    return int(valor) if valor.isdigit() else float(valor)

print(convertir_a_numero("10"))   # 10 (int)
print(convertir_a_numero("10.5")) # 10.5 (float)
```

#### 12. Callable (`-> Callable`)
```python
from typing import Callable

def obtener_operacion() -> Callable[[int, int], int]:
    def suma(a: int, b: int) -> int:
        return a + b
    return suma

operacion = obtener_operacion()
print(operacion(3, 4))  # 7
```

---

### Resumen

| Tipo de Dato  | Ejemplo |
|--------------|--------------------------------|
| `bool` | `-> bool` (`True` o `False`) |
| `int` | `-> int` (Números enteros) |
| `float` | `-> float` (Números decimales) |
| `str` | `-> str` (Cadenas de texto) |
| `list` | `-> list[int]` (Listas de números enteros) |
| `tuple` | `-> tuple[str, int]` (Tuplas con tipos definidos) |
| `dict` | `-> dict[str, int]` (Diccionario con clave `str` y valor `int`) |
| `set` | `-> set[str]` (Conjunto de cadenas) |
| `None` | `-> None` (No devuelve nada) |
| `Union` | `-> Union[int, float]` (Puede ser `int` o `float`) |
| `Callable` | `-> Callable[[int, int], int]` (Devuelve una función) |
| `Clase` | `-> Persona` (Devuelve un objeto de la clase `Persona`) |

Si necesitas más detalles o ejemplos personalizados, dime qué caso específico te interesa.