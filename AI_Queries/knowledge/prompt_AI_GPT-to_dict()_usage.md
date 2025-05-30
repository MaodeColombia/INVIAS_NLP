Aquí tienes ejemplos de todas las opciones de `.to_dict()` en Pandas, aplicadas a un **DataFrame de ejemplo**:

---

## **📌 DataFrame de Ejemplo**
```python
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    "name": ["documento1.pdf", "documento2.pdf"],
    "page_1": [3, 7]
}

df = pd.DataFrame(data)
print(df)
```

📋 **Salida del DataFrame (`df`)**
```
            name  page_1
0  documento1.pdf      3
1  documento2.pdf      7
```

---

## **🔹 1. `.to_dict("records")` → Lista de diccionarios (Filas como diccionarios)**
```python
df.to_dict("records")
```
📋 **Salida**
```python
[
    {"name": "documento1.pdf", "page_1": 3},
    {"name": "documento2.pdf", "page_1": 7}
]
```
✅ **Explicación**:  
Cada fila se convierte en un diccionario, donde las claves son los nombres de las columnas.

---

## **🔹 2. `.to_dict("dict")` → Diccionario de columnas**
```python
df.to_dict("dict")
```
📋 **Salida**
```python
{
    "name": {0: "documento1.pdf", 1: "documento2.pdf"},
    "page_1": {0: 3, 1: 7}
}
```
✅ **Explicación**:  
Cada clave representa una columna, y los valores son diccionarios con los índices como claves.

---

## **🔹 3. `.to_dict("list")` → Diccionario de listas**
```python
df.to_dict("list")
```
📋 **Salida**
```python
{
    "name": ["documento1.pdf", "documento2.pdf"],
    "page_1": [3, 7]
}
```
✅ **Explicación**:  
Cada clave representa una columna, y los valores son listas con los datos de cada fila.

---

## **🔹 4. `.to_dict("series")` → Diccionario de Series de Pandas**
```python
df.to_dict("series")
```
📋 **Salida**
```python
{
    "name": 
        0    documento1.pdf
        1    documento2.pdf
        Name: name, dtype: object,
        
    "page_1": 
        0    3
        1    7
        Name: page_1, dtype: int64
}
```
✅ **Explicación**:  
Cada clave es una columna, y los valores son **Series de Pandas**.

---

## **🔹 5. `.to_dict("split")` → Diccionario con estructura indexada**
```python
df.to_dict("split")
```
📋 **Salida**
```python
{
    "index": [0, 1],
    "columns": ["name", "page_1"],
    "data": [
        ["documento1.pdf", 3],
        ["documento2.pdf", 7]
    ]
}
```
✅ **Explicación**:  
Este formato organiza los datos en tres partes:
- `"index"`: Índices del DataFrame.
- `"columns"`: Nombres de las columnas.
- `"data"`: Listas de valores fila por fila.

---

## **🔹 6. `.to_dict("index")` → Diccionario de filas (Indexado por ID)**
```python
df.to_dict("index")
```
📋 **Salida**
```python
{
    0: {"name": "documento1.pdf", "page_1": 3},
    1: {"name": "documento2.pdf", "page_1": 7}
}
```
✅ **Explicación**:  
Cada clave representa un índice del DataFrame, y el valor es un diccionario con los datos de esa fila.

---

## **🔹 7. `.to_dict("tight")` → Diccionario compacto**
```python
df.to_dict("tight")
```
📋 **Salida**
```python
{
    "index": [0, 1],
    "columns": ["name", "page_1"],
    "data": [
        ["documento1.pdf", 3],
        ["documento2.pdf", 7]
    ]
}
```
✅ **Explicación**:  
Similar a `"split"`, pero más compacto, ya que no almacena los nombres de las columnas en cada fila.

---

## **📌 Resumen Comparativo**
| Opción         | Estructura del Resultado |
|---------------|------------------------|
| **"records"** | Lista de diccionarios, cada fila es un diccionario |
| **"dict"**    | Diccionario con columnas como claves y valores como diccionarios |
| **"list"**    | Diccionario con columnas como claves y listas como valores |
| **"series"**  | Diccionario con columnas como claves y valores como Series de Pandas |
| **"split"**   | Diccionario con `index`, `columns` y `data` separados |
| **"index"**   | Diccionario con índices como claves y valores como diccionarios (filas) |
| **"tight"**   | Diccionario compacto similar a `"split"` |

---

## 🚀 **¿Cuál Elegir Según el Caso de Uso?**
✔ **Para Bases de Datos y APIs** → `"records"` (JSON estructurado)  
✔ **Para Procesamiento en Pandas** → `"dict"` o `"list"`  
✔ **Para Exportación Compacta** → `"split"` o `"tight"`  
✔ **Para Indexación** → `"index"`  

---

**¿Necesitas más ejemplos personalizados? ¡Dime en qué contexto lo usarás y te ayudo! 🚀**