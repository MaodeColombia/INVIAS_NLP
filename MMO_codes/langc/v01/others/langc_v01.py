# %% [markdown]
# # LangChain para INVIAS

# %% [markdown]
# ## 🔒 1. Instalación de librerías

# %% [markdown]
# ### 🔓  Solo ejecutar este script si no se han instalado los paquetes para desarrollar el código

# %%
""" 
Lista de los paquetes a instalar:

    upgrade:
        pip
        setuptools
        wheel
    Packages:
        langchain 
        pypdf 
        openai 
        chromadb 
        tiktoken
        langchain-community
"""
import subprocess

comandos = [
    ["pip", "install", "--upgrade", "pip", "setuptools", "wheel"],
    ["pip", "install", "langchain", "pypdf", "openai", "chromadb", "tiktoken"],
    ["pip", "install", "-U", "langchain-community"],
    ["python", "-m", "pip", "install", "--upgrade", "pip"]
]

log_path = "instalacion_log.txt"

with open(log_path, "w", encoding="utf-8") as log_file:
    for i, cmd in enumerate(comandos, start=1):
        log_file.write(f"\n🔧 Ejecutando comando {i}: {' '.join(cmd)}\n")
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        log_file.write("✅ STDOUT:\n")
        log_file.write(result.stdout + "\n")
        
        if result.stderr:
            log_file.write("⚠️ STDERR:\n")
            log_file.write(result.stderr + "\n")

print(f"✅ Resultado guardado en {log_path}")


# %% [markdown]
# ## 2. Configuración de API Key de OpenAI

# %%
import os
from openai import OpenAI
# Recuperar la clave API de la variable de entorno
api_key_environ = os.environ.get("OPENAI_API_KEY")
 
# Verificar que la clave API esté disponible
if not api_key_environ:
    raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada o está vacía.")
 
# Inicializar el cliente de OpenAI con la clave API
client = OpenAI(api_key=api_key_environ)
 
# Usar el cliente para tus tareas
print("¡Cliente de OpenAI inicializado correctamente!")

# %% [markdown]
# ## 🔒 3. Carga de documents

# %% [markdown]
# ### 🔓  Solo ejecutar este script si no se ha hecho el proceso de embedding

# %%
import requests
from langchain.document_loaders import PyPDFLoader
import os

relative_pdf_path = "../../../assets/DG_docs/PDF_test_gradio/"

ml_papers = []

for i, file_name in enumerate(os.listdir(relative_pdf_path)):
    if file_name.lower().endswith(".pdf"):
        full_pdf_path = os.path.join(relative_pdf_path,file_name)
        print(f"📄 Cargando {file_name}")

        loader = PyPDFLoader(full_pdf_path)
        data = loader.load() # AI_Queries\code_explanation\ai_query-langc_v01-PyPDFLoader(filename).loader.load()_usage.md
        ml_papers.extend(data) # AI_Queries\code_explanation\ai_query-langc_v01-.extend_usage.md
        # print (ml_papers) # AI_Queries/code_explanation/ai_query-langc_v01-list_start_end_usage.md
# Utiliza la lista ml_papers para acceder a los elementos de todos los documentos descargados
print('Esto es todo el contenido de `ml_papers:`')
print(f"""
🆗 Todos los documentos estan cargados en ml_papers.
➖ Total de fragmentos: {len(ml_papers)}
➖ Los fragmentos son cada una de las hojas de cada uno de los {len(os.listdir(relative_pdf_path))} archivos en la carpeta {relative_pdf_path}
➖ Este script se ejecuta desde {os.getcwd()}
➖ Este es el contenido de la última hoja cargada {ml_papers[-1]}
""")

# %% [markdown]
# ## 🔒 4. Split de documents

# %% [markdown]
# ### 🔓
# 
# Solo ejecutar este script para desarrollar el proceso de embedding; este script depende del script anterior 

# %%
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500, 
    # AI_Queries\code_explanation\ai_query-langc_v01-chunk_usage.md 
    # AI_Queries\code_explanation\ai_query-langc_v01-max_tokens_Chatgptmodels.md 
    # AI_Queries\code_explanation\ai_query-langc_v01-meaning_inputpromptandanswer.md 
    # AI_Queries\code_explanation\ai_query-langc_v01-retrieval_meaning.md
    
    chunk_overlap=200,
    length_function=len
    )

documents = text_splitter.split_documents(ml_papers)

# %%
len(documents), documents[0]

# %% [markdown]
# ## 🔒 5. Embeddings e ingesta a base de datos vectorial 
# 
# ⚠️ advertencia de uso de esta sección ⚠️

# %% [markdown]
# ### 🔓 5.1.
# 
# Solo ejecutar este script para desarrolla el proceso de embedding; este script depende del script anterior
# 
# **Aquí se consume recurso de la API de OpenAI**

