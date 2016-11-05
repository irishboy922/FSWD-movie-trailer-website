# Import the media file to access the Movie class
import media
# Import fresh_tomatoes.py file to access open_movies_page function
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "test",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
toy_story.rating = toy_story.VALID_RATINGS[0]

avatar = media.Movie("Avatar",
        "A marine on an alien planet",
        "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
avatar.rating = avatar.VALID_RATINGS[1]


gladiator = media.Movie("Gladiator",
                        "When a Roman general is betrayed and his family "
                        "murdered by an emperor's corrupt son, he comes to"
                        " Rome as a gladiator to seek revenge.",
                        "https://en.wikipedia.org/wiki/File:Gladiator_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")
gladiator.rating = gladiator.VALID_RATINGS[2]

test = media.Movie("Gladiator",
                        "Maximus is then relegated to fighting to the death"
                        " in the gladiator arenas",
                        "https://en.wikipedia.org/wiki/File:Gladiator_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")
test.rating = test.VALID_RATINGS[2]

movies = [toy_story, avatar, gladiator, test]
# print(avatar.rating, toy_story.rating, gladiator.rating)
fresh_tomatoes.open_movies_page(movies)
