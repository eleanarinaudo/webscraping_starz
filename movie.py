class Movie:
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
