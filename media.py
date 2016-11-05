

class Movie():

    def __init__(self,
                 data,
                 trailer_youtube):

        # Create variables for each Class instance
        self.title = data["Title"]
        self.storyline = data["Plot"]
        self.poster_image_url = data["Poster"]
        self.trailer_youtube_url = trailer_youtube
        self.rating = data["Rated"]
        self.review = data["imdbRating"]
