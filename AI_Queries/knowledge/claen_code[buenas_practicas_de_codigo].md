# Buenas Prácticas de Código - Clean Code

El objetivo de estas prácticas no es solo hacer que el código funcione, sino que sea **legible, robusto, mantenible y eficiente**. Este archivo está basado en <MMO_codes\langc\v01\langc_v01.ipynb>

## 1. Claridad y Legibilidad (Readability)

El código se escribe una vez, pero se lee muchas veces. La claridad es fundamental.

* **Nombres Descriptivos y Estándares de Nomenclatura**
  * **Práctica:** Usar nombres de variables y funciones que describan su propósito. Las variables que actúan como constantes se escriben en mayúsculas.
  * **Ejemplo:** `TEST_QUERY`, `EXPECTED_KEYWORDS`, `retrieved_docs`, `found_keywords_count`. Es inmediatamente obvio qué contiene cada variable sin necesidad de adivinar.
  * **Estándar/Principio:** **PEP 8**, la guía de estilo oficial de Python. Recomienda `snake_case` para variables y funciones, y `UPPER_CASE` para constantes. También se alinea con el principio del "Código Limpio" (Clean Code).

* **Comentarios Útiles y Espaciado Lógico**
  * **Práctica:** Usar comentarios para explicar el *porqué* de una decisión o para guiar al usuario. Usar bloques y espaciado para agrupar código relacionado.
  * **Ejemplo:**
  
    ```python
    # Aumentamos 'k' para tener más contexto que inspeccionar
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5}) 
    ```
  
    Los bloques como `# --- LÓGICA DEL TEST ---` dividen el script en fases lógicas, mejorando la comprensión de un vistazo.
  * **Estándar/Principio:** **"El Zen de Python"** (`import this` en Python) dice: "La legibilidad cuenta" (Readability counts) y "Espaciado es mejor que denso" (Sparse is better than dense).

* **Mensajes de Progreso para el Usuario**
  * **Práctica:** Informar al usuario sobre lo que está haciendo el script, especialmente en procesos largos o al encontrar errores.
  * **Ejemplo:** `print("🧪 Iniciando el Test...")`, `print(f"  -> Procesando lote {batch_number}/{total_batches}...")`. El uso de emojis (`🧪`, `🔍`, `✅`, `❌`) hace la salida más visual y rápida de interpretar.
  * **Estándar/Principio:** Aunque no es un estándar de código, es un principio fundamental de **Experiencia de Usuario (UX)** y **Experiencia de Desarrollador (DX)**.

## 2. Configuración Separada (Configuration Management)

* **Centralizar Variables Configurables**
  * **Práctica:** Agrupar todas las variables que un usuario podría necesitar cambiar en un solo lugar, al principio del script.
  * **Ejemplo:** El bloque `--- CONFIGURACIÓN DEL TEST ---` contiene `TEST_QUERY`, `PERSIST_DIRECTORY`, `EMBEDDING_MODEL`, etc.
  * **Estándar/Principio:** Evita los **"números mágicos"** o cadenas de texto hardcodeadas dentro de la lógica. Facilita enormemente el mantenimiento y la reutilización del script sin tener que cazar las variables por todo el código.

## 3. Robustez y Manejo de Errores (Robustness & Error Handling)

* **a. Fallar Rápido (Fail-Fast)**
  * **Práctica:** Comprobar las precondiciones (como la existencia de un archivo o una clave de API) al inicio del script. Si algo esencial falta, el programa debe detenerse inmediatamente con un error claro, en lugar de continuar y fallar más tarde de una forma misteriosa.
  * **Ejemplo:**
  
    ```python
    if not api_key_environ:
        raise ValueError("La variable de entorno OPENAI_API_KEY no está configurada.")
    ```
  
  * **Estándar/Principio:** Es un principio de diseño de software que busca hacer los fallos más obvios y fáciles de depurar.

* **Programación Defensiva**
  * **Práctica:** Escribir código que anticipe posibles problemas o datos faltantes.
  * **Ejemplo:** `source = doc.metadata.get("source", "desconocido")`. Usar `.get()` en un diccionario previene un `KeyError` si la clave `"source"` no existe, proporcionando un valor por defecto en su lugar.
  * **Estándar/Principio:** Es una práctica general de desarrollo de software para crear código más estable. En los scripts posteriores, se usó un bloque `try...except` para procesar los 512 PDFs, permitiendo que el script continuara incluso si un PDF estaba corrupto.

