En este contexto, `upsert` es una operación utilizada en bases de datos y almacenes de vectores (como **ChromaDB**, **Pinecone**, **Weaviate**, o **FAISS** con almacenamiento adicional) que combina **update** (actualización) e **insert** (inserción).

### ¿Qué hace `upsert` en este script?
```python
collection.upsert(ids=ids, embeddings=embeddings, metadatas=metadatas)
```
Este comando inserta nuevos datos si los `ids` no existen en la colección o actualiza los registros si los `ids` ya existen. Es útil cuando trabajas con **almacenamiento de embeddings** para búsqueda semántica o recuperación de información en bases vectoriales.

### Parámetros:
1. **`ids`**: Lista de identificadores únicos de los embeddings (por ejemplo, `["doc1", "doc2", "doc3"]`).
2. **`embeddings`**: Lista de vectores numéricos que representan el contenido de los documentos (`[[0.1, 0.2, ...], [0.5, 0.6, ...]]`).
3. **`metadatas`**: Información adicional sobre los documentos (por ejemplo, `{ "title": "Documento 1", "page": 5 }`).

### Ejemplo práctico:
Si ejecutas esto por primera vez:
```python
collection.upsert(
    ids=["doc1", "doc2"],
    embeddings=[[0.1, 0.2, 0.3], [0.5, 0.6, 0.7]],
    metadatas=[{"title": "PDF1", "page": 1}, {"title": "PDF2", "page": 2}]
)
```
- Se insertan dos nuevos vectores (`doc1` y `doc2`).

Si vuelves a ejecutar con los mismos `ids` pero con nuevos embeddings:
```python
collection.upsert(
    ids=["doc1"],
    embeddings=[[0.9, 0.8, 0.7]],
    metadatas=[{"title": "PDF1", "page": 3}]
)
```
- **El `doc1` se actualiza** con un nuevo embedding y metadatos.
- `doc2` permanece sin cambios.

### ¿Por qué `upsert` es útil?
✅ **Evita duplicados**, ya que actualiza en lugar de insertar de nuevo.  
✅ **Optimiza el almacenamiento**, ya que no es necesario eliminar e insertar manualmente.  
✅ **Facilita actualizaciones automáticas** cuando los embeddings cambian.

### ¿Dónde se usa?
- **Búsqueda semántica** con bases vectoriales.
- **Almacenamiento de documentos** con embeddings en ChromaDB o Pinecone.
- **IA generativa** donde se necesitan bases de conocimiento actualizables.

Si estás construyendo un sistema de consulta sobre PDFs, esta operación te permite mantener la base de datos de embeddings siempre actualizada sin preocuparte por duplicaciones. 🚀

---

La diferencia principal entre `upsert` y `add` en este contexto radica en cómo manejan los datos en la colección de embeddings. Aquí te explico las diferencias clave:

---

## 1️⃣ **`collection.add(...)`**  
### 🔹 ¿Qué hace?
- **Inserta** nuevos documentos en la colección.
- **Falla si el `id` ya existe**, es decir, no permite sobrescribir datos existentes.

### 📌 Ejemplo:
```python
collection.add(
    ids=["doc1"],
    embeddings=[[0.1, 0.2, 0.3]],
    metadatas=[{"title": "PDF1", "page": 1}],
    documents=["Texto extraído de la página 1"]
)
```
- Se inserta un nuevo registro con el ID `"doc1"`.
- Si intentas volver a ejecutar la misma instrucción con el mismo ID, se generará un error.

### 🚨 Limitación:
❌ No se puede usar para **actualizar** un documento ya existente.  
❌ Si intentas agregar un ID repetido, puede fallar o duplicar registros (según la base vectorial utilizada).

---

## 2️⃣ **`collection.upsert(...)`**  
### 🔹 ¿Qué hace?
- **Inserta si el ID no existe**.
- **Actualiza si el ID ya existe** (sobreescribe el embedding, metadatos y documentos).

### 📌 Ejemplo:
```python
collection.upsert(
    ids=["doc1"],
    embeddings=[[0.9, 0.8, 0.7]],  # Nuevo embedding
    metadatas=[{"title": "PDF1", "page": 3}],  # Nueva página
    documents=["Nuevo contenido actualizado"]
)
```
- Si `"doc1"` **no existe**, se **inserta**.
- Si `"doc1"` **ya existe**, se **actualiza** con nuevos valores.

### ✅ Ventajas:
✔ Evita duplicados porque actualiza en lugar de insertar duplicados.  
✔ Es útil cuando quieres **mantener actualizada** tu base de embeddings sin preocuparte por eliminaciones manuales.  

---

## 🤔 **¿Cuál usar en tu sistema de PDFs?**
✅ **Si solo insertas nuevos datos sin preocuparte por actualizaciones**, usa `add()`.  
✅ **Si quieres actualizar documentos sin crear duplicados**, usa `upsert()`.  

Como tu sistema trabaja con búsqueda semántica y PDFs, lo más recomendable es usar **`upsert()`** para asegurarte de que si procesas un documento más de una vez, no termines con múltiples copias del mismo contenido en la base de datos. 🚀

