---
title: ChromaDB - Guía Completa de Uso, Servidor y Optimización
tags:
  - Chromadb
---

# ChromaDB

ChromaDB es una base de datos vectorial de código abierto diseñada para facilitar la construcción de aplicaciones de IA, especialmente aquellas que utilizan Modelos de Lenguaje Grandes (LLMs) y necesitan gestionar y buscar "embeddings" (representaciones numéricas de datos como texto, imágenes o audio).

## Paso a paso para usar ChromaDB

Aquí tienes un instructivo paso a paso para usar ChromaDB en Python:

### Paso 1: Instalación de ChromaDB

Lo primero es instalar la librería `chromadb` en tu entorno Python. Puedes hacerlo usando `pip`:

```bash
pip install chromadb
```

> Para usar ChromaDB en modo cliente/servidor (por ejemplo, con `chromadb.HttpClient`), o si simplemente deseas que tus datos persistan en disco y sean accesibles desde múltiples sesiones o aplicaciones, necesitas *iniciar* el servidor de ChromaDB. Este comando **`chromadb run --path ./chroma_db`** debe ejecutarse en la carpeta donde vayas a realizar tus pruebas o donde desees que se almacenen los datos de tu base de datos. Por ejemplo, si tu proyecto se llama `mi_proyecto` y dentro de él quieres que la base de datos se guarde en una subcarpeta `chroma_db`, ejecutarías el comando dentro de `mi_proyecto`.

### Paso 2: Crear un Cliente ChromaDB

Existen varias formas de *inicializar* un cliente de ChromaDB, dependiendo de *cómo quieras almacenar* tus datos:

1. **Cliente en memoria (EphemeralClient):** Ideal para pruebas rápidas y desarrollo, ya que los datos no se persisten después de que el programa termina.

   ```python
   import chromadb
   client = chromadb.Client()
   ```

2. **Cliente persistente (PersistentClient):** Si quieres que tus datos se guarden en disco y se carguen automáticamente cada vez que inicies tu aplicación, usa un cliente persistente. Debes especificar una ruta donde se almacenarán los archivos de la base de datos.

   ```python
   import chromadb

   # La ruta donde ChromaDB guardará sus archivos de base de datos
   client = chromadb.PersistentClient(path="/path/to/my/chroma_db_data")
   ```

   > **Nota sobre persistencia de la versión ChromaDB de LangChain:** Si estás utilizando LangChain y su integración con ChromaDB, el comportamiento de persistencia es ligeramente diferente y requiere llamar a `.persist()` explícitamente después de la creación. Para más detalles sobre cómo manejar la persistencia de la versión ChromaDB de LangChain, consulta el documento: [[v01-persistent_chromadb]].

3. **Cliente HTTP (para modo cliente/servidor):** Si estás ejecutando un servidor ChromaDB aparte (por ejemplo, en un Docker o en otro proceso), puedes conectarte a él usando el cliente HTTP.

   > Para usar ChromaDB en modo cliente/servidor, necesitas iniciar el servidor de ChromaDB. Este comando **`chromadb run --path ./chroma_db`** debe ejecutarse en la carpeta donde vayas a realizar tus pruebas o donde desees que se almacenen los datos de tu base de datos. Por ejemplo, si tu proyecto se llama `mi_proyecto` y dentro de él quieres que la base de datos se guarde en una subcarpeta `chroma_db`, ejecutarías el comando dentro de `mi_proyecto`.

   1. **Detalles del Servidor ChromaDB (`chromadb run --path ./chroma_db`):**

      Este comando tiene varios propósitos clave:

      - **Inicia el servidor de ChromaDB** en `http://localhost:8000`.
      - **Guarda los datos** de manera persistente en la carpeta `./chroma_db`
      - **Permite conectarte** desde cualquier otro programa o script usando `HttpClient`.

   2. **Cómo verificar que el servidor está funcionando:**

      Después de ejecutar el comando `chromadb run --path ./chroma_db`, puedes probar si ChromaDB está en marcha con:

      ```sh
      curl http://localhost:8000
      ```

      Si todo está bien, deberías recibir una respuesta del servidor.

   3. **Ejemplo de Conexión desde Python (al servidor HTTP):**

      Una vez que el servidor esté corriendo, puedes conectarte desde Python con:

      ```python
      import chromadb
      
      # Conectar a un servidor ChromaDB que se ejecuta en localhost:8000
      client = chromadb.HttpClient(host='localhost', port=8000)
      ```