# %%
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# AI_Queries\code_explanation\ai_query-langc_v01-Embeddings_and_Vector_Store_Ingestion.md

# 1. Crear embeddings con el modelo oficial de OpenAI
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002") # ⚠️ cambiar a "text-embedding-3-small"

# 2. Definir carpeta para almacenar la base de datos vectorial
persist_directory = "chroma_db" #

# 3. Crear la base desde documentos y embeddings
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory=persist_directory
)

# 4. Guardar la base en disco
vectorstore.persist()
print("✅ Base de datos Chroma guardada en:", persist_directory)


# 5. Cargar la base vectorial guardada en disco
vectorstore = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_db"
)

# 6. Usar como retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
    )

# %% [markdown]
# ### 5.2.
# 
# Fue necesario crear copia de las lineas "*# 1. Crear embeddings con el modelo oficial de OpenAI*", "*# 5. Cargar la base vectorial guardada en disco*" y "*# 6. Usar como retriever*" para **solamente hacer uso de la Based de Datos de embeddings `chroma_db` ya creada y evitar recalcularla**.

# %%
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# 1. Modelo de embeddings (debe ser el mismo usado al crear la base)
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")  # ⚠️ cambiar a "text-embedding-3-small"

# 5. Cargar la base vectorial guardada en disco
vectorstore = Chroma(
    embedding_function=embeddings,
    persist_directory="chroma_db"
)

# 6. Usar como retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)

# %% [markdown]
# ## 6. Modelos de chat y cadenas para consulta de información

# %% [markdown]
# ### 🚩 6.1. Recuperación sin trazabilidad – Primer acercamiento con LangChain; ~~No cita las fuentes de donde extrae la información~~.

# %%
#AI_Queries/code_explanation/ai_query-langc_v01-Chat_Models_and_Retrieval_Chains_for_Information_Querying.md

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

chat = ChatOpenAI(
    openai_api_key=api_key_environ,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

# AI_Queries/code_explanation/ai_query-langc_v01-RetrievalQA.from_chain_type_usage.md
qa_chain = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=retriever
)

# %%
# AI_Queries/code_explanation/ai_query-langc_v01-qa_chain.run()_usage.md

query = "qué es CCPT?"
qa_chain.run(query)

# %% [markdown]
# 🧠 Comparación entre Script 1 y Script 2
# 
# | Aspecto                           | **Script anterior**                                 | **Script siguiente**                                                       |
# | --------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------- |
# | **Importación del modelo**        | `from langchain.chat_models` (obsoleto)             | `from langchain_openai` (recomendado)                                      |
# | **Versión del API**               | Antiguo LangChain monolítico                        | Nuevo ecosistema modular `langchain-openai`                                |
# | **Método de ejecución**           | `qa_chain.run(query)` (⚠️ obsoleto)                 | `qa_chain.invoke({"query": query})` (✅ recomendado)                        |
# | **Fuentes del resultado**         | ❌ No devuelve los documentos fuente                 | ✅ Incluye los documentos fuente con `return_source_documents=True`         |
# | **Retorno estructurado**          | Sólo devuelve texto plano                           | Devuelve un diccionario con respuesta y `source_documents`                 |
# | **Transparencia institucional**   | Baja (no se puede verificar origen de la respuesta) | Alta (permite validar en qué parte de los documentos se basa la respuesta) |
# | **Uso pedagógico recomendado**    | Para introducir conceptos básicos de `RetrievalQA`  | Para enseñar buenas prácticas actuales en trazabilidad y uso del LLM       |
# | **Estabilidad futura del código** | Baja (usa módulos y métodos deprecados)             | Alta (adaptado a la versión estable y mantenida de LangChain)              |

# %% [markdown]
# ### (🚩Revisar por qué no está gerendo resultados🚩) 6.2. Con recuperación básica – El sistema responde y cita fuentes

# %%
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# Inicializa el modelo de lenguaje
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.0,
    openai_api_key=api_key_environ
)

# Crear la cadena de preguntas y respuestas con fuentes
qa_chain = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True  # ✅ Para obtener las fuentes
)

# %%
query = " que pasa en Ocaña?"
result = qa_chain.invoke({"query": query})

# Imprimir respuesta
print("🧠 Respuesta:")
print(result['result'])

# Imprimir fuentes
print("\n📚 Fuentes:")
for i, doc in enumerate(result['source_documents']):
    print(f"\nFuente {i+1}:")
    print("Archivo:", doc.metadata.get("source", "desconocido"))
    print("Contenido:", doc.page_content[:400])  # Muestra primeros 400 caracteres


