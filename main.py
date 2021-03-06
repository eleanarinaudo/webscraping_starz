#Importamos la Librerias
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json


def movieList():
    """
    Extrae los datos de las Peliculas
    y los guarda en .csv y .json
    """

    #Haremos el request a esa ruta
    res = requests.get(REQ_URL + MOVIE_PATH)

    #Procesamos el HTML mediante BeautifulSoap
    soup = BeautifulSoup(res.text, "lxml")
    
    list_m = soup.find("p").text
    movies = json.loads(list_m)
    movies_list = list()

    for i in movies["playContentArray"]["playContents"]:
        movie = {
            "ID_Pelicula": i["contentId"],
            "Tipo": i["contentType"],
            "Título": i["title"],
            "Link": BASE_URL
            + "movies/"
            + i["title"].replace(" ", "-")
            + "-"
            + str(i["contentId"]),
            "Sinopsis": i["logLine"],
            "Calificación": i["ratingName"],
            "Lanzamiento": i["releaseYear"],
            "Duración [MIN]": i["runtime"] // 60,
        }
        movies_list.append(movie)

    # Creacion de DataFrame
    movies_list_df = pd.DataFrame(movies_list)

    # Creacion de CSV
    movies_list_df.to_csv(MOVIE_CSV, encoding="utf-8")
    # Creacion de JSON
    movies_list_df.to_json(MOVIE_JSON, orient="index")

    # DataFrame de Peliculas  
    print(movies_list_df)
    return movies_list_df


def serieList():
    """
    Extrae los datos de las Series
    y los guarda en .csv y .json
    """
    res = requests.get(REQ_URL + SERIE_PATH)
    soup = BeautifulSoup(res.text, "lxml")
    listS = soup.find("p").text
    series = json.loads(listS)

    serie_list = list()
    episodes_list = list()

    for i in series["playContentArray"]["playContents"]:
        serie = {
            "Título": i["title"],
            "ID_Serie": i["contentId"],
            "Tipo": i["contentType"],
            "Link": BASE_URL
            + "series/"
            + i["title"].replace(" ", "-")
            + "/"
            + str(i["contentId"]),
            "Sinopsis": i["logLine"],
            "Genero": [gen["description"] for gen in i["genres"]],
            "CantidadEpisodios": i["episodeCount"],
            "Año Lanzamiento": i["minReleaseYear"],
            "Actual o Finalizado": i["maxReleaseYear"],
            "Calificación": i["ratingCode"],
        }
        serie["Genero"] = ", ".join(serie["Genero"])
        serie_list.append(serie)
    

        for season in i["childContent"]:
            for i, episode in enumerate(season["childContent"]):
                episodes = {
                    "Serie": serie["Título"],
                    "Titulo": episode["title"],
                    "Temporada": season["title"],
                    "Número": i + 1,
                    "Clasificacion": episode["ratingCode"],
                    "Sinopsis": episode["logLine"],
                    "Genero": [gen["description"] for gen in episode["genres"]],
                }
                episodes["Genero"] = ", ".join(episodes["Genero"])
                episodes_list.append(episodes)

    # Creacion de DataFrame
    series_list_df = pd.DataFrame(serie_list)
    episodes_list_df = pd.DataFrame(episodes_list)
    
    # Creacion de CSV
    series_list_df.to_csv(SERIE_CSV, encoding="utf-8")
    episodes_list_df.to_csv(SEASONS_CSV, encoding="utf-8")

    # Creacion de JSON
    series_list_df.to_json(SERIE_JSON, orient="index")
    episodes_list_df.to_json(SEASONS_JSON, orient="index")

    # DataFrame de Series    
    print(series_list_df)
    print(episodes_list_df)

    return series_list_df


if __name__ == "__main__":
    BASE_URL = "https://www.starz.com/ar/es/"
    REQ_URL = (
        "https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?"
    )

    MOVIE_PATH = "includes=contentId,contentType,title,logLine,ratingName,releaseYear,runtime&contentType=Movie"
    SERIE_PATH = "includes=contentId, contentType,title,logLine,episodeCount,genres,minReleaseYear,maxReleaseYear,ratingCode,childContent&contentType=Series"

    MOVIE_CSV = "csv/Movie.csv"
    MOVIE_JSON = "json/Movie.json"
    movieList()

    SERIE_CSV = "csv/Serie.csv"
    SERIE_JSON = "json/Serie.json"

    SEASONS_CSV = "csv/Temporadas.csv"
    SEASONS_JSON = "json/Temporadas.json"
    serieList()
