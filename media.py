import webbrowser

class Movie(object) :
    """Class to store movie related information"""

    #Ratings omitted in lieu of storyline details
    #VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube) :
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    #Module to open trailer video    
    def show_trailer(self) :
        webbrowser.open(self.youtube_trailer)
        return
