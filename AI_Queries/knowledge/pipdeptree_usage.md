---
title: Uso de pipdeptree en Git Bash
tags:
  - gitbash
---
# Uso de `pipdeptree` en Git Bash

A continuación tienes los comandos básicos para instalar, actualizar y usar **pipdeptree** en tu entorno de Git Bash.

## 1. Instalar `pipdeptree`

```bash
# Usando pip
pip install pipdeptree
```

```bash
# O, si usas pip3
pip3 install pipdeptree
```

## 2. Actualizar `pipdeptree`

```bash
# Actualiza a la última versión disponible
pip install --upgrade pipdeptree
```

## 3. Mostrar árbol de dependencias de todo el entorno

```bash
# Muestra en formato texto el árbol completo
pipdeptree
```

## 4. Inspeccionar dependencias de un paquete específico

```bash
# Reemplaza <nombre_paquete> por el paquete deseado
pipdeptree -p <nombre_paquete>
```

## 5. Salida en formato JSON

```bash
# Genera salida JSON para procesarla con otras herramientas
pipdeptree --json
```

## 6. Generar gráfico con Graphviz

> **Requisitos:** Tener instalado `graphviz` en tu sistema.

```bash
# Genera un archivo PNG con el gráfico de dependencias
pipdeptree --graph-output png > dependencies.png

# Para salida en DOT (texto)
pipdeptree --graph-output dot > dependencies.dot
```

## 7. Opciones útiles adicionales

```bash
# Incluir paquetes “desnudos” (sin dependencias hijas)
pipdeptree --warn silence

# Mostrar dependencias inversas (qué paquetes dependen de uno dado)
pipdeptree --reverse --packages <nombre_paquete>
```

> **Tip Obsidian**: Puedes incrustar el gráfico generado (`dependencies.png`) en tus notas usando:
> ```markdown
> ![[dependencies.png]]
> ```

## Referencias

1. [pipdeptree en PyPI](https://pypi.org/project/pipdeptree/)  
2. [Repositorio oficial de pipdeptree en GitHub](https://github.com/tox-dev/pipdeptree)
