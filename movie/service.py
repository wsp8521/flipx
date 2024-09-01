from .repository import MovieRepository

class MovieService():
    def __init__(self):
        self.__respository = MovieRepository()

    
    def read_movie(self):
        return self.__respository.get_movie() #obtando dados
    
    
    def read_movie_statistic(self):
        return self.__respository.get_statistic()
    
    def create_movie(self, title, genre, actors, realese_data, sinpse):
        data = {
            'title':title,
            'genre':genre,
            'actors':actors,
            'realese_data':realese_data,
            'sinpse':sinpse
            }
        return self.__respository.post_movie(data) #cadastrando dados
        
        