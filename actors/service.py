from .repository import ActorRepository

class ActorService():
    def __init__(self):
        self.__respository = ActorRepository()

    
    def read_actor(self):
        return self.__respository.get_actor() #obtando dados
    
    def create_actor(self, nameActor, birthday_date, nationality):
        data = {
            'nameActor':nameActor,
            'birthday_date':birthday_date,
            'nationality':nationality
            }
        return self.__respository.post_actor(data) #cadastrando dados
        
        