import requests


class API:
    def __init__(self):
        self.api_token = "5304ee034492f039c991b4ecee3512c6"

    def get_movie_info(self, movie_id):
        url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key="+self.api_token + \
              "&append_to_response=videos"

        payload = "{}"
        response = requests.request("GET", url, data=payload)

        return response.json()

    def get_release_info(self, movie_id):
        url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/release_dates?api_key="+self.api_token
        payload = "{}"
        response = requests.request("GET", url, data=payload)
        return response.json()

    def get_episode_videos(self, show_id, season_number, episode_number):
        url = "https://api.themoviedb.org/3/tv/" + str(show_id) + "/season/" + str(season_number) + "/episode/"\
              + str(episode_number) + "/videos?api_key="+self.api_token + "&language=en-US"

        payload = "{}"
        response = requests.request("GET", url, data=payload)
        return response.text

    def get_episode_info(self, show_id, season_number, episode_number):
        url = "https://api.themoviedb.org/3/tv/" + str(show_id) + "/season/" + str(season_number) +\
              "/episode/" + str(episode_number) + "?api_key=" + self.api_token + "&language=en-US"

        payload = "{}"
        response = requests.request("GET", url, data=payload)
        return response.json()
