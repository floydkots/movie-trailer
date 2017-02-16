"""
In this module, 6 instances of my favourite movies
are instantiated.

The instances, of the Movie class, from the media.py
module, are then put in a list. This list is then
passed to the function open_movies_page, from the
fresh_tomatoes.py module.
"""

import movie_project.media as media
from movie_project import fresh_tomatoes

captain_america = media.Movie(
    title="Captain America",
    poster_url="http://static2.hypable.com/wp-content/uploads/2014/03/"
               "captain-america-2-chris-evans-poster-hd.jpg",
    trailer_url="https://www.youtube.com/watch?v=dKrVegVI0Us"
)

avengers = media.Movie(
    title="Avengers",
    poster_url="http://www.hollywoodreporter.com/sites/default/files/custom/"
               "Blog_Images/avengers-movie-poster-1.jpg",
    trailer_url="https://www.youtube.com/watch?v=eOrNdBpGMv8"
)

frozen = media.Movie(
    title="Frozen",
    poster_url="http://www.heyuguys.com/images/2013/09/Frozen-UK-Poster.jpg",
    trailer_url="https://www.youtube.com/watch?v=TbQm5doF_Uc"
)

spiderman = media.Movie(
    title="Spiderman",
    poster_url="http://cdn.collider.com/wp-content/uploads/"
               "amazing-spider-man-movie-poster-438x600.jpg",
    trailer_url="https://www.youtube.com/watch?v=FpKPiHYJc54"
)

iron_man_3 = media.Movie(
    title="Iron Man 3",
    poster_url="https://img.buzzfeed.com/buzzfeed-static/static/"
               "enhanced/webdr06/2013/4/23/6/"
               "enhanced-buzz-24307-1366713398-3.jpg",
    trailer_url="https://www.youtube.com/watch?v=2CzoSeClcw0"

)

transformers_3 = media.Movie(
    title="Transformers 3",
    poster_url="http://cdn.collider.com/wp-content/uploads/"
               "transformers-dark-of-the-moon-movie-poster-04-401x600.jpg",
    trailer_url="https://www.youtube.com/watch?v=kHRf01Gjosk"
)

movies = [transformers_3, iron_man_3, spiderman, avengers,
          captain_america, frozen]

fresh_tomatoes.open_movies_page(movies=movies)
