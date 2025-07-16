---
title: Manual de Conventions para Mensajes de Commit
---

```toc
```

## 1. Introducción

### 1.1 Propósito del manual

Este documento ofrece una guía clara y concisa para redactar mensajes de commit en los repositorios de código del equipo. El objetivo es asegurar que cada cambio quede registrado de manera uniforme, legible y fácilmente rastreable, reduciendo ambigüedad y facilitando el mantenimiento del historial de versiones.

### 1.2 Beneficios de un estándar de commit

- **Claridad inmediata**: Los desarrolladores pueden comprender de un vistazo el alcance y objetivo de cada commit.

- **Mejor colaboración**: Facilita la revisión de código y la detección de cambios relevantes al integrar ramas.

- **Automatización de procesos**: Permite generar changelogs y validar el formato con herramientas de CI/CD.

- **Trazabilidad**: Facilita rastrear cuándo y por qué se introdujo cada modificación, mejorando el diagnóstico de errores.

## 2. Ámbito de aplicación

En esta sección se define dónde y a quién aplica este manual.

### 2.1 Repositorios y proyectos cubiertos

- Repositorios de código fuente del equipo de desarrollo de INVIAS.

- Proyectos internos de scripts, notebooks y herramientas de IA.

- Módulos de ejemplos de código y documentación técnica.

### 2.2 Equipos y roles involucrados

- **Desarrolladores:** Autores de los commits, responsables de seguir las convenciones.

- **Revisores/Peer Review:** Validan que los mensajes de commit cumplan con el estándar.

- **DevOps/CI:** Integran hooks y validaciones automáticas en el pipeline.

## 3. Estructura General del Mensaje

Un mensaje de commit bien estructurado facilita la lectura y automatización. Se compone de tres partes:

1. **Línea de título (subject):** Resumen breve del cambio.

2. **Línea en blanco:** Separa el título del cuerpo.

3. **Cuerpo descriptivo (body) opcional:** Detalles adicionales, contexto y pasos de prueba.

### 3.1 Línea de título (subject)

- Máximo 72 caracteres.

- Formato: `<Prefijo>: <Verbo en infinitivo> <objeto>`.

- No terminar con punto.

- Ejemplo: `Code_INVIAS: Refactorizar pipeline de ingestión de PDFs`

### 3.2 Línea en blanco

- Una línea vacía después del título para que Git interprete correctamente el body.

### 3.3 Cuerpo descriptivo (body)

- Extender la descripción si es necesario.

- Escribir en presente o infinitivo.

- Puntos clave:

  - Motivo del cambio.

  - Detalles de implementación.

  - Instrucciones para probar o validar.

  - Referencia a issues: `#123`.

### 3.4 Uso en VS Code

En VS Code, dentro del panel **Source Control** (`Ctrl+Shift+G`), tienes dos formas de redactar tu mensaje de commit siguiendo las convenciones:

#### 3.4.1 Entrada multilinea directa

- **Dónde**: Panel **Source Control** → cuadro de mensaje breve.

- **Cómo**:

1. Haz clic en el cuadro y comienza a escribir la **primera línea** (subject).

2. Cuando necesites explicar detalles, presiona `Shift+Enter` para crear una nueva línea.

3. Continúa escribiendo el **body** directamente debajo del título.

4. Una vez listo, pulsa `Ctrl+Enter` para ejecutar el commit con todas las líneas.

- **Ejemplo**:

  ```plaintext
  Code_INVIAS: Implementar validación de inputs
  
  - Se añade función `validateInputs()` en utils.js.
  - Se crean tests unitarios en validateInputs.test.js.
  - Issue relacionado: #456
  ```

- **Ventajas**:

  - Flujo rápido sin abrir pestañas adicionales.

  - Útil para commits con body corto o puntual.

- **Limitaciones**:

  - Sin realce de sintaxis Markdown ni plantillas.

  - Puede resultar incómodo para bodies extensos.

#### 3.4.2 Uso del editor completo (`COMMIT_EDITMSG`)

