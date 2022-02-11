# Web Scraping en Starz con Python


El proyecto realizado demuestra cómo realizar Web Scraping de la página [Starz](https://www.starz.com/ar/es/) utilizando Python. Extrayendo y guardando la metadata de todas las películas y series en un archivo `json` o `csv` . 

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

En el repositorio, se encuentran el `script` y la extracción de los datos en `json` y `csv`.


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

STARZ es un servicio de streaming para ver series, películas y más. Donde puede ver las temporadas actuales y pasadas de series originales de STARZ, donde, cuando y como quiera. 
Puede verlo desde una computadora o descargarlo en un smartphone o tablet.

Como STARZ, hay otros servicios de streaming que permite acceder a contenidos de audio, video o ambos a través de internet, de manera ubicua y on-demand, 
sin la necesidad de descargarlos en el dispositivo. 
Han surgido diferentes modelos de negocio que buscan monetizar esa provisión audiovisual directa al consumidor.

El usuario obtiene de manera “gratuita” el acceso a los contenidos, pero estos contienen inserciones de publicidad en las que el proveedor obtiene ingresos a partir de colocar anuncios de publicitarios que deseen dar a conocer sus productos a las audiencias.

Otra forma de generar ingreso es el modelo de suscripción,
que están disponible para comprarse por un plan de membresía. 
Y el plan de membresía puede tener diferentes modalidades. Esto hace que los clientes tengan la sensación de experimentación con un modelo de suscripción. 

Hoy las audiencias cuentan con una oferta abundante de plataformas de streaming y una competencia férrea por mantenerse entre sus preferencias.












