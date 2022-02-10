from movie import Movie
from serie import Serie
from bs4 import BeautifulSoup
import requests
import pandas as pd


def movieList():
    res = requests.get(REQ_URL + movie_path)
    soup = BeautifulSoup(res.text, "lxml")
    list_m = soup.find("p").text
    movies = eval(list_m)
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
        movies_list_df = pd.DataFrame(movies_list)

    print(movies_list_df)
    movies_list_df.to_csv(movie_csv, encoding="utf-8")
    movies_list_df.to_json(movie_json, orient = 'index')

    return movies_list_df


def serieList():
    res = requests.get(REQ_URL + serie_path)
    soup = BeautifulSoup(res.text, "lxml")
    listS = soup.find("p").text
    series = eval(listS)

    serie_link = list()

    for i in series["playContentArray"]["playContents"]:
        serie = {
            "Título": i["title"],
            "Tipo": i["contentId"],
            "ID_Serie": i["contentType"],
            "Link": BASE_URL
            + "series/"
            + i["title"].replace(" ", "-")
            + "/"
            + str(i["contentId"]),
            "Sinopsis": i["logLine"],
            "CantidadEpisodios": i["episodeCount"],
            "Genero": i["genres"],
            "Año Lanzamiento": i["minReleaseYear"],
            "Actual o Finalizado": i["maxReleaseYear"],
            "Calificación": i["ratingCode"],
        }
        serie_link.append(serie)
        series_list_df = pd.DataFrame(serie_link)

    print(series_list_df)
    series_list_df.to_csv(serie_csv, encoding="utf-8")
    series_list_df.to_json(serie_json, orient = 'index')

    return series_list_df


if __name__ == "__main__":
    BASE_URL = "https://www.starz.com/ar/es/"
    REQ_URL = (
        "https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?"
    )

    movie_path = "includes=contentId,contentType,title,logLine,ratingName,releaseYear,runtime&contentType=Movie"
    serie_path = "includes=contentId, contentType,title, logLine, episodeCount,genres,minReleaseYear,maxReleaseYear,ratingCode&contentType=Series"

    movie_csv = "csv/Movie.csv"
    movie_json = "json/Movie.json"
    movieList()
    serie_csv = "csv/Serie.csv"
    serie_json = "json/Serie.json"
    serieList()
    
