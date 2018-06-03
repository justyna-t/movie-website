import fresh_tomatoes
import media

# First step is to make instances of class Movie with 4 arguments: Movie name,
# movie description, image url, youtube trailer url.
# Then we make list with all this instances and use it as argument to call
# function open_movies_page() from module fresh_tomatoes which we import above.
story = "A group of NASA scientists discovered a space-time tunnel " + \
        "that allows to interstellar travel."
poster = "https://upload.wikimedia.org/wikipedia/en/b/bc/" + \
         "Interstellar_film_poster.jpg"
trailer = "https://youtu.be/-gieJQejbHQ"
interstellar = media.Movie("Interstellar", story, poster, trailer)

little_prince = media.Movie("The Little Prince", "The Aviator introduces the" +
                            " girl to an extraordinary world where anything "
                            "is possible, the world of the Little Prince",
                            "https://upload.wikimedia.org/wikipedia/en/1/" +
                            "1a/The_Little_Prince_%282015_film%29_poster.png",
                            "https://www.youtube.com/watch?v=fEPqgSNLfK8")

captain_fantastic = media.Movie("Captain Fantastic", "In the forests, a " +
                                "father devoted to raising his six kids with" +
                                " a rigorous physical and intellectual " +
                                "education is forced to leave his paradise " +
                                "and enter the world, challenging his idea " +
                                "of what it means to be a parent",
                                "https://upload.wikimedia.org/wikipedia/en/" +
                                "c/c2/Captain_Fantastic_poster.jpg",
                                "https://www.youtube.com/watch?v=D1kH4OMIOMc")

intouchables = media.Movie("The Intouchables", "After he becomes a " +
                           "quadriplegic from a paragliding accident, an " +
                           "aristocrat hires a young man from the projects " +
                           "to be his caregiver",
                           "https://upload.wikimedia.org/wikipedia/en/9/93/" +
                           "The_Intouchables.jpg",
                           "https://www.youtube.com/watch?v=34WIbmXkewU")

finding_neverland = media.Movie("Finding Neverland", "The story of " +
                                "J.M. Barrie's friendship with a family who " +
                                "inspired him to create Peter Pan",
                                "https://upload.wikimedia.org/wikipedia/en/" +
                                "thumb/2/2e/Findingneverlandposter.jpg/220px" +
                                "-Findingneverlandposter.jpg",
                                "https://www.youtube.com/watch?v=M5_AOB9eCDM")

moulin_rouge = media.Movie("Moulin Rouge!", "A poet falls for a beautiful " +
                           "courtesan whom a jealous duke covets",
                           "https://upload.wikimedia.org/wikipedia/en/9/9f/" +
                           "Moulin_rouge_poster.jpg",
                           "https://www.youtube.com/watch?v=2PpgPxjzbkA")


movies = [interstellar, little_prince, captain_fantastic, intouchables,
          finding_neverland, moulin_rouge]
fresh_tomatoes.open_movies_page(movies)
