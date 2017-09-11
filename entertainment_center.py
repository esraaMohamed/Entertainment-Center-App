import media
import series
import fresh_tomatoes
"""
Here we create some movie and series objects then pass them to the fresh_tomatoes open movies page function
"""

home_again = media.Movie(title="Home Again", duration_in_minutes=97,
                         trailer_url="https://www.youtube.com/watch?v=x3xfcGCwdeI",
                         poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BNDMxNTQ0NjIw"
                                          "OV5BMl5BanBnXkFtZTgwODE5NjA5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         storyline="Life for a single mom in Los Angeles takes an unexpected turn when she allows"
                                   " three young guys to move in with her.",
                         release_date="8 September 2017",
                         rating="Parents Strongly Cautioned")

table_19 = media.Movie(title="Table 19", duration_in_minutes=87,
                       trailer_url="https://www.youtube.com/watch?v=SRVzyiM8Sgo",
                       poster_image_url="https://i2.wp.com/teaser-trailer.com/wp-content/uploads/Table-19-"
                                        "Australian-Poster.jpg?ssl=1",
                       storyline="Eloise, having been relieved of maid of honor duties after being "
                                 "unceremoniously dumped by the best man via text, decides to attend "
                                 "the wedding anyway, only to find herself seated with five fellow unwanted "
                                 "guests at the dreaded Table 19.",
                       release_date="3 March 2017",
                       rating="Parents Strongly Cautioned")

the_circle = media.Movie(title="The Circle", duration_in_minutes=110,
                         trailer_url="https://www.youtube.com/watch?v=ZkzpcfY9JAo",
                         poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMjY2OTM2Njc3Ml5BMl"
                                          "5BanBnXkFtZTgwNDgzODU3MTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         storyline="A woman lands a dream job at a powerful tech company called the Circle, "
                                   "only to uncover an agenda that will affect the lives of all of humanity.",
                         release_date="28 April 2017 ",
                         rating="Parents Strongly Cautioned")

gifted = media.Movie(title="Gifted", duration_in_minutes=101,
                     trailer_url="https://www.youtube.com/watch?v=hqTSKqBCdf0",
                     poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ2NDU3NDE"
                                      "0M15BMl5BanBnXkFtZTgwMjA3OTg0MDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                     storyline="Frank, a single man raising his child prodigy niece Mary, is drawn into a"
                               " custody battle with his mother.",
                     release_date="12 April 2017",
                     rating="Parents Strongly Cautioned")

justice_league = media.Movie(title="Justice League", duration_in_minutes=0,
                             trailer_url="https://www.youtube.com/watch?v=TY078G4-tm8",
                             poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMjI2NjI2M"
                                              "DQ0NV5BMl5BanBnXkFtZTgwMTc1MjAwMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                             storyline="Fueled by his restored faith in humanity and inspired by Superman's "
                                       "selfless act, Bruce Wayne enlists the help of his newfound ally, Diana Prince, "
                                       "to face an even greater enemy.",
                             release_date="17 November 2017",
                             rating="Not Rated")

beauty_and_the_beast = media.Movie(title="Beauty and the Beast", duration_in_minutes=129,
                                   trailer_url="https://www.youtube.com/watch?v=iXfEc4wG208",
                                   poster_image_url="http://cdn.movieweb.com/img.teasers.posters/FI3"
                                                    "wb9J2tk7657_243_a/Beauty-And-The-Beast.jpg",
                                   storyline="An adaptation of the fairy tale about a monstrous-looking prince "
                                             "and a young woman who fall in love.",
                                   release_date="17 March 2017",
                                   rating="Parental Guidance Suggested")

boss_baby = media.Movie(title="The Boss Baby", duration_in_minutes=97,
                        trailer_url="https://www.youtube.com/watch?v=Ud8j5GaqH3c",
                        poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMTg5MzUxNzgxNV5BMl5"
                                         "BanBnXkFtZTgwMTM2NzQ3MjI@._V1_SY1000_CR0,0,685,1000_AL_.jpg",
                        storyline="A suit-wearing, briefcase-carrying baby pairs up with his 7-year old brother to "
                                  "stop the dastardly plot of the CEO of Puppy Co.",
                        release_date="31 March 2017",
                        rating="Parental Guidance Suggested")