### Paso 3: Crear una Colección

Las colecciones son como tablas en una base de datos relacional, son el lugar donde almacenarás tus documentos, sus embeddings y cualquier metadato asociado. Las colecciones indexan tus embeddings para permitir una recuperación y filtrado eficiente.

```python
# Crear una nueva colección llamada 'mi_coleccion'
collection = client.create_collection(name="mi_coleccion")

# O si quieres obtener una colección existente o crearla si no existe:
# collection = client.get_or_create_collection(name="mi_coleccion")
```

> Por defecto, ChromaDB utiliza el modelo de embedding "all-MiniLM-L6-v2" para convertir el texto en embeddings, pero puedes especificar un modelo diferente al crear la colección si lo necesitas.

### Paso 4: Añadir Documentos a la Colección

Puedes añadir documentos junto con sus IDs únicos y, opcionalmente, metadatos a la colección. ChromaDB se encargará de convertir automáticamente tu texto a embeddings si no los proporcionas.

```python
documents = [
    "Este es un documento sobre piñas.",
    "Este es un documento sobre naranjas.",
    "El sol es una estrella."
]
ids = ["doc1", "doc2", "doc3"]
metadatas = [
    {"categoria": "fruta", "fuente": "wikipedia"},
    {"categoria": "fruta", "fuente": "blog"},
    {"categoria": "astronomia", "fuente": "libro"}
]

collection.add(
    documents=documents,
    metadatas=metadatas, # Opcional
    ids=ids
)
```

### Paso 5: Consultar la Colección

Una vez que tus documentos están en la colección, puedes realizar búsquedas de similitud. Puedes consultar la colección con texto de consulta, y ChromaDB devolverá los `n` resultados más similares.

```python
# Realizar una consulta de similitud
results = collection.query(
    query_texts=["¿Qué frutas son cítricas?"], # ChromaDB creará el embedding para esta consulta
    n_results=2, # Cuántos resultados quieres que te devuelva
    where={"categoria": "fruta"} # Filtrar por metadatos (opcional)
)

print(results)
```
#### Filtrar los resultados basándose en los metadatos.

Para filtrar los resultados basándose en los metadatos al realizar una consulta en ChromaDB, utilizas el parámetro `where` dentro del método `collection.query()`. Este parámetro espera un diccionario que define las condiciones de filtrado.

##### Filtrado Básico (Igualdad)

Puedes filtrar para que solo se devuelvan los documentos donde un campo de metadato específico tenga un valor exacto.

**Ejemplo:** Si quieres encontrar documentos que tengan la `categoria` "fruta".

  

```python
# Suponiendo que 'collection' ya está definida y tiene documentos
# con metadatos como {"categoria": "fruta"}  

results = collection.query(
    query_texts=["¿Qué es una fruta?"],
    n_results=5,
    where={"categoria": "fruta"}  # Filtra donde 'categoria' sea exactamente 'fruta'
)

print(results)
```


##### Filtrado con Operadores Lógicos y de Comparación

ChromaDB soporta varios operadores lógicos y de comparación dentro del diccionario `where`, lo que te permite crear filtros más complejos. Los operadores se expresan como un diccionario anidado.

  * **Operadores de Comparación:** `$eq` (igual a), `$ne` (diferente de), `$gt` (mayor que), `$gte` (mayor o igual que), `$lt` (menor que), `$lte` (menor o igual que).

  * **Operadores de Pertenencia:** `$in` (está en una lista), `$nin` (no está en una lista).

  * **Operadores Lógicos:** `$and` (Y lógico), `$or` (O lógico).

###### Ejemplo con `$eq` (igual a) - es implícito si solo pones el valor directamente

```python

# Equivalente al ejemplo básico de arriba
results = collection.query(
    query_texts=["animales domésticos"],
    n_results=3,
    where={"tipo": {"$eq": "mamífero"}}
)
print(results)
```

###### Ejemplo con `$ne` (diferente de)

```python

# Documentos que NO son de la fuente "blog"
results = collection.query(
    query_texts=["información general"],
    n_results=5,
    where={"fuente": {"$ne": "blog"}}
)
print(results)

```

###### Ejemplo con `$gt` (mayor que) y `$lt` (menor que) - para valores numéricos

```python
# Documentos con un campo 'año' entre 2000 y 2010 (exclusivo)
results = collection.query(
    query_texts=["eventos históricos"],
    n_results=10,
    where={"año": {"$gt": 2000, "$lt": 2010}}
)
print(results)
```
###### Ejemplo con `$in` (está en una lista)

