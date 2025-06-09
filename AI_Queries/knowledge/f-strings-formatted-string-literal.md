# f-strings en Python

## ¿Qué es `f"{...}"`?

Una **f-string** (formatted string literal) es una cadena literal que comienza con `f` o `F` antes de las comillas. Permite:

* **Interpolar variables y expresiones** directamente sin concatenaciones.
* **Evaluar** cualquier expresión de Python entre llaves `{}`.
* **Formatear** el resultado según el mini-lenguaje de formato de Python.

```python
nombre = "Ana"
edad   = 28
print(f"Hola, {nombre}. Tienes {edad} años.")  # → Hola, Ana. Tienes 28 años.
```



## Sintaxis general

```python
f"{ expresion [!conversion] [:formato] }"
```

1. **`expresion`**: cualquier expresión Python.
2. **`!conversion`** (opcional):

   * `!s` → `str()`
   * `!r` → `repr()`
   * `!a` → `ascii()`
3. **`:formato`** (opcional): especifica anchura, alineación, relleno, precisión y tipo (igual que en `str.format()`).



## Principales usos

1. **Interpolación de variables**
   Inserta valores sin `+` ni llamadas manuales a `str()`.

   ```python
   saludo = f"Bienvenido, {usuario}"
   ```

2. **Evaluación de expresiones**
   Permite cálculos en línea:

   ```python
   print(f"2 + 2 = {2 + 2}")
   ```

3. **Formato y presentación de datos**
   Control de ancho, precisión, separadores y bases numéricas:

   ```python
   precio = 1234.5
   print(f"Precio: {precio:,.2f}")    # → "Precio: 1,234.50"
   n = 255
   print(f"{n:#b}")                   # → "0b11111111"
   ```

