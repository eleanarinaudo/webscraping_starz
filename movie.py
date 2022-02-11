# movie.py
"""Documentacion del modulo movie.py"""

class Movie:
    """Clase usada para describir la Pelicula.

    Parametros
    ----------
    contentId: int
        Id de la Pelicula 
    contentType: str
        Tipo de contenido
    title: str
        Titulo de la Pelicula
    logLine: str
        Sinopsis de la Pelicula
    ratingName: str
        Tipo de Clasificacion
    releaseYear: int
        Anio de lanzamiento
    runtime: int
        Duracion de la pelicula
    """
    def __init__(
        self, contentId, contentType, title, logLine, ratingName, releaseYear, runtime
    ):
        self.contentId = contentId
        self.contentType = contentType
        self.title = title
        self.logLine = logLine
        self.ratingName = ratingName
        self.releaseYear = releaseYear
        self.runtime = runtime
