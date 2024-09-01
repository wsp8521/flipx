import streamlit as st
from api.service import Auth


#classe responsável em realizar o login.
class Login:
    def __init__(self, username, password) : #inicializado a classe com parameentros
        self._username=username
        self._password = password

    #obter dados de acesso
    def get_login(self):
        response = Auth().get_token(username=self._username, password=self._password) #recebendos do resposta
        if response.get('error'):
            st.error(f'Falha ao realizar o login. {response.get('error')}') #retornando mensagem de erro no streamlit
        else:
            st.session_state.token = response.get('access') #armazenando o token na sessiion sttreamlit na varialvel token em   st.session_state.token
            st.rerun() #aplicando refresh na tela
            
class Logout:
      def logout(self):
        for key in st.session_state.keys():
            del st.session_state[key] #limpando a session
        st.rerun()
       
       

        


    


