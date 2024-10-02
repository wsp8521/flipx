from .repository import ActorRepository
import streamlit as st

class ActorService():
    def __init__(self):
        self.__respository = ActorRepository()

    
    def read_actor(self):
        if 'actors' in st.session_state: #verifica se foi criado uma sessão actors
            return st.session_state.actors #retorna dados da sessao armazenadas caso a sessao tenha sido criado 
        actors = self.__respository.get_actor() #obtendo dados do ator na api
        st.session_state.actors = actors #salvando  dados na sessão
        return actors
    
    def create_actor(self, nameActor, birthday_date, nationality):
        data = {
            'nameActor':nameActor,
            'birthday_date':birthday_date,
            'nationality':nationality
            }
        new_actors = self.__respository.post_actor(data) #cadastrando dados
        st.session_state.actors.append(new_actors) #adicionando novos dados na sessão
        return  new_actors
        
        