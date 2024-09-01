from .repository import ReviewRepository

class ReviwService():
    def __init__(self):
        self.__respository = ReviewRepository()

    
    def read_reviw(self):
        return self.__respository.get_reviw() #obtando dados
    
    def create_review(self, movie, stars, comment ):
        data = {
            'movie':movie,
            'stars':stars,
            'comment':comment,
            }
        return self.__respository.post_reviw(data) #cadastrando dados
        
        