1. **Configurar VS Code**:

    - Abre **Configuración** (`Ctrl+,`).

    - Busca **Git: Use Editor As Commit Input** y actívalo (`git.enableCommitInputToplevelEditor`).

    - (Opcional) Desactiva **Git: Show Commit Input** si no quieres el cuadro breve.

2. **Iniciar commit**:

    - En el panel **Source Control**, selecciona cambios y haz clic en **Commit** (o **Commit (Amend)**).

    - VS Code abrirá una nueva pestaña denominada `COMMIT_EDITMSG`.

3. **Redactar el mensaje** en `COMMIT_EDITMSG`:

   1. Primera línea: `<Prefijo>: <Verbo objeto>` (máx. 72 c.).

   2. Deja una línea en blanco.

   3. Escribe el cuerpo:
      - Propósito y contexto del cambio.
      - Detalles de implementación (funciones, archivos modificados).
      - Pasos para reproducir o probar.
      - Referencias a issues o pull requests.

4. **Finalizar**:

    - Guarda el archivo (`Ctrl+S`).

    - Cierra la pestaña.

    - VS Code aplicará el commit con el mensaje completo.

- **Ejemplo de ******`**COMMIT_EDITMSG**`:

  ```plaintext
  AI_Queries: Extender ejemplos de prompts con parámetros
  
  Se incorporan nuevos tests en `prompt_tests.md` que cubren:
  - Prompts con opciones de filtrado.
  - Múltiples escenarios de error.
  - Referencia a pipeline de CI: #789.
  ``` Uso del editor completo (`COMMIT_EDITMSG`)
  ````

#### 3.4.3 Uso en la CLI (dentro y fuera de VSCode)

Con `git commit` o `git commit -m`:

- **Título solamente**:

  ```bash
  git commit -m "AI_Queries: Agregar ejemplos básicos"
  ```

- **Con cuerpo**:

  ```bash
  git commit
  ```

  Git abrirá tu editor predeterminado con **COMMIT_EDITMSG**:

  > 1. Línea de título.
  > 2. Línea vacía.
  > 3. Body descriptivo.

## 4. Convenciones del Título

La línea de título (subject) es la parte más visible del mensaje de commit. Debe ser concisa, uniforme y contener información clave.

### 4.1 Formato general

```plaintext
<Prefijo>: <Verbo en infinitivo> <objeto>
```

- **Prefijo** (obligatorio): Define la naturaleza o el área del cambio.Puede ser un **tipo de commit** estandarizado (como `feat`, `fix`, `docs`, `refactor`) o un **prefijo de contexto** específico del proyecto (p.ej., `AI_Queries`, `Code_INVIAS`, `Code_Example-<etiqueta>_vNN`, `- Minor Edits`, `New Packages`, `Research Deepening`, `Merge branch '...'`, `Package Usage`, `Upgrade`). Este prefijo es clave para la categorización automática y la legibilidad.

- **Dos puntos y espacio** (`:` ) separando prefijo y descripción.

- **Verbo en infinitivo** (imperativo ligero): “Agregar”, “Refactorizar”, “Eliminar”, “Actualizar”, etc.

- **Objeto**: Entidad sobre la que recae la acción (archivo(s), módulo, funcionalidad).

### 4.2 Reglas de estilo

- **Longitud**: Máximo 72 caracteres (ideal entre 50–60).

- **Idioma**: Elegir español o inglés según política del repositorio y mantenerlo consistente.

- **Capitalización**: Sólo la primera palabra y nombres propios en mayúscula; resto en minúscula.

- **Sin punto final** al terminar la línea.

### 4.3 Prefijos estándar

Para estandarizar el historial de commits, usa únicamente estos prefijos:

| Prefijo                       | Descripción breve                                                                                                                                                                                              |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AI_Queries`                  | Commits relacionados con ejemplos, consultas de IA, uso de librerías, documentación de herramientas de IA o investigaciones prácticas sobre temas/modelos de Inteligencia Artificial.                          |
| `Code_INVIAS`                 | Cambios en código fuente del proyecto INVIAS.                                                                                                                                                                  |
| `Code_Example-<etiqueta>_vNN` | Ejemplos de código asociados a video NN con etiqueta.                                                                                                                                                          |
| `- Minor Edits`               | Correcciones menores o ajustes de estilo.                                                                                                                                                                      |
| `New Packages`                | Instalación de nuevas dependencias.                                                                                                                                                                            |
| `Package Usage`               | Ejemplos de uso de librerías o APIs instaladas.                                                                                                                                                                |
| `Upgrade`                     | Actualización de versiones de paquetes o herramientas.                                                                                                                                                         |
| `Research Deepening`          | Documentación, profundización teórica o conceptual del dominio del proyecto, análisis teórico, estudios de viabilidad o análisis de estado del arte o flujo de investigación; no con el desarrollo particular. |
| `Merge branch '...'`          | Mensajes automáticos al fusionar ramas.                                                                                                                                                                        |
| Troubleshoot                  | Commits relacionados con la resolución de errores, depuración o correcciones urgentes.                                                                                                                         |

#### 4.3.1 Tipos de Commit Estándar

Además de los prefijos específicos de área del proyecto, el `<Prefijo>` también puede ser un *tipo de commit* global, alineado con las convenciones de commit para indicar la **intención principal del cambio**.

| Tipo Estándar | Descripción                                                                    |
| :------------ | :----------------------------------------------------------------------------- |
| `feat`        | Introduce una **nueva característica** al código.                              |
| `fix`         | Corrige un **error (bug)** en el código.                                      |
| `docs`        | Cambios **únicamente en la documentación**.                                    |
| `style`       | Ajustes de **formato, espacios en blanco, o estilo** que no cambian la lógica. |
| `refactor`    | Reestructuración de código que **no agrega funcionalidad ni corrige errores**. |
| `test`        | Adición o corrección de **pruebas**.                                           |
| `build`       | Cambios que afectan el **sistema de compilación o dependencias externas**.     |
| `ci`          | Cambios en la **configuración de Integración Continua (CI)**.                 |
| `perf`        | Mejora del **rendimiento** del código.                                         |
| `chore`       | Tareas de mantenimiento que **no modifican el código fuente o pruebas** (ej. actualizaciones de librerías menores). |


### 4.4 Ejemplos de título válidos

- `AI_Queries: Agregar nuevas pruebas de prompts flexible`

- `Code_INVIAS: Refactorizar controlador de rutas en app.js`

- `Code_Example-emlhf_v05: Crear demo de clasificación con Gradio`

- `- Minor Edits: Corregir indentación en README.md`

- `New Packages: Instalar lodash y moment.js`

- * `Troubleshoot: Corregir error de conexión en base de datos`

#### Ejemplos multilinea completos

```plaintext
Code_INVIAS: Implementar sistema de autenticación OAuth2 v2

- Se añade módulo `oauth2.js` en /src/auth/.
- Se configura endpoint `/auth/callback` en server.js.
- Actualizar documentación en AUTH_README.md.
- Asociar issue: #1024.
```

```plaintext
AI_Queries: Extender ejemplos de prompts para clasificación de texto

Se agregan nuevos casos de prueba en `prompt_tests.md`:
- Prompt con parámetro de temperatura alta.
- Escenarios de token truncation.
- Validación de errores de conexión.
Referencia interna: DOC-5678.
```

## 5. Cuerpo descriptivo

El cuerpo (body) de un mensaje de commit ofrece el contexto y los detalles que no caben en la línea de título. Se recomienda usarlo siempre que el cambio sea más que trivial.

### 5.1 Cuándo incluir el cuerpo

- Nuevas funcionalidades o refactorizaciones complejas.

- Correcciones de bugs relevantes.

- Actualizaciones de documentación o configuración que afecten múltiples áreas.

- Cualquier cambio que requiera justificar el motivo o explicar pasos de prueba.

### 5.2 Estructura del cuerpo

1. **Introducción breve** (opcional): Una frase que enmarque el propósito general del cambio.

2. **Detalles de implementación**:

    - Descripción de las funciones, módulos o archivos modificados.

    - Rutas de archivos entre backticks o comillas.

3. **Pasos para probar** (si aplica): Listado numerado o con guiones para reproducir o validar el cambio.

4. **Referencias**:

    - Issues o tickets internos: `#123`, `DOC‑5678`.

    - Pull requests cruzados: `PR #45`.

    - Documentación externa: URLs o claves internas.

