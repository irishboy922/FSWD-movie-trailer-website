class Movie():
    """
    Class used to assign movie data from the
    OMDb API for each movie instance of Class.

    Attributes:
        data: Json data object form the OMDb API request
        trailer_youtube: URL link to the youtube trailer
    """

    def __init__(self,
                 data,
                 trailer_youtube):
        """ Inits Movie class with title, storyline, poster image,
        trailer url, movie rating, and IMDB review score.
        """
        self.title = data["Title"]
        self.storyline = data["Plot"]
        self.poster_image_url = data["Poster"]
        self.trailer_youtube_url = trailer_youtube
        self.rating = data["Rated"]
        self.review = data["imdbRating"]
