# Natural_Language_Processing_TramitesAI
 Processamiento de Lenguaje Natural con TensorFlow en python, para BDT Global

## Requisitos

- Python 3.11
- pip (Administrador de paquetes de Python)

## Configuración del Entorno de Desarrollo

### Paso 1: Crear y Activar el Entorno Virtual

En todos los sistemas operativos:

``` command prompt
python -m venv venv

o

py -m venv venv

El segundo "venv" es el nombre que uno decide ponerle al entorno virtual, se acostumbra a usar venv o env.
```

Para activar el entorno virtual en Windows:

``` command propmt
venv\Scripts\activate
```

Para activar el entorno virtual en macOS/Linux:

```bash
source venv/bin/activate
```
Una vez activado se debe ver (venv) o el nombre que le hayan puesto al enotorno a la izquierda de la ubicación de la carpeta
### Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar el Proyecto

### Paso 1: Navegar al Directorio del Proyecto

```bash
cd ruta/Natural_Language_Processing_TramitesAI
```

### Paso 2: Ejecutar el Archivo `main.py`

```bash
python main.py 

o

py main.py
```

### Descripción del Proyecto

Este proyecto utiliza la biblioteca **Pandas** para la obtención de datos a partir de archivos CSV y luego **TensorFlow** para la creación de modelos de procesamiento de lenguaje natural. 

**Pandas** es una biblioteca que proporciona estructuras de datos de alto rendimiento y herramientas de análisis de datos, mientras que **TensorFlow** es una plataforma de código abierto para el aprendizaje automático desarrollada por Google.