4. **Alineación y relleno**

   | Alineación | Símbolo | Ejemplo                      |            |     |
   | ---------- | ------- | ---------------------------- | ---------- | --- |
   | Izquierda  | `<`     | \`f"                         | {text:<10} | "\` |
   | Derecha    | `>`     | \`f"                         | {text:>10} | "\` |
   | Centro     | `^`     | \`f"                         | {text:^10} | "\` |
   | Números    | `=`     | `f"{num:=+8}"` (signo antes) |            |     |

   Y relleno con cualquier carácter:

   ```python
   print(f"{42:0>5}")   # → "00042"
   print(f"{42:_^7}")   # → "__42__"
   ```

5. **Precisión y tipos**

   * Floats: `.2f`, `.4e`, `.3g`
   * Enteros: `d`, `b`, `x`, `o`
   * Porcentaje: `%`

   ```python
   pi = 3.14159
   print(f"{pi:.2f}")   # → "3.14"
   ```

6. **Depuración rápida**
   Desde Python 3.8, agrega `=` tras la expresión para mostrarla junto a su valor:

   ```python
   valor = 42
   print(f"{valor=}")   # → "valor=42"
   ```

7. **Cadenas multilínea**
   Funcionan en triples comillas, ideal para templates largos:

   ```python
   reporte = f"""
   Fecha: {hoy}
   Usuario: {usuario}
   """
   ```

## Ventajas clave

* **Legibilidad y concisión:** elimina concatenaciones tediosas.
* **Potencia:** evalúa expresiones completas en línea.
* **Flexibilidad:** un mini-lenguaje de formato unificado.

Las f-strings tienen aún más matices y posibilidades avanzadas. Estos son algunos temas que vale la pena explorar más allá de lo básico:

1. **Expresiones complejas y llamadas en línea**
   Puedes llamar funciones, métodos o usar expresiones más elaboradas dentro de las llaves.

   ```python
   import datetime
   ahora = datetime.datetime.now()
   print(f"Fecha y hora actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
   ```

2. **Especificadores dinámicos**
   El ancho, la precisión o incluso el tipo de conversión pueden provenir de variables:

   ```python
   ancho = 10
   texto = "OK"
   print(f"{texto:^{ancho}}")           # centrado según la variable
   prec = 3
   num = 3.14159
   print(f"{num:.{prec}f}")             # precisión dinámica
   ```

3. **Campos anidados y mapeo**
   Si formateas datos de un diccionario o atributo de objeto, puedes acceder directamente:

   ```python
   user = {"name": "Ana", "age": 28}
   print(f"{user[name]} tiene {user[age]} años.")
   class P:
       def __init__(self, x): self.x = x
       def __format__(self, spec): return f"<<{self.x}:{spec}>>"
   p = P(42)
   print(f"{p:x}")                      # invoca P.__format__('x')
   ```

4. **Prefijo combinado con raw strings**
   Con `rf"…"` o `fr"…"` evitas que se procesen escapes normales, pero sí las llaves f-string:

   ```python
   path = r"C:\temp"
   print(rf"Ruta: {path}\n" )           # \n como texto literal
   ```

5. **Depuración mejorada (`=` con formateo)**
   Desde Python 3.8 puedes añadir especificadores tras el `=`:

   ```python
   val = 123.456
   print(f"{val=:.1f}")                 # → "val=123.5"
   ```

6. **Limitaciones y buenas prácticas**

   * No puedes usar saltos de línea con barra invertida dentro de la expresión `{…}`.
   * Evita lógicas muy complejas en la cadena: si te ves metiendo muchas llamadas, mejor calcula antes y usa la f-string sólo para formatear.

7. **Rendimiento**
   Las f-strings son más rápidas que `str.format()` y concatenaciones, pero si generas plantillas muy grandes dinámicamente, compara con otras alternativas (p. ej., `Template` de `string`).

8. **Internacionalización y localización**
   Para formatos de números o fechas según locales, suele ser mejor usar el módulo `locale` o librerías específicas antes de insertar en la f-string.

---

Dentro de las llaves de una f-string solo puedes poner **expresiones** de Python, no sentencias (`for`/`while` como tal). Pero como las comprensiones (list, dict, generator…) son expresiones, puedes aprovecharlas para “iterar” y generar texto. Por ejemplo:

```python
# 1. List comprehension dentro de una f-string
frutas = ["manzana", "pera", "uva"]
print(f"Frutas disponibles: {[f*  for f in frutas]}")
# → Frutas disponibles: ['manzana', 'pera', 'uva']

# 2. Generator expression + join para producir un texto limpio
nums = range(1, 6)
print(f"Números: {', '.join(str(n) for n in nums)}")
# → Números: 1, 2, 3, 4, 5

# 3. Dict comprehension
cuadrados = {n: n*n for n in range(5)}
print(f"Cuadrados: {cuadrados}")
# → Cuadrados: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 4. Generador directo (imprime la representación del generador)
print(f"Generador: {((i, i*i) for i in range(3))}")
# → Generador: <generator object <genexpr> at 0x…>
```

Si lo que ves es algo como

```python
f"{x for x in iterable}"
```

eso en realidad produce un **generator object** (no una lista), porque `{…}` sin corchetes ni llaves de dict es un *generator expression*. Para obtener valores, habitualmente lo combinas con `join()`, `list()` u otra función que consuma el generador.

### Puntos clave

* **No hay for/while “puros”** dentro de `{}`; sólo expresiones.
* **Comprensiones** (`[... for …]`, `{… for …}`) y **generator expressions** (`(… for …)`) son expresiones válidas.
* Suelen combinarse con funciones como `join()`, `list()`, etc., para convertirlos en cadenas o colecciones concretas.

Con esto puedes “iterar” y formatear colecciones en una f-string de forma compacta y poderosa.

---

**Renombrado iterativo de PDFs con f-strings**  
En tu resumen puedes incluir este bloque con los pasos y ejemplos clave:

1. **Listar archivos PDF**

   ```python
   pdfs = [f for f in os.listdir(ruta) if f.lower().endswith(".pdf")]
   ```

2. **Generar nombres numéricos secuenciales**

   * Usa `enumerate` para obtener el índice:

     ```python
     for i, nombre in enumerate(pdfs, start=1):
         nuevo = f"documento_{i}.pdf"
         os.rename(os.path.join(ruta, nombre),
                   os.path.join(ruta, nuevo))
     ```

3. **Alinear con ceros (padding dinámico)**

   * Calcula el ancho necesario a partir del total:

     ```python
     ancho = len(str(len(pdfs)))
     for i, nombre in enumerate(pdfs, start=1):
         nuevo = f"documento_{i:0{ancho}d}.pdf"
         …  # renombrado
     ```

4. **Incluir fecha y parte del nombre original**

   * Combina `datetime.strftime`, `os.path.splitext` y f-strings:

     ```python
     hoy = datetime.now().strftime("%Y%m%d")
     for i, nombre in enumerate(pdfs, start=1):
         base, ext = os.path.splitext(nombre)
         nuevo = f"{hoy}_{base}_{i:02d}{ext}"
         …
     ```

5. **Listado sin renombrar**

   * Para previsualizar nombres nuevos:

     ```python
     nuevos = [f"documento_{i}.pdf" for i in range(1, len(pdfs)+1)]
     ```



> **Resumen:** Con f-strings integras lógica y formato en una sola línea, facilitando la generación automática de nombres claros y consistentes para tus PDFs.
