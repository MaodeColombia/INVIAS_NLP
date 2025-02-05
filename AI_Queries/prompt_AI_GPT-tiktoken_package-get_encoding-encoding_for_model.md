# 📌 **Guía Completa del Paquete `tiktoken`**  

`tiktoken` es una biblioteca de OpenAI diseñada para la **tokenización eficiente** de texto, utilizada en modelos como **GPT-3.5** y **GPT-4**. Su principal ventaja es que es mucho más rápida que métodos tradicionales como `GPT-2 BPE`.

---

## 🔹 **1. Instalación**
Si aún no tienes instalado `tiktoken`, puedes hacerlo con:
```bash
pip install tiktoken
```

---

## 🔹 **2. Principales Funciones y Métodos**
A continuación, se detallan las funciones más importantes de `tiktoken`:

| **Función** | **Descripción** |
|------------|---------------|
| `tiktoken.get_encoding(encoding_name)` | Obtiene un esquema de codificación específico. |
| `tiktoken.encoding_for_model(model_name)` | Obtiene la codificación recomendada para un modelo de OpenAI. |
| `encoding.encode(texto, allowed_special=set())` | Convierte un texto en una lista de tokens. |
| `encoding.decode(lista_tokens)` | Convierte una lista de tokens en texto. |
| `encoding.encode_ordinary(texto)` | Similar a `encode()`, pero ignora tokens especiales. |
| `encoding.encode_with_special_tokens(texto)` | Tokeniza el texto incluyendo tokens especiales. |
| `encoding.n_vocab` | Obtiene el número total de tokens en el vocabulario de la codificación. |
| `encoding.special_tokens_set` | Devuelve un conjunto con los tokens especiales definidos en la codificación. |

---

## 🔹 **3. Explicación con Ejemplos**
### 🏷 **(1) Obtener una codificación específica**
Si ya conoces el nombre de la codificación, puedes usar:
```python
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")  # Codificación usada en GPT-4 y GPT-3.5-turbo
print(encoding.n_vocab)  # Número total de tokens en el vocabulario
```
---

### 🏷 **(2) Obtener la codificación adecuada para un modelo**
Si no conoces la codificación, pero sí el modelo de OpenAI:
```python
encoding = tiktoken.encoding_for_model("gpt-4")
print(encoding.n_vocab)  # Número de tokens en el vocabulario
```
---

### 🏷 **(3) Tokenizar texto**
```python
text = "Hola, ¿cómo estás?"
tokens = encoding.encode(text)
print(tokens)  # [9906, 11, 64, 1050, 239, 34]
```
---

### 🏷 **(4) Convertir tokens en texto**
```python
decoded_text = encoding.decode(tokens)
print(decoded_text)  # "Hola, ¿cómo estás?"
```
---

### 🏷 **(5) Ignorar tokens especiales**
Si quieres ignorar tokens especiales durante la tokenización:
```python
tokens = encoding.encode_ordinary("¡Hola! <|endoftext|>")
print(tokens)  # No incluirá <|endoftext|> como token
```
---

### 🏷 **(6) Incluir tokens especiales**
Si necesitas incluir tokens especiales en la tokenización:
```python
tokens = encoding.encode_with_special_tokens("¡Hola! <|endoftext|>")
print(tokens)  # Incluirá <|endoftext|> como token especial
```
---

## 🔹 **4. Codificaciones Disponibles**
Algunos esquemas de codificación en `tiktoken` son:

| **Codificación** | **Modelos que la usan** |
|-----------------|-------------------------|
| `cl100k_base` | GPT-4, GPT-3.5-turbo |
| `p50k_base` | Codificación similar a GPT-3 |
| `r50k_base` | Usada en GPT-3 antiguo |

Si tienes dudas sobre qué codificación usar, **siempre usa `encoding_for_model()`**.

---

## ✅ **Conclusión**
`tiktoken` es una herramienta fundamental para trabajar con modelos de OpenAI, optimizando la tokenización de texto. Sus dos funciones más importantes son:
1. `get_encoding()`: Para obtener una codificación específica.
2. `encoding_for_model()`: Para obtener la codificación adecuada para un modelo.

Si necesitas manipular tokens, decodificar texto o trabajar con vocabularios, `tiktoken` te ofrece una API rápida y eficiente. 🚀


[How to count tokens with Tiktoken](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)