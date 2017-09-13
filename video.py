class Video:
    """
    this class has video related information
    """
    def __init__(self, title, trailer_url, poster_image_url, storyline, release_date):
        self.title = title
        self.trailer_youtube_url = trailer_url
        self.poster_image_url = poster_image_url
        self.storyline = storyline
        self.release_date = release_date
