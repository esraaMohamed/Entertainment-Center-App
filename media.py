from video import Video

MOVIE_IDS = {"Home Again": 427900, "Table 19": 353569, "The Circle": 339988,
             "Gifted": 400928,
             "Justice League": 141052, "Beauty and the Beast": 321612,
             "The Boss Baby": 295693,
             "Secret Life of Pets": 328111, "Despicable Me 3": 324852}


class Movie(Video):
    """
    this class has information about movies
    """
    def __init__(self, title, duration_in_minutes, trailer_url,
                 poster_image_url,
                 storyline, release_date, rating):
        Video.__init__(self, title=title,
                       trailer_url=trailer_url,
                       poster_image_url=poster_image_url,
                       storyline=storyline,
                       release_date=release_date)
        self.duration_in_minutes = duration_in_minutes
        self.rating = rating






