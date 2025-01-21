```markdown
EN NINGUN EJEMPLO DE LOS QUE ME PRESENTÓ SE EXTRAJO METADATOS
```
Tienes toda la razón, pido disculpas por el error. En los ejemplos anteriores, no se extrajeron los metadatos de manera correcta.

Aquí te presento una forma correcta de extraer metadatos utilizando **PyPDF2** y cómo integrarlo con el ejemplo de **PDFMiner** que sí extrae texto correctamente:

### Extracción de Metadatos con PyPDF2 (Corregido)

```python
import PyPDF2

def extraer_metadatos_con_pypdf2(pdf_path):
    """Extrae metadatos de un archivo PDF usando PyPDF2."""
    metadatos = {}
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        metadata = pdf_reader.metadata
        if metadata:
            metadatos['autor'] = metadata.get('/Author', '')
            metadatos['creador'] = metadata.get('/Creator', '')
            metadatos['productor'] = metadata.get('/Producer', '')
            metadatos['titulo'] = metadata.get('/Title', '')
            metadatos['fecha_creacion'] = metadata.get('/CreationDate', '')
            metadatos['fecha_modificacion'] = metadata.get('/ModDate', '')
    return metadatos

# Ejemplo de uso
pdf_path = 'ejemplo.pdf'  # Reemplaza con la ruta a tu PDF
metadatos_extraidos = extraer_metadatos_con_pypdf2(pdf_path)
print(metadatos_extraidos)
```

**Explicación del código corregido:**

*   Importamos `PyPDF2`.
*   Abrimos el archivo PDF en modo lectura binaria (`'rb'`).
*   Creamos un objeto `PdfReader`.
*   Accedemos a los metadatos a través de la propiedad `pdf_reader.metadata`.
*   Extraemos los campos comunes de los metadatos como autor, creador, productor, título y fechas de creación/modificación, usando el método `get()` para evitar errores si un campo no está presente.
*   Devolvemos un diccionario con los metadatos extraídos.

### Integración con el ejemplo de PDFMiner

Como mencioné anteriormente, PDFMiner no extrae metadatos directamente. Sin embargo, podemos combinar `PyPDF2` (para metadatos) con `PDFMiner` (para texto) de la siguiente manera:

```python
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import PyPDF2

def extraer_texto_y_metadatos(pdf_path):
    """Extrae texto y metadatos de un archivo PDF usando PDFMiner y PyPDF2."""
    texto = extract_text(pdf_path, laparams=LAParams())
    metadatos = extraer_metadatos_con_pypdf2(pdf_path)
    return texto, metadatos

# Ejemplo de uso
pdf_path = 'ejemplo.pdf'  # Reemplaza con la ruta a tu PDF
texto_extraido, metadatos_extraidos = extraer_texto_y_metadatos(pdf_path)

print("Texto extraído:\n", texto_extraido)
print("\nMetadatos extraídos:\n", metadatos_extraidos)
```

**Explicación de la integración:**

*   Importamos las funciones necesarias de `pdfminer.six` y `PyPDF2`.
*   Definimos una función `extraer_texto_y_metadatos` que utiliza `extract_text` de `pdfminer.six` para extraer el texto y `extraer_metadatos_con_pypdf2` para extraer los metadatos.
*   Devolvemos tanto el texto como los metadatos.

Ahora sí, con estos ejemplos corregidos, tienes una forma fiable de extraer metadatos junto con el texto y las tablas de tus PDFs.

**¿Te gustaría que continuemos con el preprocesamiento del texto usando PLN o tienes alguna otra duda sobre la extracción de datos?**
