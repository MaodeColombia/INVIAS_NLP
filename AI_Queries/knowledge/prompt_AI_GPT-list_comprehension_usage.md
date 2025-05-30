### **📌 Lista por Comprensión (`list comprehension`) en Python**
Una **lista por comprensión** es una forma concisa y eficiente de crear listas en Python. Es más rápida y legible que usar un bucle `for` tradicional.

---

## **1️⃣ Sintaxis Básica**
La sintaxis de una **lista por comprensión** es:

```python
nueva_lista = [expresión for elemento in iterable if condición]
```

🔹 **`expresión`** → Lo que queremos añadir a la nueva lista.  
🔹 **`elemento`** → Cada elemento en la secuencia (`iterable`).  
🔹 **`iterable`** → La colección sobre la que iteramos (`list`, `tuple`, `range()`, `str`, etc.).  
🔹 **`if condición`** (opcional) → Un filtro que determina qué elementos se incluyen.  

---

## **2️⃣ Ejemplo Básico: Crear una Lista con un `for` Normal**
Sin lista por comprensión:

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = []  # Lista vacía

for n in numeros:
    cuadrados.append(n ** 2)  # Agrega cada número elevado al cuadrado

print(cuadrados)
```
🔹 **Salida:**
```python
[1, 4, 9, 16, 25]
```

**Con lista por comprensión:**
```python
cuadrados = [n ** 2 for n in numeros]
print(cuadrados)
```
🔹 **Salida:**
```python
[1, 4, 9, 16, 25]
```
✅ **Ventaja**: Se logra en una sola línea sin necesidad de usar `append()`.

---

## **3️⃣ Lista con un `if` (Filtrar Elementos)**
Si queremos **solo los números pares**, podemos agregar un `if`:

```python
pares = [n for n in numeros if n % 2 == 0]
print(pares)
```
🔹 **Salida:**
```python
[2, 4]
```
📌 **Explicación:**
- Iteramos `n` en `numeros`.
- Si `n % 2 == 0` (es par), lo agregamos a la lista `pares`.

---

## **4️⃣ Lista con `if...else`**
Podemos usar `if...else` dentro de la **expresión** (antes del `for`):

```python
par_o_impar = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(par_o_impar)
```
🔹 **Salida:**
```python
['impar', 'par', 'impar', 'par', 'impar']
```

📌 **Diferencia con el ejemplo anterior:**
- Aquí **transformamos los elementos** en `"par"` o `"impar"`, en lugar de solo filtrarlos.

---

## **5️⃣ Lista con `for` Anidados (Matrices)**
Podemos usar listas por comprensión para recorrer **listas dentro de listas** (matrices):

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattener = [num for fila in matriz for num in fila]  # Aplana la matriz
print(flattener)
```
🔹 **Salida:**
```python
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
📌 **Explicación:**
- Recorremos cada `fila` en la `matriz`.
- Luego recorremos cada `num` en esa `fila`, agregándolos a una nueva lista.

---

## **6️⃣ Uso en Filtrado de Archivos (Ejemplo con `os.listdir`)**
Ahora volvemos a tu código original:

```python
import os

carpeta = "mis_documentos"
archivos_pdf = [archivo for archivo in os.listdir(carpeta) if archivo.endswith(".pdf")]

print(f"\nSe encontraron {len(archivos_pdf)} archivos PDF en la carpeta '{carpeta}'.")
```

🔹 **¿Qué hace este código?**
1. **`os.listdir(carpeta)`** obtiene la lista de todos los archivos en la carpeta.
2. **`archivo for archivo in os.listdir(carpeta)`** recorre cada archivo en la lista.
3. **`if archivo.endswith(".pdf")`** filtra solo los que terminan en `.pdf`.
4. **La lista final `archivos_pdf` contiene solo los archivos PDF encontrados.**

Ejemplo:  
Si `os.listdir(carpeta)` devuelve:
```python
["documento.pdf", "imagen.jpg", "factura.pdf", "notas.txt"]
```
El resultado en `archivos_pdf` será:
```python
["documento.pdf", "factura.pdf"]
```

📌 **Comparación con un `for` tradicional:**
```python
archivos_pdf = []
for archivo in os.listdir(carpeta):
    if archivo.endswith(".pdf"):
        archivos_pdf.append(archivo)
```
✅ **Mismo resultado, pero más líneas de código**.

---

## **7️⃣ Otras Aplicaciones de Lista por Comprensión**
📌 **Transformar cadenas a mayúsculas:**
```python
palabras = ["hola", "mundo", "python"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # ['HOLA', 'MUNDO', 'PYTHON']
```

📌 **Extraer las primeras letras de una lista de palabras:**
```python
iniciales = [palabra[0] for palabra in palabras]
print(iniciales)  # ['h', 'm', 'p']
```

📌 **Generar una lista de tuplas `(n, n²)`:**
```python
pares_numeros = [(n, n**2) for n in range(1, 6)]
print(pares_numeros)  # [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

---

## **8️⃣ Ventajas de las Listas por Comprensión**
✅ **Código más corto y limpio**.  
✅ **Mejor rendimiento** que un `for` tradicional con `append()`.  
✅ **Expresión única**, en lugar de varias líneas de código.  
✅ **Fácil de leer cuando se usa correctamente**.

⚠️ **Precaución:** No abusar de listas por comprensión anidadas, ya que pueden hacer que el código sea más difícil de entender.

---

## **🚀 Conclusión**
Las **listas por comprensión (`list comprehension`)** son una herramienta poderosa en Python que permite **crear listas de manera concisa y eficiente**. Son ideales para **filtrar, transformar y generar listas** sin necesidad de estructuras `for` largas.

Ahora, con este conocimiento, puedes escribir código más compacto y legible, especialmente cuando trabajas con listas y archivos. 🚀