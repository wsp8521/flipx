import requests
import streamlit as st
from login.service import Logout

class MovieRepository:
    def __init__(self):
        self.__url_base = 'https://wesley8521.pythonanywhere.com/api/v1/'
        self.__url_token = f'{self.__url_base}movie/'
        self.__headers = {'Authorization': f'Bearer {st.session_state.token}'} #armazenando a sessão 
        
     #obtando dados   
    def get_movie(self):
        response = requests.get(
            url=self.__url_token,
            headers=self.__headers
        )
        if response.status_code ==200: #verifica se obteve dados com sucesso
            return response.json() #retornando lista de generos
        
        if response.status_code == 401: #verifica se o token expirou
            logout = Logout()
            logout.logout()
            return None
        raise Exception(f'Erro ao obter dados da api. Error code: {response.status_code}')
    
   #obtendo statistica de filmes
    def get_statistic(self):
        response = requests.get(
            url=f'{self.__url_token}statistic',
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
    def post_movie(self, data):
        response = requests.post(url=self.__url_token, headers=self.__headers, data=data)
        if response.status_code ==201: #verifica se dados foram postados com sucesso
            return response.json() #retornando lista de generos
        
        if response.status_code == 401: #verifica se o token expirou
            logout = Logout()
            logout.logout()
            return None
        raise Exception(f'Erro ao obter dados da api. Error code: {response.status_code}')