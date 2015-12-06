import webbrowser

class Movie():
    """ This class provides a way to store movie related info

        Attributes:
            movie_title: The title of the movie
            poster_image: A picture that will be displayed for the movie 
            trailer_youtube: A link to the trailer that will open when clicked
            """
    
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Creates a movie object, that requires 3 string parameters

            Args:
            movie_title: The title of the movie
            poster_image: A picture that will be displayed for the movie 
            trailer_youtube: A link to the trailer that will open when clicked
        """
        
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """ Opens the trailer for the movie that called it """
       
        webbrowser.open(self.trailer_youtube_url)
