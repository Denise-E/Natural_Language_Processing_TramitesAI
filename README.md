# Natural_Language_Processing_TramitesAI
 Processamiento de Lenguaje Natural con TensorFlow y SpaCy en python, para BDT Global.

## Requisitos

- Python 3.11
- pip (Administrador de paquetes de Python)

## Configuración del Entorno de Desarrollo
Para este proyecto, utilizar la consola Command Prompt para correr los siguientes comandos.

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

### Paso 2: Levantar el proyecto de Flask

```command prompt
flask run
```
Para que el servidor recargue automáticamente cuando se realicen cambios en el código, se lo puede correr con el siguiente comando: 

```command prompt
flask run --reload
```

### Documentación

La documentación del proyecto está disponible en la ruta /swagger. Puedes acceder a ella navegando a http://localhost:5000/swagger una vez que el servidor esté en funcionamiento.

### Descripción del Proyecto

Este proyecto utiliza la biblioteca **Pandas** para la obtención de datos a partir de archivos CSV y luego **TensorFlow** para la creación de modelos PLN (Procesamiento de Lenguaje Natural). Además, se utiliza **SpaCy** para la creación de modelos NER (Reconocimiento de Entidades Nombradas).

**Pandas** es una biblioteca que proporciona estructuras de datos de alto rendimiento y herramientas de análisis de datos, mientras que **TensorFlow** es una plataforma de código abierto para el aprendizaje automático desarrollada por Google. **SpaCy** es una biblioteca de procesamiento de lenguaje natural de código abierto diseñada para la producción de software.
