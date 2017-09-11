from video import Video


class Series(Video):
    """
    this class has information about tv shows
    """

    def __init__(self, title, duration_in_minutes, trailer_url, poster_image_url, storyline, release_date):
        Video.__init__(self, title=title, duration_in_minutes=duration_in_minutes,
                       trailer_url=trailer_url, poster_image_url=poster_image_url,storyline=storyline,
                       release_date=release_date)








