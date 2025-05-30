# Curso de Langchain (langc) - video 01

## [Desarrollo del archivo langc_v01.ipynb](../../Platzi_codes/langc/v01/langc_v01.ipynb)

- ![Sección "Carga de documents"](../../assets/images/langc_v01-seccion_carga_documents.png)

  - [Funcionamiento del `for` combinado con el `enumerate` en langc_v01.ipynb](../AI_Queries/code_explanation/ai_query-langc_v01-for_usage.md)
    - Message Commit: `Code_Example-langc_v01: Desarrollo de codigo de ejemplo del video 1 de langc - Author: maodecolombia`
  - [¿Qué hace `response`?](../AI_Queries/code_explanation/ai_query-langc_v01-response_usage.md)
  - [¿Por qué `lista[:2]` **no incluye el índice 2**?](../AI_Queries/code_explanation/ai_query-langc_v01-list_start_end_usage.md)
  - [¿Qué es `.extend()`?](../AI_Queries/code_explanation/ai_query-langc_v01-.extend_usage.md)
  - [¿Qué es loader?](../AI_Queries/code_explanation/ai_query-langc_v01-PyPDFLoader(filename).loader.load()_usage.md)
  - [¿Para qué es el  wd en `with open("archivo.pdf", "wb") as f:`](../AI_Queries/code_explanation/ai_query-langc_v01-wb_usage.md)

- ![alt text](../../assets/images/langc_v01-seccion_split_de_documents.png)
  - [`chunk_size` y `chunk_overlap` de `from langchain.text_splitter import RecursiveCharacterTextSplitter`](../AI_Queries/code_explanation/ai_query-langc_v01-chunk_usage.md)
    - [¿que significac la afirmacion "Estos límites incluyen tanto el texto de entrada (prompt) como la respuesta generada por el modelo"?](../AI_Queries/code_explanation/ai_query-langc_v01-meaning_inputpromptandanswer.md)
      - [¿A qué hace referecia "retrieval"?](../AI_Queries/code_explanation/ai_query-langc_v01-retrieval_meaning.md)
  - El script maneja 1500 caracteres pero cuanto sería el máximo chunk en función de los tokens para modelos de ChatGPT [¿Cuántos tokens acepta cada modelo de ChatGPT?](../AI_Queries/code_explanation/ai_query-langc_v01-max_tokens_Chatgptmodels.md)

- ![Embeddings e ingesta a base de datos vectorial](../../assets/images/langc_v01-seccion_Embeddings_ingesta_a_base_de_datos_vectorial.png)
  - [¿Qué hacen estas líneas?](../AI_Queries/code_explanation/ai_query-langc_v01-Embeddings_and_Vector_Store_Ingestion.md)
  - ![nuevas lineas de código](../../assets/images/langc_v01-seccion_Embeddings_ingesta_a_base_de_datos_vectorial-MOD.png)
  - [ChromaDB como base de datos persistente](../AI_Queries/code_explanation/ai_query-langc_v01-persistent_chromadb.md)

- ## Modelos de chat y cadenas para consulta de información
  ![alt text](../../assets/images/langc_v01-seccion_modelos-de-chat-y-cadenas-para-consultas.png)

  - [¿Qué hacen estas líneas?](../AI_Queries/code_explanation/ai_query-langc_v01-Chat_Models_and_Retrieval_Chains_for_Information_Querying.md)

  - [**Explicación detallada** de RetrievalQA.from_chain_type](ai_query-langc_v01-RetrievalQA.from_chain_type_usage.md)

- ![alt text](../../assets/images/langc_v01-seccion_modelos-de-chat-y-cadenas-para-consultas(query1).png)
- ![alt text](../../assets/images/langc_v01-seccion_modelos-de-chat-y-cadenas-para-consultas(query2).png)
- ![alt text](../../assets/images/langc_v01-seccion_modelos-de-chat-y-cadenas-para-consultas(query3).png)
- ![alt text](../../assets/images/langc_v01-seccion_modelos-de-chat-y-cadenas-para-consultas(query4).png)
  - [Uso de `qa_chain`](../AI_Queries/code_explanation/ai_query-langc_v01-qa_chain.run()_usage.md)

## Comentarios

- En este blog en [medium](https://medium.com/@murtuza753/using-llama-2-0-faiss-and-langchain-for-question-answering-on-your-own-data-682241488476) puedes ver un ejemplo de como usar Llama2

- Puedes hacerlo con una alternativa libre como llama, [repo github](https://github.com/gabalzate/LLM-s/tree/f03d4b8c6b8aa666c7db97f03da341842d14fcbe/Langchain-basico-pregunta-documentos)

- [llama-cpp-python is a Python binding for llama.cpp](https://python.langchain.com/docs/integrations/llms/llamacpp/)

- [Los LLM están dominando el mundo, ¿cómo entrar? - Omar Espejel](https://platzi.com/cursos/platziconf2023mx/los-llm-estan-dominando-el-mundo-como-entrar-omar-/)