### 5.3 Reglas de estilo

- **Linea en blanco** tras el título (subject).

- **Máximo 72 caracteres** por línea en el cuerpo para legibilidad.

- **Presente o infinitivo**: Usar “Agrega”, “Refactoriza” o “Agregar”, “Refactorizar”.

- **Markdown básico**: Listas con `-` o `1.`, fragmentos de código en backticks.

### 5.4 Ejemplos de cuerpos descriptivos

```plaintext
Code_INVIAS: Refactorizar módulo de envío de correos

Se extrae la lógica de plantillas a `mailer/templates.js`:
- Nueva función `renderTemplate()`.
- Actualizar `sendEmail()` para recibir objetos de datos.

Pasos para probar:
1. Ejecutar `npm run test-mailer`.
2. Verificar que los correos simulan datos de prueba.

Issue: #678
```

```plaintext
New Packages: Instalar y configurar ESLint y Prettier

- Se agrega paquete `eslint` y `prettier` en `package.json`.
- Se crea `.eslintrc.json` con reglas base.
- Se define script `lint:fix` en `package.json`.

Para validar:
- Ejecutar `npm run lint`.
- Ejecutar `npm run lint:fix` y confirmar que formatea archivos.
```

## 6. Prompt para formatear commits con IA

A continuación se presenta un **instructivo-prompt** listo para usar en modelos de lenguaje como GPT, Gemini o Claude. El usuario debe proporcionar la descripción bruta de su commit y la IA devolverá un mensaje de commit formateado según este manual. Si falta información clave, la IA solicitará los datos necesarios.

```prompt
Eres un asistente experto en Git y manejo de commits. Formatea las descripciones de commit siguiendo estas convenciones:

1. Línea de título (subject):
   - Formato: `<Prefijo>: <Verbo en infinitivo> <objeto>`
   - Prefijos válidos: feat, fix, docs, style, refactor, test, build, ci, perf, chore, AI_Queries, Code_INVIAS, Code_Example-<etiqueta>_vNN, - Minor Edits, New Packages, Package Usage, Upgrade, Research Deepening, Merge branch '...', Troubleshoot
   - Máximo 72 caracteres, sin punto final, verbo en infinitivo, mayúscula inicial.

2. Cuerpo (body) opcional si la descripción lo requiere:
   - Dejar una línea en blanco tras el título.
   - Incluir motivo, detalles de implementación, pasos de prueba y referencias a issues o documentos internos (`#123`, `DOC-5678`).
   - Máximo 72 caracteres por línea.

**Instrucción al usuario:**
"Proporciona la descripción del commit con al menos el Prefijo, Verbo y Objeto. Si deseas cuerpo, añade detalles separados con un salto de línea." 
```

**Ejemplo de uso:**

- Usuario:

  ```prompt
  "Deseo agregar validación de inputs en utils.js con tests en validateInputs.test.js y asociar issue #456"
  ```

- respuesta de IA:

  ```markdown
  Code_INVIAS: Agregar validación de inputs en utils.js
  
  - Se añade función `validateInputs()` en utils.js.
  - Se crean tests unitarios en validateInputs.test.js.
  - Issue relacionado: #456
  ```

**Manejo de información faltante:**

Si al formatear detectas que falta alguno de los elementos (Prefijo, Verbo en infinitivo, Objeto o detalles para el body), responde con:

> "Por favor, proporciona [elemento faltante], por ejemplo: Prefijo, Verbo en infinitivo, Objeto, motivo o referencias."

## Referencias

- Conventional Commits. (2020). Conventional Commits Specification. https://www.conventionalcommits.org

- Git Documentation. (2025). git-commit Manual. https://git-scm.com/docs/git-commit

- Visual Studio Code Docs. (2025). Commit message editor. https://code.visualstudio.com/docs/editor/versioncontrol#_commit-message-editor

- Obsidian Help. (2025). Front Matter. https://help.obsidian.md/Advanced+topics/Front+Matter