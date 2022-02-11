# serie.py
"""Documentacion del modulo serie.py"""


class Serie:
    """Clase usada para describir la Serie.

    Parametros
    ----------
    title: str
        Titulo de la Serie
    contentId: int
        Id de la Pelicula
    contentType: str
        Tipo de contenido
    logLine: str
        Sinopsis de la Serie
    ratingName: str
        Tipo de Clasificacion
    episodeCount: int
        Cantidad total de Episodios
    maxReleaseYear: int
        Lanzamiento de la Serie
    minReleaseYear: int
        Año de la finzalizacion de la Serie
    ratingCode:
        Tipo de Clasificacion
    """

    def __init__(
        self,
        title,
        contentId,
        contentType,
        logLine,
        episodeCount,
        minReleaseYear,
        maxReleaseYear,
        ratingCode,
    ):
        self.title = title
        self.contentType = contentType
        self.contentId = contentId
        self.logline = logLine
        self.episodeCount = episodeCount
        self.maxReleaseYear = maxReleaseYear
        self.minReleaseYear = minReleaseYear
        self.ratingCode = ratingCode
