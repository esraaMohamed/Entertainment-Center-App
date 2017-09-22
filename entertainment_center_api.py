import media
import series
import extractor
import fresh_tomatoes

home_again = extractor.get_movie_data(media.MOVIE_IDS["Home Again"])
table_19 = extractor.get_movie_data(media.MOVIE_IDS["Table 19"])
the_circle = extractor.get_movie_data(media.MOVIE_IDS["The Circle"])
gifted = extractor.get_movie_data(media.MOVIE_IDS["Gifted"])
beauty_and_the_beast = extractor.\
    get_movie_data(media.MOVIE_IDS["Beauty and the Beast"])
boss_baby = extractor.get_movie_data(media.MOVIE_IDS["The Boss Baby"])
secret_life_of_pets = extractor.\
    get_movie_data(media.MOVIE_IDS["Secret Life of Pets"])
despicable_me_3 = extractor.get_movie_data(media.MOVIE_IDS["Despicable Me 3"])
justice_league = extractor.get_movie_data(media.MOVIE_IDS["Justice League"])

seinfield = extractor.get_show_data(series.SHOW_IDS["Seinfield"],
                                    series.SEASON_NUMBER["Seinfield"],
                                    series.EPISODE_NUMBER["Seinfield"])
friends = extractor.get_show_data(series.SHOW_IDS["Friends"],
                                  series.SEASON_NUMBER["Friends"],
                                  series.EPISODE_NUMBER["Friends"])
got = extractor.get_show_data(series.SHOW_IDS["Game of Thrones"],
                              series.SEASON_NUMBER["Game of Thrones"],
                              series.EPISODE_NUMBER["Game of Thrones"])


movies = [home_again, table_19, the_circle, gifted, boss_baby,
          secret_life_of_pets, despicable_me_3, justice_league,
          beauty_and_the_beast, seinfield, friends, got]

fresh_tomatoes.open_movies_page(movies=movies)

