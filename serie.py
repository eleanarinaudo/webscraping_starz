class Serie:
    def __init__(
        self,
        title,
        contentId,
        contentType,
        logLine,
        episodeCount,
        genres,
        minReleaseYear,
        maxReleaseYear,
        ratingCode,
    ):
        self.title = title
        self.contentType = contentType
        self.contentId = contentId
        self.logline = logLine
        self.episodeCount = episodeCount
        self.genres = genres
        self.maxReleaseYear = maxReleaseYear
        self.minReleaseYear = minReleaseYear
        self.ratingCode = ratingCode
