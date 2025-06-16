# **BORRARDOR: Convención uniforme para la creación de etiquetas bibliográficas (citation keys)**

## Convención propuesta: `autor_año_tipo_identificador`

#### 1. **autor**

Usa el primer apellido del autor o nombre institucional (ej.: `platzi`, `microsoft`, `deckler`).

#### 2. **año**

Año de publicación o "s.f." si no tiene fecha (sin puntos). Ejemplo: `2024`, `sf`.

#### 3. **tipo**

Abreviatura del tipo de recurso:

* `doc` = documento / artículo
* `vid` = video / clase en video
* `cur` = curso completo
* `cap` = capítulo o clase específica
* `web` = sitio web técnico
* `bib` = libro
* `pat` = patente
* `std` = norma / estándar técnico

#### 4. **identificador**

Una palabra clave breve que identifique el contenido (por tema, tecnología o nombre del módulo).

---

### 🧠 Ejemplos aplicados a tu caso:

| Recurso                            | Etiqueta sugerida         |
| ---------------------------------- | ------------------------- |
| Curso de LangChain de Platzi       | `platzi_sf_cur_langchain` |
| Curso de Fundamentos NLTK          | `platzi_sf_cur_nltk`      |
| Clase 4: Configurar ambiente       | `platzi_sf_cap_ambiente`  |
| Curso de Chatbots con OpenAI       | `platzi_sf_cur_chatbots`  |
| Clase 5: Aplicación modelos OpenAI | `platzi_sf_cap_openai`    |

---

### 📌 Recomendaciones adicionales:

* Siempre en minúscula.
* Sin espacios ni caracteres especiales (usa guiones bajos `_`).
* Si usas Zotero o BibTeX, puedes automatizar la generación de estos `citation keys` con herramientas como Better BibTeX.

---

¿Quieres que revise tus referencias actuales y te devuelva todas las etiquetas normalizadas con esta convención?