secret_life_of_pets = media.Movie(title="Secret Life of Pets", duration_in_minutes=87,
                                  trailer_url="https://www.youtube.com/watch?v=UZ4WBlveGfw",
                                  poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMjIzMzA1O"
                                                   "TkzNV5BMl5BanBnXkFtZTgwODE3MjM4NzE@._V1_.jpg",
                                  storyline="The quiet life of a terrier named Max is upended when his owner takes in "
                                            "Duke, a stray whom Max instantly dislikes.",
                                  release_date="8 July 2016",
                                  rating="Parental Guidance Suggested")

despicable_me_3 = media.Movie(title="Despicable Me 3", duration_in_minutes=90,
                              trailer_url="https://www.youtube.com/watch?v=euz-KBBfAAo",
                              poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BNjUyNzQ2MTg3Ml5BM"
                                               "l5BanBnXkFtZTgwNzE4NDM3MTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
                              storyline="Gru meets his long-lost charming, cheerful, and more successful twin brother"
                                        " Dru who wants to team up with him for one last criminal heist.",
                              release_date="30 June 2017",
                              rating="Parental Guidance Suggested")

friends_last_episode = series.Series(title="The Last One", duration_in_minutes=22,
                                     trailer_url="https://www.youtube.com/watch?v=rivGNerDt6c",
                                     poster_image_url="https://i.pinimg.com/236x/46/8c/81/468c81d7750d07b29590017"
                                                      "b1dae69ec--last-episode-friends-forever.jpg",
                                     storyline="Rachel is leaving for her job in Paris. Monica and Chandler are "
                                               "packing up the apartment.",
                                     release_date="6 May 2004")

how_i_met_your_mother_last_episode = series.Series(title="Last Forever", duration_in_minutes=22,
                                                   trailer_url="https://www.youtube.com/watch?v=AM9AqsEwZrA",
                                                   poster_image_url="https://images-na.ssl-images-amazon.com/images/"
                                                                    "M/MV5BMTQ4Nzg0Njk1M15BMl5BanBnXkFtZTgwMDQ5MDMyMj"
                                                                    "E@._V1_.jpg",
                                                   storyline="As the years go on, changes cause the group to drift "
                                                             "apart, but they reunite one more time for Ted's wedding."
                                                             " Meanwhile, a monumental event causes Barney to finally "
                                                             "change his ways.",
                                                   release_date="31 March 2014")


game_of_thrones_season_7_finale = series.Series(title="The Dragon and the Wolf", duration_in_minutes=81,
                                                trailer_url="https://www.youtube.com/watch?v=-5xdTlgaaaw",
                                                poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5"
                                                                 "BOTMyM2UxZmMtMGI5My00NmEwLWI5OTMtMWQzNTU0NzgyYmEyXk"
                                                                 "EyXkFqcGdeQXVyNzgzMjE3Njg@._V1_.jpg",
                                                storyline="Everyone meets in King's Landing to discuss the fate of "
                                                          "the realm. In Winterfell, Sansa confronts Arya. Sam reaches"
                                                          " Winterfell, where he and Bran discover a shocking secret"
                                                          " about Jon Snow.",
                                                release_date="27 August 2017")

# The movies and series instances are added to the movies_and_series_list list variable

movies_and_series_list = [home_again, table_19, the_circle, gifted, justice_league, beauty_and_the_beast, boss_baby,
                          secret_life_of_pets, despicable_me_3, friends_last_episode,
                          how_i_met_your_mother_last_episode, game_of_thrones_season_7_finale]

# call the open_movies_page function and pass the movies_and_series_list variable to it to generate the web page

fresh_tomatoes.open_movies_page(movies=movies_and_series_list)