# %% [markdown]
# 🧠 Comparación entre Script 1 y Script 2
# 
# | Aspecto                           | **Script anterior**                                 | **Script actual**                                                       |
# | --------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------- |
# | **Importación del modelo**        | `from langchain.chat_models` (obsoleto)             | `from langchain_openai` (recomendado)                                      |
# | **Versión del API**               | Antiguo LangChain monolítico                        | Nuevo ecosistema modular `langchain-openai`                                |
# | **Método de ejecución**           | `qa_chain.run(query)` (⚠️ obsoleto)                 | `qa_chain.invoke({"query": query})` (✅ recomendado)                        |
# | **Fuentes del resultado**         | ❌ No devuelve los documentos fuente                 | ✅ Incluye los documentos fuente con `return_source_documents=True`         |
# | **Retorno estructurado**          | Sólo devuelve texto plano                           | Devuelve un diccionario con respuesta y `source_documents`                 |
# | **Transparencia institucional**   | Baja (no se puede verificar origen de la respuesta) | Alta (permite validar en qué parte de los documentos se basa la respuesta) |
# | **Uso pedagógico recomendado**    | Para introducir conceptos básicos de `RetrievalQA`  | Para enseñar buenas prácticas actuales en trazabilidad y uso del LLM       |
# | **Estabilidad futura del código** | Baja (usa módulos y métodos deprecados)             | Alta (adaptado a la versión estable y mantenida de LangChain)              |

# %% [markdown]
# 🧠 Diferencias clave entre ambos scripts
# 
# | Característica       | Script con `create_retrieval_chain` (moderno, script siguiente)            | Script con `RetrievalQA.from_chain_type` (clásico, script anterior) |
# | -------------------- | -------------------------------------------------------- | -------------------------------------------------- |
# | API utilizada        | Moderna (modular, flexible)                              | Clásica (más sencilla, menos control)              |
# | Cadena usada         | `create_retrieval_chain` + `combine_docs_chain`          | `RetrievalQA.from_chain_type`                      |
# | Prompt               | Totalmente personalizado con `PromptTemplate`            | Interno, no configurable por defecto               |
# | Control de flujo     | Separación clara de pasos (`retriever`, `prompt`, `LLM`) | Todo en una sola línea                             |
# | Adaptabilidad futura | Alta (recomendado en versiones recientes)                | Limitada (deprecated en versiones nuevas)          |
# 

# %% [markdown]
# ### 6.3. Con recuperación moderna – El sistema responde y muestra fuentes

# %%
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import ChatOpenAI

# 1. LLM moderno
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0, api_key=api_key_environ)

# 2. Prompt simple para combinar documentos
prompt = PromptTemplate.from_template(
    "Usa los siguientes documentos para responder la pregunta.\n\n{context}\n\nPregunta: {input}"
)

# 3. Cadena para combinar documentos (tipo "stuff")
combine_docs_chain = create_stuff_documents_chain(
    llm=llm,
    prompt=prompt
)

# 4. Cadena de recuperación completa con el retriever
qa_chain = create_retrieval_chain(
    retriever=retriever,
    combine_docs_chain=combine_docs_chain
)


# %%
response = qa_chain.invoke({"input": "aeropuerto del amazonas"})

print("🧠 Respuesta:")
print(response["answer"])

print("\n📚 Documentos usados:")
for i, doc in enumerate(response["context"]):
    print(f"\nFuente {i+1}:", doc.metadata.get("source", "desconocido"))
    print(doc.page_content[:300])


# %% [markdown]
# 🧠 Diferencias clave entre ambos scripts
# 
# | Característica       | Script con `create_retrieval_chain` (moderno)            | Script con `RetrievalQA.from_chain_type` (clásico) |
# | -------------------- | -------------------------------------------------------- | -------------------------------------------------- |
# | API utilizada        | Moderna (modular, flexible)                              | Clásica (más sencilla, menos control)              |
# | Cadena usada         | `create_retrieval_chain` + `combine_docs_chain`          | `RetrievalQA.from_chain_type`                      |
# | Prompt               | Totalmente personalizado con `PromptTemplate`            | Interno, no configurable por defecto               |
# | Control de flujo     | Separación clara de pasos (`retriever`, `prompt`, `LLM`) | Todo en una sola línea                             |
# | Adaptabilidad futura | Alta (recomendado en versiones recientes)                | Limitada (deprecated en versiones nuevas)          |
# 

# %% [markdown]
# #### 6.3.1 Gradio para seccion 6.3.

# %%
import gradio as gr

