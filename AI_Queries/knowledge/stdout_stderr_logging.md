# 🗃️ Registro de salida y errores en Bash: `stdout`, `stderr` y redirecciones

Cuando ejecutamos comandos en una terminal Bash, los resultados pueden clasificarse en dos tipos de salida:

* `1` = **stdout** (*standard output*): es la **salida estándar** del comando, que representa los mensajes normales, como confirmaciones, listas o resultados esperados.
* `2` = **stderr** (*standard error*): es la **salida de error**, que contiene advertencias o fallos ocurridos durante la ejecución.
* `>` = **operador de redirección**: permite enviar una salida a un archivo en lugar de mostrarla en la terminal.

---

### 🎯 Redirección básica

Usamos `>` y `2>` para redirigir cada tipo de salida por separado:

```bash
comando > archivo_salida.txt        # redirige solo stdout
comando 2> archivo_errores.txt      # redirige solo stderr
```

Esto permite registrar por separado los mensajes informativos y los errores del comando.

---

### 🔁 Redirección combinada: `2>&1`

El operador `2>&1` significa:

> Redirigir la salida de errores (`stderr`, descriptor `2`) al mismo destino que la salida estándar (`stdout`, descriptor `1`).

Se utiliza cuando queremos **unificar ambas salidas en un solo archivo**:

```bash
comando > todo.txt 2>&1
```

Esto es útil cuando deseamos tener un único archivo de log con toda la información generada por el comando, tanto exitosa como de errores.

---

### 🧪 Redirección a archivos separados (recomendado para debugging)

Una práctica más organizada y técnica es separar la salida estándar y los errores en dos archivos distintos:

```bash
comando > salida.txt 2> errores.txt
```

Así obtenemos:

* `salida.txt`: contiene solo mensajes informativos (`stdout`)
* `errores.txt`: contiene únicamente advertencias y errores (`stderr`)

Esto facilita la depuración y permite analizar errores sin mezclar la salida útil.

---

### 📁 Aplicación práctica: instalación de paquetes en `emlhf`

Para registrar detalladamente el resultado de la instalación de paquetes en tu curso, puedes usar esta estructura:

```bash
mkdir -p ../Installed_packages/logs

pip install tensorflow \
  > ../Installed_packages/logs/tensorflow_stdout.txt \
  2> ../Installed_packages/logs/tensorflow_stderr.txt
```

Este enfoque:

* Crea una carpeta de logs si no existe.
* Guarda los mensajes informativos en `tensorflow_stdout.txt`.
* Guarda cualquier error o advertencia en `tensorflow_stderr.txt`.

Esto garantiza trazabilidad, facilita la revisión de errores, y mantiene tus entornos reproducibles y documentados, cumpliendo buenas prácticas de trabajo en proyectos de Machine Learning.

---

¿Te gustaría que lo agregue al archivo `emlhf.md` bajo una sección como `"🧩 Buenas prácticas de instalación y logging"` o prefieres que espere a que lo hagas tú directamente?
