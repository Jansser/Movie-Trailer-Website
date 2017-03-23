import media
import fresh_tomatoes

def get_movies():
    # Create the list of my favorites movies
    southpaw = media.Movie("Southpaw",
                           "As tragedy strikes him in his prime, famed boxer, B"
                           "illy Hope, begins to fall into a great depression. "
                           "Once the decision regarding the custody of his daug"
                           "hter is under question, Billy decides to get his li"
                           "fe back on track by getting back into the ring.",
                           "https://upload.wikimedia.org/wikipedia/en/8/89/Southpaw_poster.jpg",
                           "https://www.youtube.com/watch?v=Mh2ebPxhoLs")

    man_on_fire = media.Movie("Man on Fire",
                              "In Mexico City, a former assassin swears vengean"
                              "ce on those who committed an unspeakable act aga"
                              "inst the family he was hired to protect.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/e/e8/Man_on_fireposter.jpg/220px-Man_on_fireposter.jpg",
                              "https://www.youtube.com/watch?v=g4kLizDXLY0")

    deadpool = media.Movie("Deadpool",
                           "A fast-talking mercenary with a morbid sense of hum"
                           "or is subjected to a rogue experiment that leaves h"
                           "im with accelerated healing powers and a quest for "
                           "revenge.",
                           "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                           "https://www.youtube.com/watch?v=gtTfd6tISfw")

    toy_story = media.Movie("Toy Story",
                            "A cowboy doll is profoundly threatened and jealous"
                            " when a new spaceman figure supplants him as top t"
                            "oy in a boy's room.",
                            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    pulp_fiction = media.Movie("Pulp Fiction",
                               "The lives of two mob hit men, a boxer, a gangst"
                               "er's wife, and a pair of diner bandits intertwi"
                               "ne in four tales of violence and redemption.",
                               "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                               "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

    avengers = media.Movie("Avengers",
                           "Earth's mightiest heroes must come together and lea"
                           "rn to fight as a team if they are to stop the misch"
                           "ievous Loki and his alien army from enslaving human"
                           "ity.",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

    return [man_on_fire, deadpool, southpaw, toy_story, pulp_fiction, avengers]

movies = get_movies()

# Create and open the web page
fresh_tomatoes.open_movies_page(movies)