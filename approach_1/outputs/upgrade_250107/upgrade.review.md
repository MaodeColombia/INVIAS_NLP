# Documentación de Actualización de Paquetes con `pip`

Este documento describe los comandos utilizados y las acciones realizadas para actualizar y resolver conflictos de paquetes en un entorno virtual de Python.

---

## 1. **Listar Paquetes Desactualizados**

Se generó una lista de los paquetes desactualizados presentes en el entorno virtual y se guardó en un archivo para referencia futura:

```bash
pip list --outdated > 250117-090700_outdated.md
```

- **Salida**: Se generó el archivo `250117-090700_outdated` que contiene la lista de paquetes desactualizados.

---

## 2. **Actualizar Paquetes Automáticamente**

Se ejecutó un comando para actualizar automáticamente todos los paquetes desactualizados:

```bash
pip list --outdated --format=columns | awk '{if (NR>2) print $1}' | xargs -n1 pip install -U
```

- **Descripción**:
  - `pip list --outdated --format=columns`: Lista los paquetes desactualizados en formato de columnas.
  - `awk '{if (NR>2) print $1}'`: Ignora las dos primeras líneas (encabezado) y extrae los nombres de los paquetes.
  - `xargs -n1 pip install -U`: Actualiza cada paquete a la última versión disponible.

---

## 3. **Verificar Conflictos de Dependencias**

Se utilizó el siguiente comando para verificar si había conflictos de dependencias entre los paquetes instalados:

```bash
pip check
```

- **Resultado**: Se identificaron los siguientes conflictos:
  - `fastapi` requería una versión específica de `starlette`.
  - `torch` requería una versión específica de `sympy`.

---

## 4. **Resolver Conflictos de Dependencias**

### **4.1. Resolver conflicto entre `fastapi` y `starlette`**

Para solucionar este conflicto, se instaló una versión específica de `starlette`:

```bash
pip install starlette==0.41.0
```

### **4.2. Resolver conflicto entre `torch` y `sympy`**

Para solucionar este conflicto, se instaló una versión específica de `sympy`:

```bash
pip install sympy==1.13.1
```

---

## 5. **Actualizar Paquetes Respetando Dependencias Existentes**

Se ejecutó el siguiente comando para actualizar los paquetes restantes sin causar nuevos conflictos:

```bash
pip install --upgrade --upgrade-strategy only-if-needed
```

- **Descripción**: Este comando actualiza únicamente los paquetes que lo necesitan, respetando las dependencias ya instaladas.

---

## Resultados Finales

- Todos los paquetes desactualizados fueron actualizados exitosamente.
- Los conflictos de dependencias detectados con `pip check` fueron resueltos manualmente instalando versiones específicas de los paquetes involucrados.
- El entorno virtual quedó limpio y funcional tras eliminar directorios temporales y conflictos.

---

**Fecha de documentación:** 16 de enero de 2025
