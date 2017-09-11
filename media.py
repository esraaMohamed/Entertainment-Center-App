from video import Video


class Movie(Video):
    """
    this class has information about movies
    """

    # since movies have ratings this is the ratings variable, a dictionary
    RATINGS = {"General Audiences": "G", "Parental Guidance Suggested": "PG", "Parents Strongly Cautioned": "PG-13",
               "Restricted": "R", "Adults Only": "NC-17", "Not Rated": "NR"}

    def __init__(self, title, duration_in_minutes, trailer_url, poster_image_url, storyline, release_date, rating):
        Video.__init__(self, title=title, duration_in_minutes=duration_in_minutes,
                       trailer_url=trailer_url, poster_image_url=poster_image_url,storyline=storyline,
                       release_date=release_date)
        self.rating = self.RATINGS[rating]  # selecting a rating value from the ratings dictionary








