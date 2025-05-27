# ChromaDB como base de datos persistente


## 🧠 Comportamiento por defecto de `Chroma.from_documents(...)`

Cuando usas:

```python
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings
)
```

### 📌 Por defecto:

* \*\*Crea una base de datos vectorial **en memoria (RAM) solamente**, no en disco.
* No guarda nada en archivos permanentes a menos que tú se lo indiques explícitamente.

---

## ✅ Solución: crear base de datos Chroma **persistente**

Para que puedas ver y conservar la base de datos, necesitas:

### 1. Crear un **directorio persistente**

```python
persist_directory = "chroma_db"
```

### 2. Usar `Chroma.from_documents` con `persist_directory`

```python
from langchain.vectorstores import Chroma

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=persist_directory
)
```

### 3. Llamar a `.persist()` después

```python
vectorstore.persist()
```

---

## 📁 Resultado

Esto crea una carpeta llamada `chroma_db/` con archivos como:

```
chroma_db/
├── chroma-collections.parquet
├── chroma-embeddings.parquet
├── index/
│   └── ... (archivos internos de la base de datos)
```

✅ ¡Esta es tu base vectorial ya lista y reutilizable!

---

## 🧪 ¿Y luego cómo la vuelves a cargar?

En otra sesión puedes hacer:

```python
vectorstore = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_db"
)
```

---

¿Quieres que te prepare el bloque de código completo para dejar esto persistente, listo para indexar y usar el retriever?
