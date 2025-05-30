En la función `client.chat.completions.create` de la API de OpenAI, los mensajes se estructuran en una lista donde cada elemento es un diccionario que contiene dos claves: `role` y `content`. El campo `role` define el rol del emisor del mensaje, y puede tomar uno de los siguientes valores:

1. **system**: Este rol se utiliza para establecer el comportamiento y las instrucciones iniciales del modelo. El mensaje asociado puede definir el contexto, las reglas o la personalidad que el modelo debe adoptar durante la conversación. Por ejemplo, un mensaje con rol `system` podría indicar: "Eres un asistente útil y conciso".

2. **user**: Corresponde a los mensajes enviados por el usuario. Estos mensajes representan las preguntas o instrucciones directas que el usuario proporciona al modelo. Por ejemplo, un mensaje con rol `user` podría ser: "¿Cuál es la capital de Francia?".

3. **assistant**: Este rol es utilizado por el modelo para generar respuestas al usuario. En las respuestas de la API, los mensajes generados por el modelo tendrán el rol `assistant`, indicando que provienen del asistente virtual.

Es importante destacar que, según la documentación actual de OpenAI, solo se permiten estos tres roles: `system`, `user` y `assistant`. El uso adecuado de estos roles permite estructurar conversaciones más efectivas y controlar el comportamiento del modelo de manera más precisa. 

Al estructurar los mensajes de esta forma, se facilita una interacción más natural y coherente con el modelo, permitiendo que las respuestas generadas sean más alineadas con las expectativas y necesidades del usuario.