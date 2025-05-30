En Python, las variables pueden contener datos de diversos **tipos**, los cuales determinan cómo se almacenan y manipulan. Estos tipos se agrupan en **tipos básicos** y **tipos compuestos**. A continuación, detallo los principales tipos de variables en Python:

---

## **1. Tipos básicos**

### **a. Numéricos**
1. **`int` (Enteros)**: Números enteros, positivos o negativos, sin parte decimal.
   - Ejemplo:
     ```python
     x = 42  # Entero
     y = -15  # Entero negativo
     ```

2. **`float` (Flotantes)**: Números con parte decimal.
   - Ejemplo:
     ```python
     pi = 3.14159
     negativo = -7.2
     ```

3. **`complex` (Complejos)**: Números en formato complejo con parte real e imaginaria.
   - Ejemplo:
     ```python
     z = 3 + 4j  # Parte real: 3, Parte imaginaria: 4
     ```

---

### **b. Cadenas de texto**
1. **`str` (String o cadenas)**: Secuencias de caracteres, representadas entre comillas simples o dobles.
   - Ejemplo:
     ```python
     nombre = "Python"
     saludo = 'Hola, ¿cómo estás?'
     ```

---

### **c. Booleanos**
1. **`bool` (Booleanos)**: Valores de verdad: `True` (Verdadero) o `False` (Falso).
   - Ejemplo:
     ```python
     es_activo = True
     es_mayor = 10 > 5  # True
     ```

---

### **d. Binarios**
1. **`bytes`**: Secuencia inmutable de valores en formato binario.
   - Ejemplo:
     ```python
     data = b"Hola mundo"
     ```

2. **`bytearray`**: Secuencia mutable de valores en formato binario.
   - Ejemplo:
     ```python
     mutable_data = bytearray(b"Hola")
     mutable_data[0] = 72  # Cambiar el primer byte
     ```

3. **`memoryview`**: Permite acceder y modificar datos binarios sin copiarlos.
   - Ejemplo:
     ```python
     mem = memoryview(b"Hola mundo")
     print(mem[0])  # Muestra 72 (el valor ASCII de 'H')
     ```

---

## **2. Tipos compuestos**

### **a. Listas**
1. **`list`**: Secuencia mutable y ordenada de elementos.
   - Ejemplo:
     ```python
     numeros = [1, 2, 3, 4]
     frutas = ["manzana", "pera", "naranja"]
     numeros[0] = 10  # Cambiar el primer elemento
     ```

---

### **b. Tuplas**
1. **`tuple`**: Secuencia inmutable y ordenada de elementos.
   - Ejemplo:
     ```python
     coordenadas = (10, 20)
     ```

---

### **c. Conjuntos**
1. **`set`**: Colección no ordenada de elementos únicos.
   - Ejemplo:
     ```python
     conjunto = {1, 2, 3, 3}  # Resultado: {1, 2, 3}
     ```

2. **`frozenset`**: Conjunto inmutable.
   - Ejemplo:
     ```python
     fs = frozenset([1, 2, 3])
     ```

---

### **d. Diccionarios**
1. **`dict`**: Colección mutable de pares clave-valor.
   - Ejemplo:
     ```python
     persona = {"nombre": "Juan", "edad": 30}
     print(persona["nombre"])  # "Juan"
     ```

---

## **3. Tipos especiales**

### **a. `NoneType`**
1. **`None`**: Representa la ausencia de valor o un valor nulo.
   - Ejemplo:
     ```python
     resultado = None
     ```

---

## **4. Tipos avanzados**

1. **`range`**: Representa un rango de números.
   - Ejemplo:
     ```python
     r = range(5)  # Números del 0 al 4
     ```

2. **`callable`**: Representa funciones o métodos invocables.
   - Ejemplo:
     ```python
     def funcion():
         return "Hola"
     print(callable(funcion))  # True
     ```

3. **`type`**: Representa el tipo de una variable.
   - Ejemplo:
     ```python
     print(type(42))  # <class 'int'>
     ```

---

## **Conversión de tipos**

Python permite convertir variables de un tipo a otro mediante funciones integradas:
- `int()`: Convertir a entero.
- `float()`: Convertir a flotante.
- `str()`: Convertir a cadena.
- `list()`: Convertir a lista.
- `tuple()`: Convertir a tupla.
- `set()`: Convertir a conjunto.

#### Ejemplo:
```python
numero = "123"
entero = int(numero)  # Convierte la cadena a entero
flotante = float(entero)  # Convierte el entero a flotante
cadena = str(flotante)  # Convierte el flotante a cadena
```

---

### **Resumen visual**
| Tipo           | Ejemplo               | Mutable |
|----------------|-----------------------|---------|
| `int`          | `42`                 | No      |
| `float`        | `3.14`               | No      |
| `complex`      | `1+2j`               | No      |
| `bool`         | `True`               | No      |
| `str`          | `"texto"`            | No      |
| `list`         | `[1, 2, 3]`          | Sí      |
| `tuple`        | `(1, 2, 3)`          | No      |
| `set`          | `{1, 2, 3}`          | Sí      |
| `dict`         | `{"key": "value"}`   | Sí      |
| `NoneType`     | `None`               | N/A     |

Estos tipos son la base para cualquier operación en Python, y su flexibilidad permite escribir código más dinámico y eficiente.