## 4. Modularidad y Reutilización (Visto en los Scripts Posteriores)

* **No te Repitas (Don't Repeat Yourself - DRY)**
  * **Práctica:** Si realizas la misma secuencia de acciones en varios lugares, encapsúlala en una función.
  * **Ejemplo:** En el script de diagnóstico de *chunks*, creamos la función `clean_text(text)`. Esto nos permitió aplicar la misma lógica de limpieza de manera ordenada y reutilizable.
  * **Estándar/Principio:** **Principio DRY**. Es uno de los pilares del desarrollo de software de calidad.

* **b. Tipado Estático Opcional (Type Hinting)**
  * **Práctica:** Añadir "pistas" sobre el tipo de datos que una función espera como entrada y el que devuelve como salida.
  * **Ejemplo:** `def clean_text(text: str) -> str:`
  * **Estándar/Principio:** **PEP 484**. Mejora drásticamente la legibilidad, ayuda a los editores de código a detectar errores y facilita el trabajo en equipo.

## 5. Eficiencia y Buenas Prácticas de API (Visto en el Último Script)

* **Procesamiento por Lotes (Batching)**
  * **Práctica:** Cuando se interactúa con una API que tiene límites de solicitud, procesar los datos en lotes más pequeños en lugar de enviar todo de una vez.
  * **Ejemplo:** El bucle `for i in range(0, total_docs, batch_size):` que procesaba los documentos en grupos de 200.
  * **Estándar/Principio:** Es una técnica estándar para manejar grandes volúmenes de datos y respetar los **límites de tasa (rate limits)** y de carga útil (payload) de las APIs, previniendo errores como el `BadRequestError` que obtuvimos.

En resumen, los scripts fueron evolucionando desde un enfoque lineal simple hacia uno más modular, robusto y eficiente, aplicando progresivamente estos principios para solucionar los problemas que encontramos.

---

Entendido. Primero, condensaré las prácticas que **faltaban** en nuestra discusión para tener un marco completo de desarrollo de software de calidad. Luego, con esa base completa, te generaré un "prompt universal" que puedes usar para que cualquier IA (incluyéndome) aplique estos conceptos a cualquier código que le presentes.

## Buenas Prácticas Adicionales para un Código Profesional

Además de las que ya cubrimos (legibilidad, configuración, robustez, etc.), aquí hay otros pilares fundamentales para un desarrollo de software sólido:

### 6. **Gestión de Dependencias (Reproducibilidad)**

* **Qué es:** En lugar de instalar paquetes manualmente, se listan todas las librerías externas que un proyecto necesita en un archivo, comúnmente l amado `requirements.txt`.
* **Por qué es importante:** Garantiza que cualquier persona (o servidor) que ejecute tu proyecto pueda recrear el mismo entorno con las mismas versiones de las librerías, evitando errores de "en mi máquina sí f nciona".
* **Estándar:** Es la práctica estándar en el ecosistema de Python, gestionada por `pip`.

### 7. **Pruebas Automatizadas (Testing)**

* **Qué es:** Escribir código cuyo único propósito es verificar que tu código principal funciona como se espera. Se crean "casos de prueba" para funciones específicas (pruebas unitarias) o para flujos de trabajo completos (pruebas de integración).
* **Por qué es importante:** Te da la confianza para hacer cambios y mejoras (refactorizar) sabiendo que si rompes algo, las pruebas te avisarán inmediatamente. Ahorra tiempo de depuración manual a largo plazo.
* **Estándar:** Frameworks como `pytest` (el más popular y recomendado) o `unittest` (incluido en Python) son el estándar de la industria.

### 8. **Principios de Seguridad Básicos**

* **Qué es:** Programar teniendo en cuenta posibles vulnerabilidades. Esto incluye:
  * **Validación de Entradas:** Nunca confiar en los datos que vienen del exterior (un usuario, otra API). Siempre se deben validar y "sanitizar".
  * **Manejo de Secretos:** Nunca escribir contraseñas, claves de API o tokens directamente en el código. Usar variables de entorno (como hicimos) o archivos de configuración seguros (como `.env`).
* **Por qué es importante:** Previene brechas de seguridad, pérdida de datos y accesos no autorizados.
* **Estándar:** Principios como los del **OWASP Top 10** (para aplicaciones web) son una referencia clave en seguridad.

### 9. **Estructura y Escalabilidad (Organización del Código)**

* **Qué es:** A medida que un script crece, las funciones sueltas no son suficientes. La **Programación Orientada a Objetos (OOP)** usando `clases` permite agrupar datos (atributos) y comportamientos (métodos) relacionados en entidades lógicas.
* **Por qué es importante:** Hace que el código complejo sea mucho más fácil de entender, mantener y extender. Si en nuestro caso quisiéramos tener múltiples "chatbots" con diferentes documentos, una clase `RAGSystem` sería la forma ideal de organizarlo.
* **Estándar:** OOP es un paradigma fundamental de la programación moderna.

### Prompt Universal para Mejorar Código con IA

Ahora sí, aquí tienes un prompt detallado y estructurado que encapsula todas estas buenas prácticas. Puedes copiarlo y pegarlo, reemplazando las secciones indicadas, para pedirle a una IA que mejore cualquier código.

```plaintext
  Actúa como un desarrollador de software senior y un experto en "Código Limpio" (Clean Code). Tu tarea es revisar y refactorizar el siguiente código de Python para mejorar su calidad general aplicando las mejores prácticas de la industria.
  
  **CÓDIGO A REVISAR:**
  \```python
  [PEGAR EL CÓDIGO AQUÍ]
  \```
  **CONTEXTO ADICIONAL (Opcional):**
  (Ej: "Este código es para un sistema de RAG y el principal problema es que es lento" o "Este es mi primer proyecto en Python y quiero que sea más legible").
  [DESCRIBIR EL PROPÓSITO DEL CÓDIGO Y CUALQUIER PROBLEMA ESPECÍFICO AQUÍ]
  
  
  **INSTRUCCIONES DE REFACTORIZACIÓN:**
  
  Por favor, aplica los siguientes principios al refactorizar el código:
  
  1.  **Legibilidad y Estilo (PEP 8):**
      * Asegura que el código siga las convenciones de formato de PEP 8.
      * Mejora los nombres de variables, funciones y clases para que sean claros y descriptivos.
      * Añade comentarios solo donde la lógica sea compleja y no evidente.
  
  2.  **Configuración y Flexibilidad:**
      * Identifica cualquier valor "hardcodeado" (rutas de archivos, URLs, números mágicos, nombres de modelos) y muévelo a una sección de configuración clara al inicio del script.
  
  3.  **Robustez y Manejo de Errores:**
      * Implementa un manejo de errores robusto con bloques `try...except` donde puedan ocurrir fallos (ej: operaciones de red, lectura de archivos).
      * Añade validaciones para las entradas o configuraciones críticas (Fail-Fast).
  
  4.  **Modularidad y Estructura (DRY):**
      * Refactoriza el código en funciones o clases para eliminar la duplicación (principio DRY).
      * Si el script es suficientemente complejo, propón una estructura basada en clases (OOP) que agrupe la lógica de manera coherente.
  
  5.  **Documentación y Tipado (Clarity):**
      * Añade `docstrings` a todas las funciones y clases explicando qué hacen, sus parámetros y qué devuelven.
      * Aplica "type hints" (tipado estático) de PEP 484 a los parámetros de las funciones y a los valores de retorno.
  
  6.  **Seguridad Básica:**
      * Revisa si hay problemas de seguridad obvios, como secretos hardcodeados, y sugiere el uso de variables de entorno.
      * Añade validaciones para cualquier entrada que provenga del exterior.
  
  7.  **Eficiencia:**
      * Busca cuellos de botella o bucles ineficientes y reemplázalos con alternativas más "Pythónicas" y de mejor rendimiento si es posible.
  
  
  **FORMATO DE LA RESPUESTA:**
  
  Por favor, estructura tu respuesta de la siguiente manera:
  
  1.  **CÓDIGO REFACTORIZADO:**
      * Primero, presenta la versión completa del código mejorado.
  
  2.  **RESUMEN DE CAMBIOS Y BUENAS PRÁCTICAS APLICADAS:**
      * Después del código, incluye una lista detallada, punto por punto, explicando los cambios que hiciste y qué buena práctica se aplicó en cada caso (ej: "Se movió la ruta del archivo a una constante `PDF_PATH` para mejorar la gestión de la configuración.").
```