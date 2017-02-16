class Movie(object):
    """
    This class provides the structure for storing
    information about movies.

    Attributes:
        title (str): The title of the movie
        poster_image_url (str): The url of the movie's poster.
        trailer_youtube_url (str): The url of the movie's
            trailer, on youtube.
    """
    def __init__(self, title, poster_url, trailer_url):
        """
        Initializes objects of the class Movie.
        Args:
            title (str): Movie's title
            poster_url (str): Url to movie's poster
            trailer_url (str): Url to movie's trailer on youtube
        """
        # Check title is a string. If not, raise a TypeError.
        if isinstance(title, str):
            self.title = title
        else:
            raise TypeError("title should be a string")

        # Check poster_url is a string. If not, raise a TypeError.
        if isinstance(poster_url, str):
            self.poster_image_url = poster_url
        else:
            raise TypeError("poster_url should be a string")

        # Check trailer_url is a string. If not, raise a TypeError
        if isinstance(trailer_url, str):
            self.trailer_youtube_url = trailer_url
        else:
            raise TypeError("trailer_url should be a string")








