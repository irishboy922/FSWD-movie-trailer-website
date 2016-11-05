# Import the media file to access the Movie class
import media
import requests
# Import fresh_tomatoes.py file to access open_movies_page function
import fresh_tomatoes

# Data for all the movies provided by the OMDb API
# Link: https://www.omdbapi.com/
# License: CC BY-NC 4.0.

'''
Function get_data is used to get data from the OMDb API and
return a JSON object.
It takes in one @param: the OMDb API request link
'''


def get_data(json_link):
        # request data from API
    data_request = requests.get(json_link)
    # Trun the data_request into a JSON object
    data = data_request.json()
    # return the data from the collected JSON
    return data


toy_story = media.Movie(get_data("http://www.omdbapi.com/?t=toy+story&y=&plot=short&r=json"),
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
#


avatar = media.Movie(get_data("http://www.omdbapi.com/?t=avatar&y=&plot=short&r=json"),
                     "https://www.youtube.com/watch?v=4KPTXpQehio")


gladiator = media.Movie(get_data("http://www.omdbapi.com/?t=gladiator&y=&plot=short&r=json"),
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")


movies = [toy_story, avatar, gladiator]
# print(avatar.rating, toy_story.rating, gladiator.rating)

fresh_tomatoes.open_movies_page(movies)
