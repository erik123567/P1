import media
import fresh_tomatoes

#Creating favorite movies
joe_dirt = media.Movie("Joe Dirt",
                       "https://djrioblog.files.wordpress.com/2013/12/joe-dirt-2001-movie-poster.jpg" ,
                       "https://www.youtube.com/watch?v=FpHIIE9Lois")
lotr = media.Movie("Lord of the Rings",
                   "http://ia.media-imdb.com/images/M/MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@._V1_SX640_SY720_.jpg" ,
                   "https://www.youtube.com/watch?v=V75dMMIW2B4")
step_brothers = media.Movie("Step Brothers" ,
                            "http://ia.media-imdb.com/images/M/MV5BMTcwNzUzMjU1OV5BMl5BanBnXkFtZTcwMTM0NDQ2MQ@@._V1_SX640_SY720_.jpg" ,
                            "https://www.youtube.com/watch?v=CewglxElBK0")
the_matrix = media.Movie("The Matrix",
                         "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX640_SY720_.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")
gladiator = media.Movie("Gladiator" ,
                        "http://velocitycleveland.org/wordpress/wp-content/uploads/2014/01/gladiator1.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE")
the_patriot = media.Movie("The Patriot",
                          "http://ecx.images-amazon.com/images/I/51TiXRZCo7L.jpg",
                          "https://www.youtube.com/watch?v=P5u1am7pmrw")




movies = [joe_dirt, lotr, step_brothers, the_matrix, gladiator, the_patriot]
#Passing the list of movies so they can be rendered 
fresh_tomatoes.open_movies_page(movies)
