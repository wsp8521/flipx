import requests
import streamlit as st
from login.service import Logout

class GenreRepository:
    def __init__(self):
        self.__url_base = 'https://wesley8521.pythonanywhere.com/api/v1/'
        self.url_api = f'{self.__url_base}genere/'
        self.__headers = {'Authorization': f'Bearer {st.session_state.token}'}

     #obtando dados   
    def get_genres(self):
        response = requests.get(
            url=self.url_api,
            headers=self.__headers
        )
        if response.status_code ==200: #verifica se obteve dados com sucesso
            return response.json() #retornando lista de generos
        
        if response.status_code == 401: #verifica se o token expirou
            logout = Logout()
            logout.logout()
            return None
        raise Exception(f'Erro ao obter dados da api. Error code: {response.status_code}')
        
    #postando dados 
    def post_genres(self, data):
        response = requests.post(url=self.url_api, headers=self.__headers, data=data)
        if response.status_code ==201: #verifica se dados foram postados com sucesso
            return response.json() #retornando lista de generos
        
        if response.status_code == 401: #verifica se o token expirou
            logout = Logout()
            logout.logout()
            return None
        raise Exception(f'Erro ao obter dados da api. Error code: {response.status_code}')