# Sistema de Análisis de PDFs y Respuesta a Preguntas: Búsqueda y Recuperación de Información (con Recursos)

## 3. Búsqueda y Recuperación de Información \[41\]

Con el texto extraído de los PDFs y procesado mediante técnicas de PLN, el siguiente paso crucial es implementar un sistema de búsqueda eficiente. Este sistema permitirá al asistente del director de INVIAS encontrar respuestas precisas a sus preguntas dentro de los PDFs.

### 3.1. Construcción de un Índice

Para una búsqueda eficiente, crearemos un índice invertido. Este índice asocia cada palabra con los documentos y las posiciones donde aparece, lo que permite una búsqueda rápida de las palabras clave en las preguntas del usuario. \[41\]

### 3.2. Algoritmos de Búsqueda

Implementaremos algoritmos de búsqueda que consideren la similitud semántica entre la pregunta del usuario y el contenido de los PDFs. Esto significa que el sistema no solo buscará coincidencias exactas de palabras, sino que también intentará comprender el significado de la pregunta y encontrar respuestas relevantes. \[47, 81\]

* **TF-IDF:** Esta técnica mide la importancia de una palabra en un documento en relación con un conjunto de documentos. Permite identificar las palabras más relevantes para cada documento y usarlas para la búsqueda. \[65\]  
* **Modelos de incrustación de palabras (word embeddings):** Estos modelos representan las palabras como vectores en un espacio multidimensional, donde las palabras con significados similares se encuentran cerca unas de otras. Esto permite al sistema comparar la similitud semántica entre palabras y frases. \[49, 71\]

### 3.3. Ranking de Resultados

Para mostrar al usuario las respuestas más probables primero, implementaremos un sistema de ranking de resultados. Este sistema asignará una puntuación a cada respuesta potencial en función de su relevancia para la pregunta. \[66, 97, 99, 101\]

**Factores a considerar para el ranking:**

* **Similitud semántica:** Se utilizarán las técnicas de TF-IDF y word embeddings para medir la similitud semántica entre la pregunta y las posibles respuestas.  
* **Coincidencia de palabras clave:** Se contabilizará el número de palabras clave de la pregunta que aparecen en cada respuesta.  
* **Ubicación en el documento:** Se dará mayor puntuación a las respuestas que se encuentren en secciones relevantes del documento, como títulos o resúmenes.  
* **Frecuencia de términos:** Se considerará la frecuencia de los términos de la pregunta en el documento en relación con la respuesta.

## Próximos Pasos

Con la estrategia de búsqueda definida, el siguiente paso es investigar a fondo las diferentes técnicas de indexación, algoritmos de búsqueda y métodos de ranking. Evaluaremos sus ventajas, desventajas y cómo se adaptan a las necesidades específicas del sistema. Una vez que hayamos seleccionado las técnicas más adecuadas, continuaremos con el desarrollo del prototipo, incorporando el sistema de búsqueda para que el asistente del director de INVIAS pueda interactuar con los PDFs.

Recuerda Mauricio, que este es un proceso iterativo. A medida que avancemos, iremos refinando el sistema y realizando ajustes para asegurar que cumpla con tus expectativas y las del asistente del director de INVIAS.

## Fuentes citadas

* **\[41\] Manning, C. D., Raghavan, P., & Schütze, H. (2008). Introduction to Information Retrieval. Cambridge University Press.**  
* **\[47\] Bhavnani, S. K., & John, B. E. (2000, November). The strategic use of libraries and the Web. In Proceedings of the annual meeting-ASIS (Vol. 37, pp. 227-237). American Society for Information Science.**  
* **\[49\] Intelliarts. (2023, November 21). Retrieval-based chatbot for enterprises.. Retrieved from [https://intelliarts.com/blog/retrieval-based-chatbot-for-enterprises/](https://intelliarts.com/blog/retrieval-based-chatbot-for-enterprises/)**  
* **\[65\] Honnibal, M., & Montani, I. (2017). spaCy 2: Natural language understanding with Bloom embeddings, convolutional neural networks and incremental parsing. To appear.**  