```python
# Documentos cuya categoría es "noticias" o "deporte"
results = collection.query(
    query_texts=["eventos actuales"],
    n_results=5,
    where={"categoria": {"$in": ["noticias", "deporte"]}}
)
print(results)
```

###### Ejemplo con `$and` (Y lógico)

Para `$and`, simplemente colocas múltiples condiciones en el mismo diccionario `where`.

```python
# Documentos que son de 'categoria' "fruta" Y 'fuente' "wikipedia"

results = collection.query(
    query_texts=["algo sobre frutas"],
    n_results=3,
    where={"categoria": "fruta", "fuente": "wikipedia"}
)
print(results)

# O explícitamente con $and para mayor claridad o para combinar con otros operadores:

results = collection.query(
    query_texts=["algo sobre frutas"],
    n_results=3,
    where={"$and": [{"categoria": "fruta"}, {"fuente": "wikipedia"}]}
)
print(results)
```

###### Ejemplo con `$or` (O lógico)

```python
# Documentos que son de 'categoria' "fruta" O 'categoria' "vegetal"
results = collection.query(
    query_texts=["plantas comestibles"],
    n_results=5,
    where={"$or": [{"categoria": "fruta"}, {"categoria": "vegetal"}]}
)
print(results)
```

##### Consideraciones

  * **Tipos de datos:** Asegúrate de que los valores en tus metadatos coincidan con el tipo de dato que estás usando en el filtro (ej. números para `$gt`, `$lt`).

  * **Case sensitivity:** Los filtros de cadena son generalmente *case-sensitive*. "Fruta" no es lo mismo que "fruta".

  * **[[usage_chromadb_IndexacionMetadatos_y_Optimizacion|Indexación de metadatos]]**: Para un rendimiento óptimo en filtros complejos sobre metadatos muy grandes, es posible que desees consultar la documentación de ChromaDB sobre cómo manejan la indexación de metadatos o si hay formas de optimizar esto.

#### Listado de Operaciones Comunes en ChromaDB

- **Crear un Cliente:**
  - `chromadb.Client()`: Cliente en memoria (datos no persistentes).
  - `chromadb.PersistentClient(path="/ruta/a/mi/chroma_db_data")`: Cliente persistente (los datos se guardan en disco).
  - `chromadb.HttpClient(host='localhost', port=8000)`: Cliente para conectar a un servidor ChromaDB remoto.

- **Gestionar Colecciones:**
  - `client.create_collection(name="nombre_coleccion")`: Crea una nueva colección.
  - `client.get_collection(name="nombre_coleccion")`: Obtiene una colección existente.
  - `client.get_or_create_collection(name="nombre_coleccion")`: Obtiene una colección si existe, o la crea si no.
  - `client.delete_collection(name="nombre_coleccion")`: Elimina una colección existente.

- **Añadir y Gestionar Documentos:**
  - `collection.add(documents=..., metadatas=..., ids=...)`: Añade nuevos documentos, sus metadatos opcionales y sus IDs únicos a la colección. ChromaDB puede convertir el texto a embeddings automáticamente.

  - `collection.upsert(documents=..., metadatas=..., ids=...)`: Actualiza un documento si el ID ya existe, o lo inserta si no.

    ```python
    collection.upsert(
        documents=["Este es el documento uno actualizado."],
        ids=["doc1"]
    )
    ```

  - `collection.get(ids=...)`: Obtiene documentos específicos por sus IDs.

      ```python
      doc = collection.get(ids=["doc1"])
      print(doc)
      ```

  - `collection.count()`: Devuelve el número total de documentos en la colección.

      ```python
      count = collection.count()
      print(f"Número de documentos en la colección: {count}")
      ```

  - `collection.delete(ids=...)` o `collection.delete(where=...)`: Elimina documentos por ID o por una condición de metadatos.

      ```python
      # Eliminar por ID
      collection.delete(ids=["doc2"])
      # Eliminar por condición
      # collection.delete(where={"categoria": "astronomia"})
      ```

- **Consultar Colecciones (Búsqueda de Similitud):**
  - `collection.query(query_texts=..., n_results=..., where=..., where_document=...)`: Realiza una búsqueda de similitud. Puedes especificar textos de consulta (ChromaDB los embebe), el número de resultados deseado y aplicar filtros de metadatos (`where`) o filtros sobre el contenido del documento (`where_document`).

