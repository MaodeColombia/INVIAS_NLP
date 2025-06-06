# Sistema de Análisis de PDFs y Respuesta a Preguntas: INVIAS_NLP

## Objetivo

Desarrollar un sistema avanzado que permita al asistente del director de INVIAS interactuar con documentos PDF mediante una interfaz de chatbot. El sistema deberá ser capaz de comprender preguntas en lenguaje natural, extraer información relevante de los PDFs y proporcionar respuestas precisas y concisas.

## Actores

- Mauricio Martínez (Ingeniero de Desarrollo de Sistemas de Información)  
- Director General de INVIAS  
- Asistente del Director General de INVIAS (Usuario principal del sistema)

## Estrategia de Desarrollo - Temario

### 1. Extracción de Información de los PDFs

- Bibliotecas:  
  - PyPDF2  
  - PDFMiner  
  - PDFQuery  
  - Tesseract (con OCR para extraer texto de imágenes dentro de los PDFs)  
  - PyMuPDF  
  - Tabula-py (para extraer tablas)  
  - Camelot (para extraer tablas)

- Estructuras de Datos:

  - Diccionarios (para almacenar información estructurada)  
  - Listas (para almacenar secuencias de datos)  
  - SQLite (base de datos ligera para almacenar y consultar información extraída)  
  
- Consideraciones:
  - Manejo de diferentes formatos de PDF  
  - Extracción de texto, tablas, imágenes y metadatos  
  - Detección de estructura del documento (títulos, secciones, párrafos)  
  - Gestión de PDFs con contenido escaneado (OCR)

### 2. Procesamiento del Lenguaje Natural (PLN)

- Bibliotecas:  
  - NLTK  
  - spaCy  
  - Transformers (modelos pre-entrenados como BERT, RoBERTa)  
  - Gensim (para modelos de temas y similitud semántica)

- Tareas:  
  - Pre-procesamiento (conversión a minúsculas, eliminación de puntuación)  
  - Tokenización (división del texto en palabras o frases)  
  - Eliminación de stop words (palabras comunes sin significado relevante)  
  - Lematización/Stemming (reducción de palabras a su raíz)  
  - Etiquetado gramatical (identificación de sustantivos, verbos, etc.)  
  - Análisis sintáctico (identificación de relaciones entre palabras)  
  - Extracción de entidades nombradas (personas, lugares, organizaciones)  
  - Reconocimiento de entidades (clasificación de entidades en categorías)  
  - Resolución de correferencias (identificación de entidades que se refieren a lo mismo)  
  - Análisis de sentimiento (identificación de emociones en el texto)

### 3. Búsqueda y Recuperación de Información

- Estrategias:  
  - Construcción de un índice invertido (mapeo de palabras a documentos)  
  - Algoritmos de búsqueda (BM25, Elasticsearch)  
  - Modelos de recuperación de información (TF-IDF, Okapi BM25, modelos de lenguaje)  
  - Modelos de incrustación de palabras (Word2Vec, GloVe, BERT)  
  - Ranking de resultados (basado en relevancia, ubicación, frecuencia, etc.)  
  - Similitud semántica (utilizando word embeddings o modelos de lenguaje)  
  - Expansión de consultas (agregando sinónimos o términos relacionados)

### 4. Interfaz de Chatbot

- Desarrollo de una interfaz:  
  - Bibliotecas: Tkinter, PyQt, Flask, Streamlit  
  - Integración con el sistema de análisis

- Elementos de la interfaz:  
  - Área de entrada de texto  
  - Área de visualización de respuestas  
  - Botones de acción (cargar PDF, hacer pregunta, etc.)  
  - Elementos visuales (iconos, gráficos)  
  - Barra de progreso (para mostrar el estado del procesamiento)  
  - Historial de chat

- Funcionalidades:  
  - Carga de uno o varios documentos PDF  
  - Formulación de preguntas en lenguaje natural  
  - Visualización de respuestas con fragmentos relevantes del documento  
  - Posibilidad de hacer preguntas de seguimiento  
  - Retroalimentación del usuario sobre la calidad de las respuestas

- Consideraciones:  
  - Diseño centrado en el usuario  
  - Personalización (adaptación a las necesidades del usuario)  
  - Accesibilidad  
  - Usabilidad

---

### Estrategia de Desarrollo - Prompts para la exploración de los temas propuestos

Propuesta de procesamiento de lenguaje de documentos internos de INVIAS para identificar documentos relacionados con temas puntuales de consulta

