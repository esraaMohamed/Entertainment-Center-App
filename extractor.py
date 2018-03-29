import api_class
import media
import series

"""
API calls from the api class 
"""


def get_movie_name(json_text):
    return json_text["original_title"]


def get_movie_story_line(json_text):
    return json_text["overview"]


def get_movie_poster_url(json_text):
    return "https://image.tmdb.org/t/p/w500/" + json_text["poster_path"]


def get_movie_release_date(json_text):
    return json_text["release_date"]


def get_movie_duration(json_text):
    return json_text["runtime"]


def get_movie_youtube_trailer_link(json_text):
    return "https://www.youtube.com/watch?v=" + \
           json_text["videos"]["results"][0]["key"]


def get_movie_rating(movie_id):
    """
    getting the rating of the movie
    :param movie_id: the movie id
    :return: the rating of the movie in the US
    """
    release_data_json_text = api_class.API().get_release_info(movie_id)
    data = release_data_json_text["results"]
    for item in data:
        if item["iso_3166_1"] == "US":
            return item["release_dates"][0]["certification"]


def movie_api_data_call(movie_id):
    """
    getting the movie details from the api call in the api class
    :param movie_id: movie id
    :return: the movie json data returned from the api call
    """
    return api_class.API().get_movie_info(movie_id)


def get_movie_data(movie_id):
    """
    getting the movie data object from the json data returned from the api
     calls
    :param movie_id: the id of the movie
    :return: the movie object
    """
    movie_data_json = movie_api_data_call(movie_id)
    movie = media.Movie(
        title=get_movie_name(movie_data_json),
        duration_in_minutes=get_movie_duration(movie_data_json),
        trailer_url=get_movie_youtube_trailer_link(movie_data_json),
        poster_image_url=get_movie_poster_url(movie_data_json),
        storyline=get_movie_story_line(movie_data_json),
        release_date=get_movie_release_date(movie_data_json),
        rating=get_movie_rating(movie_id))
    return movie


def get_episode_name(json_text):
    return json_text["name"]


def get_episode_release_date(json_text):
    return json_text["air_date"]


def get_episode_storyline(json_text):
    return json_text["overview"]


def get_episode_poster(json_text):
    return "https://image.tmdb.org/t/p/w500/" + json_text["still_path"]


def episode_api_data_call(show_id, season_number, episode_number):
    """
    calling the api method to get the tv show episode data from the api class
    :param show_id:
    :param season_number:
    :param episode_number:
    :return: the json data returned from the api call
    """
    return api_class.API().get_episode_info(show_id=show_id,
                                            season_number=season_number,
                                            episode_number=episode_number)


def get_episode_video(show_id, season_number, episode_number):
    """
    gets the videos of a certain episode
    :param show_id: the show id
    :param season_number: the season number
    :param episode_number: the episode number
    :return: the videos of the episode (if any exist)
    """
    return api_class.API().get_episode_videos(show_id=show_id,
                                              season_number=season_number,
                                              episode_number=episode_number)


def get_show_data(show_id, season_number, episode_number):
    """
    getting the TV show data object from the json data returned from the api
    calls
    :param show_id: the tv show id
    :param season_number: the number of the season
    :param episode_number: the episode number
    :return: an object of the tv show episode
    """
    episode_data = episode_api_data_call(show_id, season_number,
                                         episode_number)
    show = series.Series(title=get_episode_name(episode_data),
                         trailer_url=series.TRAILERS[show_id],
                         poster_image_url=get_episode_poster(episode_data),
                         storyline=get_episode_storyline(episode_data),
                         release_date=get_episode_release_date(episode_data))
    return show
