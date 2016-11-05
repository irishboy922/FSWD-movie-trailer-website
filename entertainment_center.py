import media
# import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "test",
                        "https://en.wikipedia.org/wiki/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

# print(toy_story.title)

avatar = media.Movie("Avatar",
        "A marine on an alien planet",
        "https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")


# avatar.show_trailer()

gladiator = media.Movie("Gladiator",
                        "Maximus is then relegated to fighting to the death"
                        " in the gladiator arenas",
                        "https://en.wikipedia.org/wiki/File:Gladiator_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")

# gladiator.show_trailer()
movies = [toy_story, avatar, gladiator]

# fresh_tomatoes.open_movies_page(movies)
print(gladiator.VALID_RATINGS[0])