El desarrollo del Sistema podrá cambiar en el transcurso del desarrollo por lo que la estructura de las carpetas se dejará como  

- [approach_1](./approach_1/): Esta es el primer enfoque formal para iniciar el desarrollo, el cual se está desarrollano con *Gemini Advance 1.5 Pro with Deep Research*

  - [Prompt AI Gemini V01.md](./approach_1/Prompt_AI_Gemini_V01.md): Prompt para Gemini

    - [Prompt AI Gemini V01A.md](./approach_1/Prompt_AI_Gemini_V01A.md/): Respuesta

    - [Prompt AI Gemini V02A.md](./approach_1/Prompt_AI_Gemini_V02A.md/): Respuesta

    - [Prompt_AI_Gemini_V03A.md](./approach_1/Prompt_AI_Gemini_V03A.md): Respuesta

    - [Prompt_AI_Gemini_V04A.md](./approach_1/Prompt_AI_Gemini_V04A.md): Respuesta.

      - [Prompt_AI_Gemini_V04A_01.md](./approach_1/Prompt_AI_Gemini_V04A_01.md): Compleción vs. Embeddings en el Procesamiento del Lenguaje Natural

    - [Prompt_AI_Gemini_V05A.md](./approach_1/Prompt_AI_Gemini_V05A.md): Respuesta

    - [Prompt_AI_Gemini_V06A.md](./approach_1/Prompt_AI_Gemini_V06A.md): Respuesta

      - [Extracción de Información de PDF (texto)](./approach_1/Prompt_AI_Gemini_V06A_01.md): Respuesta

        - [Extracción de Información de PDF (metadata)](./approach_1/Prompt_AI_Gemini_V06A_01.01.md): Respuesta

#### 📁 Árbol de directorios

- 📁 AI_Queries/
  - 📁 [code_explanation/](./support/code_explanation.md)
- 📁 MMO_codes/
- 📁 Platzi_codes/
- 📁 approach_1/
  - 📁 outputs/
  - 📁 deepping/
  - 📁 upgrade_250107/
- 📁 assets/
  - 📁 images/

#### 📦 Paquetes instalados

## Identificación de temas futuros

Para el desarrollo futuro del sistema, es fundamental estandarizar el almacenamiento de la información de manera eficiente y estructurada. Este proceso se basará en los lineamientos y recomendaciones técnicas presentadas por *Rosenthol (2013) en Developing with PDF: Dive Into the Portable Document Format*, y *Whitington (2011) en PDF Explained*. Estos autores enfatizan la importancia de adoptar estándares robustos y universales, como el formato PDF, para garantizar la interoperabilidad, la preservación a largo plazo y la accesibilidad de los documentos, aspectos esenciales en la implementación de soluciones tecnológicas como la propuesta presentada.

Para fortalecer la toma de decisiones basada en datos en INVIAS, es esencial la implementación de un enfoque data-driven que optimice la gestión y el análisis de la información contenida en los documentos institucionales. Este proceso se apoyará en marcos y metodologías reconocidas, como las estrategias de gestión de datos presentadas por Provost y Fawcett (2013) en Data Science for Business y Davenport y Harris (2007) en Competing on Analytics: The New Science of Winning. Estos autores destacan la importancia de la integración de técnicas de minería de datos, aprendizaje automático y procesamiento del lenguaje natural para transformar datos no estructurados en conocimiento accionable. En este contexto, la adopción de herramientas de análisis semántico y recuperación de información avanzadas garantizará una mayor eficiencia en la identificación de patrones, tendencias y correlaciones dentro del ecosistema documental de INVIAS, facilitando la toma de decisiones estratégicas basadas en evidencia.

## Referencias

Para cada recurso utilizado en el desarrollo de este proyecto —incluyendo videos, cursos, lecturas y documentación técnica— se asigna una *referencia abreviada* que permite identificar su origen de forma concisa.

### Cursos de Platzi

