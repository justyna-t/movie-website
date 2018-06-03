import webbrowser


class Video():
    def __init__(self, title, trailer_youtube):
        self.title = title
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    """This class provides a way to store movie related information."""
    # Variable "VALID_RATINGS" is defined at the level of the class and is
    # autside the init function, because this is Class Variable. The all
    # instances of class Movie can share this list. If Class Variable is
    # constant (the value of this variable is probably not going change every
    # now and then) Google Style Guide recommends to use all an uppercase
    # letters.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube_url):
        Video.__init__(self, movie_title, trailer_youtube_url)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
