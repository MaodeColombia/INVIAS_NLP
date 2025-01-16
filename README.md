# Sistema de Análisis de PDFs y Respuesta a Preguntas: INVIAS_NLP

## Objetivo:

Desarrollar un sistema avanzado que permita al asistente del director de INVIAS interactuar con documentos PDF mediante una interfaz de chatbot. El sistema deberá ser capaz de comprender preguntas en lenguaje natural, extraer información relevante de los PDFs y proporcionar respuestas precisas y concisas.

## Actores:

- Mauricio Martínez (Ingeniero de Desarrollo de Sistemas de Información)  
- Director General de INVIAS  
- Asistente del Director General de INVIAS (Usuario principal del sistema)

## Estrategia de Desarrollo:

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

## Desarrollo de la estrategia


Propuesta de procesamiento de lenguaje de documentos internos de INVIAS para identificar documentos relacionados con con temas puntuales de consulta

El desarrollo del Sistema podrá cambiar en el transcurso del desarrollo por lo que la estructura de las carpetas se dejará como 

- [approach_1](./approach_1/): Esta es el primer enfoque formal para iniciar el desarrollo, el cual se está desarrollano con *Gemini Advance 1.5 Pro with Deep Research*
 
  - [Prompt AI Gemini V01.md](./approach_1/Prompt_AI_Gemini_V01.md): Prompt para Gemini
    
    - [Prompt AI Gemini V01A.md](./approach_1/Prompt_AI_Gemini_V01A.md/): Respuesta

    - [Prompt AI Gemini V02A.md](./Prompt_AI_Gemini_V02A.md/): Respuesta

    - [Prompt_AI_Gemini_V03A.md](./Prompt_AI_Gemini_V03A.md): Respuesta

    - [Prompt_AI_Gemini_V04A.md](./Prompt_AI_Gemini_V04A.md): Respuesta

    - [Prompt_AI_Gemini_V05A.md](./Prompt_AI_Gemini_V05A.md): Respuesta
  
##  Identificación de temas futuros

Para el desarrollo futuro del sistema, es fundamental estandarizar el almacenamiento de la información de manera eficiente y estructurada. Este proceso se basará en los lineamientos y recomendaciones técnicas presentadas por *Rosenthol (2013) en Developing with PDF: Dive Into the Portable Document Format*, y *Whitington (2011) en PDF Explained*. Estos autores enfatizan la importancia de adoptar estándares robustos y universales, como el formato PDF, para garantizar la interoperabilidad, la preservación a largo plazo y la accesibilidad de los documentos, aspectos esenciales en la implementación de soluciones tecnológicas como la propuesta presentada.


## Referencias

### Cursos de Platzi

- [Curso de LangChain](https://platzi.com/cursos/langchain-chatbots/) <sub>[langc]</sub>

- [Curso de Fundamentos de Procesamiento de Lenguaje Natural con Python y NLTK](https://platzi.com/cursos/python-lenguaje-natural/) <sub>[funpnl]</sub>

  - [Clase 4. Configurar ambiente de trabajo](./Platzi_codes/C04_workspace.ipynb)

- [Curso de Desarrollo de Chatbots con OpenAI](https://platzi.com/cursos/openai-api-23/)<sub>[oaib]</sub> 
  
  - [Clase 5. Aplicación de ejemplo utilizando modelos de OpenAI](./Platzi_codes/oaib_v05-adivinaranimal.ipynb)





### Consultas a las Inteligenicias Artificiales

- [Nociones básica de un archivo `requirements.txt`](./AI_Queries/prompt_AI_GPT-Requirements.md)

- [Uso del argumento `-r` en un archivo `requirements.txt`](./AI_Queries/prompt_AI_GPT-r_uses.md)

- [¿Qué es `sys_platform`?](./AI_Queries/prompt_AI_GPT-sys_plataform_uses.md)

- [Process to Create an Environment Variable in Windows](./AI_Queries/prompt_AI_GPT-Environment_variable_creation.md)

- [Acerca de PyMuPDF4LLM](./AI_Queries/prompt_AI_GPT-about_PyMuPDF4LLM.md)

- [Evitar que se corra `!pip install openai` cada vez que se corre el código](./AI_Queries/prompt_AI_GPT-openai_install_upgrade.md)

- [Roles de *Chat_Completions_API*](./AI_Queries/prompt_AI_GPT-Chat_Completions_API.md)

- [Parámetros adicionales de *Chat_Completions_API* que permiten personalizar la interacción con los modelos de chat](./AI_Queries/prompt_AI_GPT-Chat_completions_API_parameter.md)

- [Tipos de varibles en python](./AI_Queries/prompt_AI_GPT-variables_types.md)

- [Uso del try y exception para el manejo de errores](./AI_Queries/prompt_AI_GPT-try-exception_uses.md)

- [Definición de Aumento de la Capacidad de Recuperación en el contexto de RGA](./AI_Queries/prompt_AI_GPT-Enhancement_of_Retrieval_Capabilities(RAG).md)

- [Usos del `for`](./AI_Queries/prompt_AI_GPT-for_usage.md)



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

   Collado Alonso, M. Á. (2024). Implementación de técnicas de RAG (Retrieval Augmented Generation) sobre LLM (Large Language Models) para la extracción y generación de documentos en las entidades públicas [Trabajo de fin de máster, Universidad de Valladolid]. UVaDOC. https://uvadoc.uva.es/handle/10324/71509