- [Curso de LangChain](https://platzi.com/cursos/langchain-chatbots/). Referencia `langc`
  
  - Platzi. (s.f.). Curso de LangChain: Crea chatbots con LLMs y Python. Platzi. <https://platzi.com/cursos/langchain-chatbots/>. Consultado el 23 de mayo de 2025.
  - [Recursos del curso](/Platzi_codes/langc/)
  
- [Curso de Fundamentos de Procesamiento de Lenguaje Natural con Python y NLTK](https://platzi.com/cursos/python-lenguaje-natural/) <sub>[funpnl]</sub>

  - [Clase 4. Configurar ambiente de trabajo](./Platzi_codes/C04_workspace.ipynb)

- [Curso de Desarrollo de Chatbots con OpenAI](https://platzi.com/cursos/openai-api-23/). Referencia `oaib` 
  
  - [Clase 5. Aplicación de ejemplo utilizando modelos de OpenAI - código: `oaib_v05-adivinaranimal.ipynb`](./Platzi_codes/oaib_v05-adivinaranimal.ipynb)
  
    - [Version adaptada de `oaib_v05-adivinaranimal.ipynb`](./MMO_codes/GPT_adivinaranimal.ipynb)

- [Curso de LangChain para Manejo y Recuperación de Documentos](https://platzi.com/cursos/langchain-documents/) <sub>[lanmr]</sub>
  
  - Clase 2. Obtención de datos de la web con LangChain: Context aware data extraction - repositorio: [`curso-langchain-qa-documents`](https://github.com/platzi/curso-langchain-qa-documents.git) - código: [`oaib_v05-adivinaranimal.ipynb`](./Platzi_codes/lanmr_v02_text_extraction.ipynb)

- [Curso de Embeddings y Bases de Datos Vectoriales para NLP](https://platzi.com/cursos/embeddings-nlp/) <sub>[emydb]</sub>

  - Clase 13. Creación de un Motor de Búsqueda Semántico con Python - código: [`emydb_v13-Search_Embeddings.ipynb`](./Platzi_codes/emydb_v13-Search_Embeddings.ipynb)

### Consultas a las Inteligenicias Artificiales

- [¿Qué es git stash?](./AI_Queries/knowledge/stash_usage.md)

- [Nociones básica de un archivo `requirements.txt`](./AI_Queries/knowledge/prompt_AI_GPT-Requirements.md)

- [Uso del argumento `-r` en un archivo `requirements.txt`](./AI_Queries/knowledge/prompt_AI_GPT-r_uses.md)

- [¿Qué es `sys_platform`?](./AI_Queries/knowledge/prompt_AI_GPT-sys_plataform_uses.md)

- [Process to Create an Environment Variable in Windows](./AI_Queries/knowledge/prompt_AI_GPT-Environment_variable_creation.md)

- [Acerca de PyMuPDF4LLM](./AI_Queries/knowledge/prompt_AI_GPT-about_PyMuPDF4LLM.md)

- [Evitar que se corra `!pip install openai` cada vez que se corre el código](./AI_Queries/knowledge/prompt_AI_GPT-openai_install_upgrade.md)

- [Roles de *Chat_Completions_API*](./AI_Queries/knowledge/prompt_AI_GPT-Chat_Completions_API.md)

- [Parámetros adicionales de *Chat_Completions_API* que permiten personalizar la interacción con los modelos de chat](./AI_Queries/knowledge/prompt_AI_GPT-Chat_completions_API_parameter.md)

- [Tipos de varibles en python](./AI_Queries/knowledge/prompt_AI_GPT-variables_types.md)

- [Uso del try y exception para el manejo de errores](./AI_Queries/knowledge/prompt_AI_GPT-try-exception_uses.md)

- [Definición de Aumento de la Capacidad de Recuperación en el contexto de RGA](./AI_Queries/knowledge/prompt_AI_GPT-Enhancement_of_Retrieval_Capabilities(RAG).md)

- [Usos del `for`](./AI_Queries/knowledge/prompt_AI_GPT-for_usage.md)

- [Contraste **fine-tuning** (ajuste fino) y **RAG** (**Retrieval-Augmented Generation**)](https://platform.openai.com/docs/guides/fine-tuning)

- [Dirección de las operaciones realizadas sobre un **DataFrame** o **Series**, `axis=0` (vertical, para filas) y `axis=1`(horizontal, para columnas)](./AI_Queries/knowledge/prompt_AL_GPT-diferencias_axis0h_axis1v.md)

- [Principios SOLID, la estructura de una 'función en Python](./AI_Queries/knowledge/prompt_AI-GPT-SOLID_foundations-def.md)

- [Bloques de código compatibles con Jupyter Notebook en VSCode](./AI_Queries/knowledge/prompt_AI_GPT-code_bloks-jupyternotebook.md)

- [Los tipos de salida (return type) que devuelve una función](./AI_Queries/knowledge/prompt_AI-GPT-SOLID_foundations-return_types.md)

- [El uso de `with`, la función `open()` y el manejo del archivo](./AI_Queries/knowledge/prompt_ALGPT-with_open.md)

- [Create chat completion de OpenAI.](./AI_Queries/knowledge/prompr_AI_GTP-CodeExplanation01-chat_completions_API.md)

- [Obtener el historial de cambios de un archivo específico en Git y mostrarlo en la terminal](./AI_Queries/knowledge/prompt_AI-GPT-selected_log_file.md)

- [Máximo número de tokens que se puede enviar a la API de OpenAI](./AI_Queries/knowledge/prompt_AI_GPT-max_output_tokens_to_API.md)

- [Package Usage - tiktoken: tiktoken.encoding.n_vocab](./AI_Queries/knowledge/prompt_AI_GPT-tiktoken_package-n_vocab.md)

- [Package Usage - tiktoken: tiktoken.get_encoding() y tiktoken.encoding_for_model()](./AI_Queries/knowledge/prompt_AI_GPT-tiktoken_package-get_encoding-encoding_for_model.md)

- [Cómo los modelos para embeddings como `sentence-transforme` y `ChatGpt` manejan inputs muy grandes](./AI_Queries/knowledge/prompt_AI_GPT-Transformer-how_works.md)

- [Cómo crear un entorno virtual](./AI_Queries/knowledge/prompt_AI_GPT-Create_Virtual_environment+install_requirements.md)

#### Code explanation

- [Curso de Langchain](/AI_Queries/code_explanation/)

### Youtube

- [Domina el API de OpenAI - De Principiante a Experto](https://youtube.com/playlist?list=PLgQnGGtCss_gYY4lsuO-hees3dBOqlyv4&si=7Xya0eqKDM1wqVMa)

  - [Github](https://github.com/alarcon7a/openai-api-tutorial)

### Referencias Bibliográficas

1. **OpenAI Platform Documentation**  
   OpenAI. (2025). *Chat Completions*. Recuperado de [https://platform.openai.com/docs/guides/chat](https://platform.openai.com/docs/guides/chat)

   - Documentación oficial sobre cómo usar la API de completions de chat, incluyendo ejemplos prácticos y parámetros configurables.

2. **OpenAI API Reference**  
   OpenAI. (2025). *API Reference for Chat Models*. Recuperado de [https://platform.openai.com/docs/api-reference](https://platform.openai.com/docs/api-reference)  

   - Referencia técnica detallada sobre los métodos disponibles, parámetros, y respuestas del modelo.

3. **OpenAI Cookbook**  
   OpenAI. (2025). *Practical Examples for Chat Models*. Recuperado de [https://github.com/openai/openai-cookbook](https://github.com/openai/openai-cookbook)  

   - Ejemplos prácticos y avanzados para trabajar con los modelos de OpenAI, incluyendo personalización y casos de uso específicos.

4. **OpenAI Community Forum**  
   OpenAI. (2025). *Discussions and Tutorials on Chat Models*. Recuperado de [https://community.openai.com](https://community.openai.com)

   - Foros donde desarrolladores y usuarios comparten experiencias, soluciones, y guías relacionadas con el uso de la API.

5. **Introducción a la Inteligencia Artificial con OpenAI**  
   Martínez, J., & López, R. (2024). *Interacción con modelos de lenguaje natural*. Editorial TechPress.  
  
   - Libro que incluye fundamentos teóricos y prácticos sobre cómo utilizar APIs de modelos de lenguaje como OpenAI.

6. **OpenAI Developer Quickstart**  
   OpenAI. (2025). *Quickstart Guide for Developers*. Recuperado de [https://platform.openai.com/docs/quickstart?language-preference=python](https://platform.openai.com/docs/quickstart?language-preference=python)  
   - Guía inicial para desarrolladores sobre cómo integrar y usar la API de OpenAI con ejemplos en Python.

7. **Text Generation Guide**  
   OpenAI. (2025). *Text Generation with OpenAI Models*. Recuperado de [https://platform.openai.com/docs/guides/text-generation](https://platform.openai.com/docs/guides/text-generation)  
   - Guía detallada sobre cómo generar texto utilizando los modelos de OpenAI, incluyendo parámetros configurables y mejores prácticas.  

8. **Trabajo de grado de Implementación de técnicas de RAG sobre LLM.**

   Collado Alonso, M. Á. (2024). Implementación de técnicas de RAG (Retrieval Augmented Generation) sobre LLM (Large Language Models) para la extracción y generación de documentos en las entidades públicas [Trabajo de fin de máster, Universidad de Valladolid]. UVaDOC. <https://uvadoc.uva.es/handle/10324/71509>

9. **Fine-Tuning Guide**  
   OpenAI. (2025). *Fine-Tuning Guide*. Recuperado de [https://platform.openai.com/docs/guides/fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)  

   Guía oficial sobre cómo realizar el ajuste fino de modelos de lenguaje, incluyendo los pasos necesarios, configuraciones avanzadas y ejemplos prácticos para personalizar modelos en tareas específicas.

10. **Counting Tokens with Tiktoken**  
    OpenAI. (2025). How to Count Tokens with Tiktoken. Recuperado de <https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken>

    Ejemplo práctico sobre cómo contar tokens utilizando la biblioteca tiktoken, con explicaciones detalladas sobre la tokenización y su impacto en el uso de la API de OpenAI.

### Modelos Hugging Face

- Hugging Face. (n.d.). google/pegasus-xsum. Hugging Face. Retrieved January 3, 2025, from <https://huggingface.co/google/pegasus-xsum>

## Useful commands

### Gitbash

1. ```bash
   pip freeze > ./approach_1/requirements.txt
   ```  

2. ```bash
   pipdeptree > ./approach_1/tree.txt
   ```

     - pipdeptree reporta los conflictos de la siguiente manera

       ```markdown
       Warning!!! Possibly conflicting dependencies found:
       \* pinecone-client==5.0.1
         \- pinecone-plugin-inference [required: >=1.0.3,<2.0.0, installed: 3.1.0]
       ------------------------------------------------------------------------
       ```

       Se soluciona con el siguiente script

       ```bash
       pip install --force-reinstall 'pinecone-client==5.0.1' 'pinecone-plugin-inference>=1.0.3,<2.0.0'
       ```

3. Estando `~/INVIAS_NLP (main)` ejecutar:

   ```bash
   git log --pretty=format:"Commit: %h - Date: %ad%nMessage: %s - Author: %an" --date=format:%Y%m%d-%H%M%S> ./approach_1/commits.txt
   ```

   - Solo text del commit

     ```bash
     git log --pretty=format:"Message: %s" > ./approach_1/commits.txt
     ```

4. Reinstala PyTorch ignorando archivos en caché para evitar errores.

   ```bash
   pip install torch --no-cache-dir
   ```

   o purga la cache

   ```bash
   pip cache purge
   ```

   - Si se necesita instalar una versión específica, *(Reemplazar `2.0.1` por la versión que se necesite).*  

     ```bash
     pip install torch==2.0.1 --no-cache-dir
     ```

5. Archivos modificados en un commit específico en Git  

   - Ver solo los nombres de los archivos modificados en un commit

     ```bash
     git show --name-only <commit_hash>
     ```

     Esto te muestra el mensaje del commit y los nombres de los archivos modificados.

     ```plaintext
     commit 1ee305a080c701ad193cbb3ee15919493096729c (HEAD -> main, origin/main, origin/HEAD)
     Author: maodecolombia <maodecolombia@gmail.com>
     Date:   Tue May 20 14:52:38 2025 -0500
     - Minor Edits: Presentación del archivo README.md
     README.md
     approach_1/Prompt_AI_Gemini_V01A.md
     (NLP_Congreso) 
     ```

   - Alternativa rápida para ver el listado limpio (sin mensaje ni diff)**

     ```bash
     git diff-tree --no-commit-id --name-only -r <commit_hash>
     ```

     Este comando lista solo los nombres de los archivos.

     ```bash
     $ git diff-tree --no-commit-id --name-only -r  1ee305a
     README.md
     approach_1/Prompt_AI_Gemini_V01A.md
     (NLP_Congreso)
     ```

6. **Deshacer un commit que ya se ha subido al repositorio remoto**, hay dos enfoques

   🔄 OPCIÓN 1: **Deshacer commit remoto y sobrescribirlo (fuerza total)**

   Si quieres eliminar el commit remoto como si **nunca hubiera existido**, y **puedes forzar el push** (por ejemplo, trabajas solo o el equipo lo permite):

    🔧 Pasos:

   ```bash
   # 1. Vuelve al estado anterior al último commit
   git reset --hard HEAD~1

   # 2. Fuerza el push para sobrescribir en el remoto
   git push origin HEAD --force
    ```

   Esto **borra** el commit local y remoto.

   🔁 OPCIÓN 2: **Revertir el commit (crea un nuevo commit que deshace el anterior)**

   Si **no puedes sobrescribir el historial remoto** (por políticas de equipo), lo correcto es **revertir**:

   ```bash
   git revert <commit_hash>
   git push origin main
   ```

   Esto **no borra historial**, sino que agrega un commit que revierte los cambios del anterior. Es más seguro y colaborativo.  
