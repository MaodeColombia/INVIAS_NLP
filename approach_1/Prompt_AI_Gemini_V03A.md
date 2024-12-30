# **Sistema de Análisis de PDFs y Respuesta a Preguntas: Procesamiento del Lenguaje Natural (PLN)**

## 2. Procesamiento del Lenguaje Natural (PLN)

Una vez que hayamos extraído el texto de los PDFs, el siguiente paso es procesarlo para que el sistema pueda "entenderlo". Para lograr esto, utilizaremos técnicas de Procesamiento del Lenguaje Natural (PLN). El PLN nos permitirá transformar el texto en una forma que la computadora pueda comprender y analizar, lo que a su vez permitirá al sistema buscar respuestas relevantes a las preguntas del usuario.

### **2.1. Bibliotecas de Python para PLN**

Python ofrece una variedad de bibliotecas para PLN, y para este proyecto consideraremos las siguientes:

* **NLTK (Natural Language Toolkit):** Esta biblioteca es una de las más populares para PLN en Python. NLTK ofrece una amplia gama de herramientas para diversas tareas, como tokenización (dividir el texto en palabras o frases), stemming (reducir las palabras a su raíz), lematización (reducir las palabras a su forma base) y etiquetado gramatical (identificar la función de las palabras en una oración) 1. Su versatilidad y la gran cantidad de recursos que ofrece la convierten en una herramienta fundamental para el análisis lingüístico.  
* **spaCy:** Esta biblioteca se destaca por su velocidad y eficiencia en el procesamiento de texto. spaCy es ideal para tareas como el análisis sintáctico (identificar la estructura de las oraciones) y la identificación de entidades (reconocer nombres de personas, lugares, organizaciones, etc.) 1. Su enfoque en el rendimiento la convierte en una excelente opción para procesar grandes volúmenes de texto de manera rápida y precisa.  
* **Transformers:** Esta biblioteca nos permitirá utilizar modelos de lenguaje pre-entrenados de última generación, como BERT o RoBERTa. Estos modelos pueden capturar relaciones complejas entre palabras y frases, lo que mejora la comprensión del significado del texto 1. Su capacidad para el análisis semántico profundo nos permitirá construir un sistema más preciso y capaz de responder preguntas complejas.

### 2.2. Tareas de PLN para el Sistema

Para procesar el texto extraído de los PDFs, aplicaremos las siguientes técnicas de PLN:

* **Pre-procesamiento:** Antes de aplicar las técnicas de PLN, limpiaremos el texto. Esto incluye eliminar caracteres especiales, manejar diferentes codificaciones y convertir el texto a minúsculas. El pre-procesamiento asegura que el texto esté en un formato uniforme y listo para el análisis.  

* **Tokenización:** Dividiremos el texto en unidades individuales, como palabras o frases. La tokenización es un paso fundamental para el análisis del lenguaje, ya que permite a la computadora trabajar con unidades de significado.  

* **Eliminación de stop words:** Eliminaremos palabras comunes que no aportan mucho significado al análisis, como "el", "la", "un", "en", "de", etc. Esto reduce el tamaño del texto y facilita el análisis.  

* **Lematización:** Reduciremos las palabras a su forma base o lema. Por ejemplo, "corriendo" se convertiría en "correr", y "mejores" en "mejor". La lematización ayuda a agrupar palabras con el mismo significado, lo que facilita el análisis semántico.  

* **Etiquetado gramatical:** Identificaremos la función gramatical de las palabras, como sustantivo, verbo, adjetivo, etc. Esta información es útil para comprender la estructura de las oraciones y el significado del texto.  

* **Extracción de entidades:** Identificaremos nombres de personas, lugares, organizaciones, fechas, etc. Esto nos permitirá extraer información específica del texto y responder preguntas que se refieran a estas entidades.

## Próximos Pasos

Ahora que tenemos una estrategia para el PLN, el siguiente paso es investigar a fondo las bibliotecas mencionadas (NLTK, spaCy y Transformers) y determinar cuál es la más adecuada para nuestro proyecto. Consideraremos sus fortalezas, debilidades y cómo se adaptan a las necesidades específicas del sistema. Una vez seleccionada la biblioteca, continuaremos con el desarrollo del prototipo, incorporando las técnicas de PLN para el análisis del texto.  

Recordar que esto es un proceso iterativo, a medida que avancemos, iremos refinando el sistema y realizando ajustes para asegurar que cumpla con tus expectativas y las del asistente del director de INVIAS.

### Fuentes citadas

1\. Top 8 Python Libraries For Natural Language Processing (NLP) in 2023 | by Soffos AI, acceso: diciembre 30, 2024, [https://medium.com/@soffosdotai/top-8-python-libraries-for-natural-language-processing-nlp-in-2023-5963bfa53296](https://medium.com/@soffosdotai/top-8-python-libraries-for-natural-language-processing-nlp-in-2023-5963bfa53296)