# Función para manejar la entrada y salida de QA Chain
def ask_question(question: str):
    # Invoca la cadena con la pregunta del usuario
    response = qa_chain.invoke({"input": question})
    # Extrae la respuesta
    answer = response.get("answer", "")
    # Construye la lista de fuentes y fragmentos
    context_snippets = []
    for i, doc in enumerate(response.get("context", [])):
        source = doc.metadata.get("source", "desconocido")
        snippet = doc.page_content[:300].replace("\n", " ")  # primeras 300 chars
        context_snippets.append(f"Fuente {i+1}: {source}\n{snippet}")
    context_text = "\n\n".join(context_snippets)
    return answer, context_text

# Definición de la interfaz de Gradio
iface = gr.Interface(
    fn=ask_question,
    inputs=gr.Textbox(lines=2, placeholder="Ingrese su pregunta aquí…"),
    outputs=[
        gr.Textbox(lines=5, label="Respuesta"),
        gr.Textbox(lines=20,label="Documentos usados")
    ],
    title="Interfaz QA con LangChain",
    description="Ingrese una consulta y obtenga la respuesta junto con las fuentes utilizadas."
)

# Lanzar la aplicación (en local o con share=True para exponerla)
iface.launch()
#iface.launch(share=True)


# %% [markdown]
# ### 6.4. Con memoria – El sistema conserva el contexto

# %%
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(temperature=0),
    retriever=vectorstore.as_retriever(),
    memory=memory
)

# Simulación de una conversación con contexto
chat_history = []

# Primera pregunta
response_1 = qa_chain({"question": "¿Qué entidad está a cargo del contrato de la vía Ocaña-Cúcuta?"})
print("Respuesta 1:", response_1['answer'])

# Segunda pregunta que se apoya en la anterior
response_2 = qa_chain({"question": "¿Cuál es el plazo de entrega del contrato?"})
print("Respuesta 2:", response_2['answer'])
# Aquí, la segunda pregunta sí aprovecha el contexto anterior, gracias a la memoria.

# %% [markdown]
# ## 7. LangChain para INVIAS
# 

# %% [markdown]
# ### 7.1. Descripción del código

# %% [markdown]
# El archivo `langc_v01.ipynb` es un **notebook de Jupyter** diseñado para mostrar paso a paso cómo construir un **sistema de consulta de información basado en documentos PDF usando LangChain y modelos de lenguaje de OpenAI**. 
# 
# #### Propósito del archivo `langc_v01.ipynb`
# 
# Implementar un **chatbot inteligente** que pueda:
# 
# 1. **Leer documentos PDF** institucionales.
# 2. **Convertirlos en embeddings semánticos** usando OpenAI.
# 3. **Almacenarlos en una base vectorial persistente** (Chroma).
# 4. **Responder preguntas** formuladas en lenguaje natural usando LLMs.
# 
# #### Estructura del notebook
# 
# 1. **Carga y lectura de documentos PDF**
# 
#    * Usa loaders como `PyPDFLoader`.
#    * Fragmenta el contenido en chunks con metadatos.
#    * Prepara los datos para el embedding.
# 
# 2. **Generación de embeddings y base vectorial**
# 
#    * Usa `OpenAIEmbeddings` (`text-embedding-ada-002`).
#    * Crea y guarda una base en Chroma (`chroma_db`).
#    * Permite que la búsqueda de contexto sea semántica, no solo por palabras clave.
# 
# 3. **Creación del `retriever`**
# 
#    * Define cuántos documentos relevantes recuperar (`k=3` o `k=5`).
#    * Es el núcleo del sistema RAG (Retrieval-Augmented Generation).
# 
# 4. **Construcción de la cadena de QA (`RetrievalQA`)**
# 
#    * Conecta el `retriever` con un modelo de lenguaje (`ChatOpenAI`).
#    * Puede configurarse para devolver solo la respuesta, o también las fuentes.
# 
# 5. **Ejecución de consultas**
# 
#    * Envía preguntas como `"¿Qué es CCPT?"` o `"¿Qué acciones tomó el INVÍAS en El Tarrita?"`.
#    * El sistema responde basándose en los documentos cargados.
# 
# > Este codigo viene de [langc_v01.ipynb](../../../Platzi_codes/langc/v01/langc_v01.ipynb). Este código desarrollo tiene [Code Explanation](../../../AI_Queries/code_explanation/).  

# %% [markdown]
# ### 7.2. Test del código

# %% [markdown]
# - [QA_01.md](others/QA_01.md)
# - [QA_02.md](others/QA_02.md)
# - [QA_03.md](others/QA_03.md)

# %% [markdown]
# ### 7.3. Hallazgos 🚩

# %% [markdown]
# 1. No cita las fuentes de donde extrae la información.
# 2. Solo para una pregunta. Si uso LangChain con un `ConversationalRetrievalChain`, se puede hacer varias preguntas en la misma sesión
# 3. Sin memoria – Cada pregunta se responde de forma aislada


