import pytest
from movie_website.media import Movie
from movie_website.media import Video


def test_video():
    new = Video("some_title", "some_trailer")
    assert new.title == "some_title"
    assert new.trailer_youtube_url == "some_trailer"


def test_movie_1():
    story = "A story of a boy and his toys that come to life"
    poster = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
    trailer = "https://www.youtube.com/watch?v=vwyZH85NQC4"
    toy_story = Movie("Toy Story", story, poster, trailer)
    assert toy_story.storyline == story
    assert toy_story.title == "Toy Story"


def test_movie_2():
    story = "A marine on an alien planet"
    poster = "https://upload.wikimedia.org/wikipedia/en/b/b0/" + \
             "Avatar-Teaser-Poster.jpg"
    trailer = "https://youtu.be/5PSNL1qE6VY?t=2m15s"
    avatar = Movie("Avatar", story, poster, trailer)
    assert avatar.storyline == story
    assert avatar.title == "Avatar"


def test_movie_my_favourite():
    story = "A group of NASA scientists discovered a space-time tunnel " + \
            "that allows to interstellar travel."
    poster = "https://upload.wikimedia.org/wikipedia/en/b/bc/" + \
             "Interstellar_film_poster.jpg"
    trailer = "https://youtu.be/-gieJQejbHQ?t=55s"
    interstellar = Movie("Interstellar", story, poster, trailer)
    assert interstellar.storyline == story
    assert interstellar.title == "Interstellar"


def test_movie_valid_ratings():
    new_movie = Movie("title", "story", "poster", "trailer")
    assert Movie.VALID_RATINGS == new_movie.VALID_RATINGS


def test_movie_doc():
    result = "This class provides a way to store movie related information."
    assert Movie.__doc__ == result


def test_movie_name():
    assert Movie.__name__ == "Movie"


def test_movie_module():
    assert Movie.__module__ == "movie_website.media"
