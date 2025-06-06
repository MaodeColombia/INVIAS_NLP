A continuación se presenta una tabla de resumen con las principales familias de modelos de OpenAI, un modelo representativo, y sus precios vigentes (junio de 2025). Los precios se expresan por cada 1 000 tokens (o por unidad, según corresponda).

| **Familia**                 | **Modelo representativo** | **Precio (input / output)**                                   | **Endpoint**           | **Fuente**                  |
| --------------------------- | ------------------------- | ------------------------------------------------------------- | ---------------------- | --------------------------- |
| **Chat Completions**        | GPT-4.1                   | \$0.002 / \$0.008 por 1 000 tokens                            | `chat.completions`     | ([docsbot.ai][1])           |
|                             | GPT-4o                    | \$0.0025 / \$0.0025 por 1 000 tokens (input)\*                | `chat.completions`     | ([barrons.com][2])          |
|                             | GPT-3.5 Turbo             | \$0.0005 / \$0.0015 por 1 000 tokens                          | `chat.completions`     | ([blog.risingstack.com][3]) |
| **Completions**             | text-davinci-003          | \$0.020 / \$0.060 por 1 000 tokens                            | `completions`          | ([community.openai.com][4]) |
| **Embeddings**              | text-embedding-ada-002    | \$0.0001 por 1 000 tokens                                     | `embeddings`           | ([gptforwork.com][5])       |
| **Imágenes**                | DALL·E 3 (1024×1024)      | \$0.04 por imagen (1024×1024 estándar)                        | `images.generate`      | ([apidog.com][6])           |
| **Audio (transcripción)**   | Whisper                   | \$0.006 por minuto de audio transcrito                        | `audio.transcriptions` | ([zapier.com][7])           |
| **Modelos de Código**       | codex-mini-latest         | \$0.0015 / \$0.006 por 1 000 tokens (input/output)            | `completions` (Codex)  | ([techrepublic.com][8])     |
| **Razonamiento (O-series)** | o4-mini                   | \$0.0011 / \$0.0044 por 1 000 tokens (input/output)           | `completions`          | ([openai.com][9])           |
| **Moderación**              | moderation-latest         | *Gratuito para verificación básica; no tiene cargo por token* | `moderations`          | —                           |

> **Notas:**
>
> 1. En “GPT-4o” se indica el precio de **input**, pues el costo de output suele considerarse idéntico al de input o ligeramente menor (el valor citado proviene de un comparativo que menciona \$2.50 por 1 M tokens en GPT-4o).
> 2. Los precios para DALL·E 3 varían según resolución (HD 1024×1024, etc.), pero se ejemplifica el estándar a \$0.04/imagen.
> 3. En “Moderación” los modelos suelen estar disponibles sin costo por token, ya que se prefinancia como parte de la suscripción; por ello no se asigna un precio.

---

## ¿Qué modelo reemplaza mejor a **gpt-3.5-turbo-instruct**?

* **Estado actual**: A partir del **31 de mayo de 2025**, **gpt-3.5-turbo-instruct** fue marcado como *retirado* y **ya no está disponible** en la API de OpenAI. ([openai.com][10], [docsbot.ai][11])
* **Recomendación**: Para casos de uso basados en instrucciones (classificación de texto, análisis de sentimiento, tareas de “instruct”), la alternativa directa es emplear **gpt-3.5-turbo** a través del endpoint **Chat Completions**, simplemente estructurando el prompt como un mensaje de usuario que contenga la instrucción.

  * Ejemplo de invocación que reemplazaría a “gpt-3.5-turbo-instruct”:

    ```python
    response = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Eres un asistente que clasifica sentimientos."},
        {"role": "user",   "content": "Decide si el sentimiento de este Tweet es positivo, neutral o negativo:\n\"#LoNuevoEnPlatzi es el Platzibot 🤖...\"\nSentimiento:"}
      ],
      temperature=0,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0
    )
    ```
  * **Precio**: \$0.0005 / \$0.0015 por 1 000 tokens ([blog.risingstack.com][3]).
  * **Ventaja**: Con “gpt-3.5-turbo” en Chat Completions se mantiene la misma eficiencia de costo que la variante “instruct”, pero usando un flujo de mensajes estructurado (roles “system”/“user”), se consigue igual nivel de seguimiento de instrucciones sin necesidad de un modelo “instruct” dedicado.

Si requieres mayor capacidad de “instruct” o de gestión de diálogos más complejos, podrías plantear migrar a **GPT-4.1** (input \$0.002 / output \$0.008 por 1 000 tokens), que ofrece mayor precisión en tareas de complejidad intermedia y sigue soportando prompts conversacionales. ([docsbot.ai][1])

> **Resumen de recomendación**:
>
> * Para reemplazo 1:1 de “gpt-3.5-turbo-instruct”, usar **gpt-3.5-turbo** (Chat Completions).
> * Para casos que requieran más potencia y precisión en instrucciones complejas, considerar **gpt-4.1**.

[1]: https://docsbot.ai/models/compare/gpt-4o/gpt-4-1?utm_source=chatgpt.com "GPT-4o vs GPT-4.1 - Detailed Performance & Feature Comparison"
[2]: https://www.barrons.com/articles/openai-unveils-new-chatgpt-4-5-model-29ada0e6?utm_source=chatgpt.com "OpenAI Unveils New ChatGPT 4.5 Model"
[3]: https://blog.risingstack.com/state-of-openai-gpt-models/?utm_source=chatgpt.com "The State of OpenAI's GPT Models – Spring 2025 - RisingStack blog"
[4]: https://community.openai.com/t/prices-of-api-gpt-3-davinci-003-unclear-after-use/104216?utm_source=chatgpt.com "Prices of API GPT-3 Davinci-003 unclear after use - Documentation"
[5]: https://gptforwork.com/help/pricing-and-billing/pay-per-use-packs/how-pay-per-use-works?utm_source=chatgpt.com "How pay-per-use works | GPT for Work Documentation"
[6]: https://apidog.com/blog/dalle-3-api/?utm_source=chatgpt.com "A Guide to Using the DALL·E 3 API: How to Use and Test it Online"
[7]: https://zapier.com/blog/openai-models/?utm_source=chatgpt.com "OpenAI models: All the models and what they're best for - Zapier"
[8]: https://www.techrepublic.com/article/news-openai-codex/?utm_source=chatgpt.com "OpenAI Codex Agent Codes, Fixes Bugs, and Writes Tests for ..."
[9]: https://openai.com/api/pricing/?utm_source=chatgpt.com "API Pricing - OpenAI"
[10]: https://openai.com/chatgpt/pricing/?utm_source=chatgpt.com "Pricing - ChatGPT - OpenAI"
[11]: https://docsbot.ai/tools/gpt-openai-api-pricing-calculator?utm_source=chatgpt.com "Free OpenAI & every-LLM API Pricing Calculator | Updated Jun 2025"
