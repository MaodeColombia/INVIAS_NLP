# Estructura de la respuesta de la API

Input:

```python
# Ejecutando esta linea de python para obtener la respuesta del modelo `gpt-4o-mini`
completion.choices[0].message
```

Output:

```plaintext
ChatCompletionMessage(content='¡Hola! Claro, estaré encantado de ayudarte a aprender sobre la API de OpenAI. La API de OpenAI te permite interactuar con modelos de inteligencia artificial, como GPT (Generative Pre-trained Transformer), para realizar tareas de procesamiento de lenguaje natural. Aquí tienes un resumen de los aspectos clave de la API:\n\n### 1. **¿Qué es la API de OpenAI?**\nLa API de OpenAI proporciona acceso a modelos de IA que pueden generar texto, responder preguntas, traducir idiomas, y realizar muchas otras tareas relacionadas con el lenguaje.\n\n### 2. **Cómo empezar**\n- **Registro**: Necesitas registrarte en el sitio web de OpenAI y obtener una clave de API.\n- **Documentación**: Puedes consultar la [documentación oficial de OpenAI](https://platform.openai.com/docs/) para obtener información detallada sobre cómo utilizar la API.\n\n### 3. **Llamadas a la API**\nPuedes hacer solicitudes a la API utilizando bibliotecas HTTP en varios lenguajes de programación. Aquí hay un ejemplo básico en Python usando la biblioteca `requests`:\n\n```python\nimport requests\n\n# Definir la clave de API y el endpoint\napi_key = "tu_clave_de_api"\nendpoint = "https://api.openai.com/v1/chat/completions"\n\n# Crear la solicitud\nheaders = {\n    "Authorization": f"Bearer {api_key}",\n    "Content-Type": "application/json"\n}\n\ndata = {\n    "model": "gpt-3.5-turbo",\n    "messages": [{"role": "user", "content": "Hola, ¿cómo estás?"}],\n}\n\nresponse = requests.post(endpoint, headers=headers, json=data)\nprint(response.json())\n```\n\n### 4. **Modelos**\nExisten diferentes modelos disponibles, con capacidades y precios variables. Por ejemplo:\n- `gpt-3.5-turbo`: adecuado para la mayoría de las aplicaciones de chat.\n- `gpt-4`: ofrece capacidades más avanzadas (si está disponible en tu acceso).\n\n### 5. **Parámetros de la API**\nAlgunos parámetros que puedes utilizar incluyen:\n- **messages**: Un array de mensajes que representa un historial de conversación.\n- **max_tokens**: El número máximo de tokens que deseas en la respuesta.\n- **temperature**: Controla la aleatoriedad de las respuestas (valores más bajos hacen que el texto sea más determinista).\n\n### 6. **Ejemplos de uso**\nPuedes utilizar la API para:\n- Generación de texto creativo.\n- Respuestas a preguntas frecuentes.\n- Resumen de texto.\n- Traducción de idiomas.\n  \n### 7. **Consideraciones de uso**\n- **Costos**: Revisa la estructura de precios para entender los costos asociados con el uso de la API.\n- **Límites**: Ten en cuenta los límites de uso y las políticas de contenido de OpenAI.\n\nSi tienes preguntas más específicas o deseas profundizar en algún tema, ¡dímelo!', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)
```
La estrutura del output es:

- `content`:

   ```plaintext
   '¡Hola! Claro, estaré encantado de ayudarte a aprender sobre la API de OpenAI. ...'
   ```

   **Descripción**: Este es el contenido principal de la respuesta generada por el modelo.

   **Función**: Contiene el texto que responde a la consulta del usuario. Es el cuerpo del mensaje que incluye la explicación y los detalles.


- `refusal`:

   ```plaintext
   None
   ```

   **Descripción**: Representa si el modelo ha rechazado responder la consulta.

   **Función**: Si el modelo determina que la solicitud es inapropiada, el contenido podría ser reemplazado por un rechazo. En este caso, no hubo rechazo, por lo que aparece como `None`.


- `role`:

   ```plaintext
   'assistant'
   ```

   **Descripción**: Indica el papel que está desempeñando el modelo en esta conversación.

   **Función**: Define quién genera esta respuesta. Aquí, el modelo actúa como un asistente.


- `audio`:

   ```plaintext
   None
   ```

   **Descripción**: Campo reservado para datos de salida de audio, en caso de que se utilice un modelo que soporte respuestas habladas.

   **Función**: Actualmente está vacío (`None`), porque esta respuesta no incluye audio.


- `function_call`:

   ```plaintext
   None
   ```

   **Descripción**: Representa si el modelo está solicitando realizar una llamada a una función externa.

   **Función**: Si el modelo decidiera invocar una función específica para completar la solicitud (por ejemplo, consultar una API externa o realizar un cálculo), este campo incluiría los detalles de esa llamada. Aquí no se ha realizado ninguna llamada a funciones.


- `tool_calls`:

   ```plaintext
   None
   ```

   **Descripción**: Campo utilizado si el modelo necesita realizar llamadas a herramientas externas, como bases de datos o servicios complementarios.

   **Función**: En este caso, no se usó ninguna herramienta externa, por lo que aparece como `None`.

---

**Estructura jerárquica de la respuesta**

- **Raíz**: Objeto de respuesta de la API (en este caso fue en formato Markdown).

  `content`: El mensaje principal que responde a la consulta.

  `refusal`: Indica si hubo rechazo a la solicitud.

  `role`: Rol del generador de esta respuesta (generalmente `"assistant"`).

  `audio`: Reservado para salidas de audio.

  `function_call`: Información sobre llamadas a funciones externas.

  `tool_calls`: Información sobre el uso de herramientas adicionales.

---


| **Campo**        | **Valor en el ejemplo**                                                                                     | **Descripción**                                                                                          | **Función**                                                                                              | **Código para acceder**                             |
|-------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| `content`         | `'¡Hola! Claro, estaré encantado de ayudarte a aprender sobre la API de OpenAI. ...'`                     | Contiene el texto principal de la respuesta del modelo.                                                  | Proporcionar la respuesta generada al usuario, basada en la solicitud.                                  | `completion.choices[0].message.content`           |
| `refusal`         | `None`                                                                                                    | Indica si el modelo rechazó responder la solicitud.                                                      | Si el modelo considera inapropiada la consulta, puede rechazarla (en este caso, no hubo rechazo).        | `completion.choices[0].message.refusal`           |
| `role`            | `'assistant'`                                                                                            | Define el papel del emisor de la respuesta (generalmente `"assistant"`).                                  | Identificar que la respuesta proviene del asistente virtual o del modelo.                               | `completion.choices[0].message.role`              |
| `audio`           | `None`                                                                                                    | Campo reservado para datos de audio, en caso de que se soporte respuestas habladas.                      | Usado cuando la respuesta incluye una salida de voz (vacío en este caso).                               | `completion.choices[0].message.audio`             |
| `function_call`    | `None`                                                                                                    | Representa si el modelo solicita realizar una llamada a una función externa.                             | Permitir que el modelo invoque funciones adicionales para procesar la solicitud (no se usó en este caso).| `completion.choices[0].message.function_call`     |
| `tool_calls`      | `None`                                                                                                    | Campo reservado para llamadas a herramientas o servicios externos.                                       | Permitir el uso de herramientas externas para resolver consultas más avanzadas (vacío en este caso).    | `completion.choices[0].message.tool_calls`        |
