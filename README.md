# Web Scraping en Starz con Python

El proyecto realizado demuestra cómo realizar Web Scraping de la página [Starz](https://www.starz.com/ar/es/) utilizando Python, extrayendo y guardando la metadata de cada contenido de todas las películas y series en un archivo `json` o `csv` . 

Para Web scraping utilizamos la librería `BeatifulSoup`

## Objetivo
Los objetivos a realizar son los siguientes: 
- Obtener todas las películas y series
- Obtener la metadata de cada contenido: título, año, sinopsis, link, duración (solo para movies)
- Guardar la información obtenida en una base de datos, en archivo .json o .csv automáticamente
- PLUS: Episodios de cada serie
- PLUS: Metadata de los episodios
- PLUS: Si es posible obtener mas información/metadata por cada contenido
- PLUS: Identificar modelo de negocio

## Antes de empezar

Primero, clonamos nuestro repositorio 

```bash
git clone https://github.com/eleanarinaudo/webscraping_starz.git
```
Desde el directorio que se creó, instalamos y creamos el entorno virtual (en Windows)

```bash
pip install virtualenv
```

```bash
python -m venv webscraping-starz
```

Luego, activamos el entorno virtual
```bash
.\webscraping-starz\Script\activate
```

## Requisitos previos

Necesitarás instalar

- Python 3.x

## Instalación de paquetes necesarios

Las librerías que se instalarán en el entorno virtual son:

- Request: Requests es la única libreria HTTP para Python
- Pandas: librería para análisis de datos de Python
- lxml: librería para procesar XML y HTML
- BeatifulSoup4: Librería para extraer datos de archivos HTML y XML


Se instalarán con la siguiente línea en la Terminal:

```bash 
pip install -r requirements.txt
```

# Proyecto

En el repositorio, se encuentran los `módulos`, `scripts` y la extracción de los datos en `json` y `csv`.

>Los módulos son:
>```python
>movie.py
>```
>
>```python
>serie.py
>```
>En estos módulos, se encuentran las clases con >su correspondiente documentación: 
>
>```python
>class Movie
>```
>
>```python
>class Serie
>```

>El `Script` ha ejecutar en la terminal es:
>```bash
>py main.py
>```

>Una vez ejecutado el `Script`, se obtienen las bases de datos en `csv` y `json` en sus correspondientes directorios.
>```bash
>+---csv
>|       Movie.csv
>|       Serie.csv
>|       
>+---json
>|       Movie.json
>|       Serie.json
>```

## Analisis de negocio

STARZ es un servicio de streaming para ver series, películas y más. 
Donde puede ver las temporadas actuales y pasadas de series originales de STARZ, las mejores películas de hoy y otros de sus contenidos favoritos donde, cuando y como quiera.
Puede verlo en una computadora o descargarlo a un teléfono inteligente o tableta y comenzar a obsesionarse.

Como STARZ, hay otros servicios de streaming que están disponibles para comprarse por un plan de membresía, en lugar de la manera antigua de uno en uno. 
El plan de membresía puede tener diferentes modalidades. 
Esto hace que los clientes tengan la sensación de experimentar con un modelo de suscripción.












