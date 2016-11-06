# Import the media file to access the Movie class
import media
# Import Requests library to use for api data requests
import requests
# Import fresh_tomatoes.py file to access open_movies_page function
import fresh_tomatoes

# Data for all the movies provided by the OMDb API
# Link: https://www.omdbapi.com/
# License: CC BY-NC 4.0.


def get_data(json_link):
    """
    Fetches data from the OMDb API.

    Args:
        json_link: the OMDb API request link

    Returns:
        A JSON object containing all the data needed for
        the Movie instances.

    """
    try:
        # request data from API
        data_request = requests.get(json_link)
        # Trun the data_request into a JSON object
        data = data_request.json()
    except requests.exceptions.RequestException as err:
        # If error loading data print error message.
        print err
    # return the data from the collected JSON
    return data


# Toy Story instance of Movie class
toy_story = media.Movie(get_data("http://www.omdbapi.com/?t=toy+story&y=&plot=short&r=json"),  # NOQA
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

# Gladiator instance of Movie class
gladiator = media.Movie(get_data("http://www.omdbapi.com/?t=gladiator&y=&plot=short&r=json"),  # NOQA
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")

# Shawshank Redemption instance of Movie class
shawshank = media.Movie(get_data("http://www.omdbapi.com/?t=shawshank&y=&plot=short&r=json"),  # NOQA
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

# The Godfather instance of Movie class
godfather = media.Movie(get_data("http://www.omdbapi.com/?t=the+godfather&y=&plot=short&r=json"),  # NOQA
                        "https://www.youtube.com/watch?v=sY1S34973zA")

# Inception instance of Movie class
inception = media.Movie(get_data("http://www.omdbapi.com/?t=inception&y=&plot=short&r=json"),  # NOQA
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

# Snatch instance of Movie class
snatch = media.Movie(get_data("http://www.omdbapi.com/?t=snatch&y=&plot=short&r=json"),  # NOQA
                     "https://www.youtube.com/watch?v=ni4tEtuTccc")

# Boondock Saints instance of Movie class
boondock_saints = media.Movie(get_data("http://www.omdbapi.com/?t=boondock+saints&y=&plot=short&r=json"),  # NOQA
                              "https://www.youtube.com/watch?v=VoRrQiORYck")

# A Beautiful Mind instance of Movie class
a_beautiful_mind = media.Movie(get_data("http://www.omdbapi.com/?t=a+beautiful+mind&y=&plot=short&r=json"),  # NOQA
                               "https://www.youtube.com/watch?v=WFJgUm7iOKw")

# Matrix instance of Movie class
matrix = media.Movie(get_data("http://www.omdbapi.com/?t=the+matrix&y=&plot=short&r=json"),  # NOQA
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Saving Private Ryan instance of Movie class
saving_private_ryan = media.Movie(get_data("http://www.omdbapi.com/?t=saving+private+ryan&y=&plot=short&r=json"),  # NOQA
                                  "https://www.youtube.com/watch?v=zwhP5b4tD6g")  # NOQA

# American History X instance of Movie class
american_history_x = media.Movie(get_data("http://www.omdbapi.com/?t=american+history+x&y=&plot=short&r=json"),  # NOQA
                                 "https://www.youtube.com/watch?v=XfQYHqsiN5g")

# The Green Mile instance of Movie class
green_mile = media.Movie(get_data("http://www.omdbapi.com/?t=green+mile&y=&plot=short&r=json"),  # NOQA
                         "https://www.youtube.com/watch?v=Ki4haFrqSrw")

# Braveheart instance of Movie class
braveheart = media.Movie(get_data("http://www.omdbapi.com/?t=braveheart&y=&plot=short&r=json"),  # NOQA
                         "https://www.youtube.com/watch?v=wj0I8xVTV18")

# Good Will Hunting instance of Movie class
good_will_hunting = media.Movie(get_data("http://www.omdbapi.com/?t=good+will+hunting&y=&plot=short&r=json"),  # NOQA
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")

# An array of the Movie instances
movies = [good_will_hunting, gladiator, shawshank, godfather, inception,
          snatch, boondock_saints, a_beautiful_mind, matrix,
          saving_private_ryan, american_history_x, green_mile,
          braveheart, toy_story]

# Execute the open_movies_page function
fresh_tomatoes.open_movies_page(movies)
