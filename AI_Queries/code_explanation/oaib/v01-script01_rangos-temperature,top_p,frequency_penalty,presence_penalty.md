A continuación se muestra una tabla con los principales parámetros de generación de texto en la API de OpenAI y sus rangos de valores permitidos (vigentes a junio de 2025):

| Parámetro              | Descripción breve                                                                                                       | Rango de valores permitidos |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| **temperature**        | Controla la aleatoriedad en la selección de tokens. Valores bajos → más determinista; valores altos → más variabilidad. | 0.0 – 2.0                   |
| **top\_p**             | Define el umbral de probabilidad acumulada para nucleus sampling. Filtra los tokens de cola con baja probabilidad.      | 0.0 – 1.0                   |
| **frequency\_penalty** | Penaliza tokens que ya han aparecido según su frecuencia. Valores positivos reducen repeticiones.                       | –2.0 – 2.0                  |
| **presence\_penalty**  | Penaliza la mera presencia previa de un token (sin importar cuántas veces). Valores positivos fomentan palabras nuevas. | –2.0 – 2.0                  |

**Notas adicionales sobre rangos y comportamiento**:

1. **temperature (0.0 – 2.0)**

   * 0.0: selección determinista (siempre token de mayor probabilidad).
   * 0.1 – 0.5: salidas muy “focalizadas”, con poca aleatoriedad.
   * 0.6 – 1.0: balance entre coherencia y diversidad.
   * 1.1 – 2.0: cada vez más creativas o “arriesgadas” (aumenta ruido).

2. **top\_p (0.0 – 1.0)**

   * 0.0 < top\_p < 1.0: activa nucleus sampling. Por ejemplo, top\_p = 0.9 indica “mantén el mínimo conjunto de tokens cuya probabilidad acumulada alcance 90 %”.
   * top\_p = 1.0: equivale a “no filtrar nada por probabilidad acumulada” (se usa todo el vocabulario, sujeto solo a temperatura y penalizaciones).

3. **frequency\_penalty (–2.0 – 2.0)**

   * Valores negativos (ej. –1.0): favorecen repetir tokens que ya han aparecido.
   * 0.0: sin penalización.
   * Valores positivos (ej. 0.5 – 2.0): reducen progresivamente la probabilidad de reaparecer de la misma palabra según cuántas veces apareció.

4. **presence\_penalty (–2.0 – 2.0)**

   * Valores negativos (ej. –1.0): aumentan la probabilidad de volver a introducir tokens ya usados (favorecen repeticiones).
   * 0.0: sin penalización por presencia.
   * Valores positivos (ej. 0.5 – 2.0): penalizan cualquier token que ya apareció, independientemente de cuántas veces, para fomentar vocabulario nuevo.

---

**Ejemplo de combinaciones típicas**:

* Clasificación o análisis determinista:

  * `temperature = 0.0`
  * `top_p = 1.0`
  * `frequency_penalty = 0.0`
  * `presence_penalty = 0.0`

* Conversación balanceada entre coherencia y diversidad:

  * `temperature = 0.7`
  * `top_p = 0.9`
  * `frequency_penalty = 0.2`
  * `presence_penalty = 0.1`

* Generación creativa / narrativa:

  * `temperature = 1.0 – 1.2`
  * `top_p = 0.95`
  * `frequency_penalty = 0.0 – 0.2`
  * `presence_penalty = 0.0 – 0.1`
