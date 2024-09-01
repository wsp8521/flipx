from .repository import GenreRepository


class GenreService():
    def __init__(self):
        self.genre_repository = GenreRepository()
    
    def read_genre(self):
        return self.genre_repository.get_genres() #obtando dados
    
    def create_genre(self, name):
        data = {'name':name}
        return self.genre_repository.post_genres(data) #cadastrando dados
        
        