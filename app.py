import streamlit as st
from genres.page import show_genres
from actors.page import show_actor
from reviws.page import show_reviews
from movie.page import show_movie
from login.page import show_login
from home.page import show_home

def main():

    if 'token' not in st.session_state: #verifica se há uma sessão com chavem 'token'
        show_login() #permanece na pagina de longin se nao for encotrado uma chave token
    else:
        navBar = st.sidebar.selectbox(
                'Selecione uma opção',['Home', 'Filmes','Gênero','Elenco','Avaliação'],
            )
        
        if navBar == 'Home':
            st.title('Flipx')
            show_home()
                
        if navBar == 'Filmes':
            st.title("Flipx/Filmes")
            show_movie()

        if navBar == 'Gênero':
            st.title("Flipx/Gênero")
            show_genres()

        if navBar == 'Elenco':
            st.title("Flipx/Elenco")
            show_actor()

        if navBar == 'Avaliação':
            st.title("Flipx/Avaliação")
            show_reviews()

if __name__ == '__main__':
    main()
