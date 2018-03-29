from video import Video


SHOW_IDS = {"Seinfield": 1400, "Friends": 1668, "Game of Thrones": 1399}
EPISODE_NUMBER = {"Seinfield": 24, "Friends": 18, "Game of Thrones": 7}
SEASON_NUMBER = {"Seinfield": 9, "Friends": 10, "Game of Thrones": 7}
TRAILERS = {1400: "https://www.youtube.com/watch?v=REF6wTs9tPk",
            1668: "https://www.youtube.com/watch?v=Eibl9JIpcKk",
            1399: "https://www.youtube.com/watch?v=-5xdTlgaaaw"}


class Series(Video):
    """
    this class has information about tv shows
    """
    def __init__(self, title, trailer_url, poster_image_url, storyline,
                 release_date):
        """
        this method initializes the series object
        :param title: the series title
        :param trailer_url: the trailer url
        :param poster_image_url: the poster of the series
        :param storyline: the storyline of the episode
        :param release_date: the release date of the series
        """
        Video.__init__(self, title=title,
                       trailer_url=trailer_url,
                       poster_image_url=poster_image_url,
                       storyline=storyline,
                       release_date=release_date)








