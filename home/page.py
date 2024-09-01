import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid
from movie.service import MovieService


 

def show_home(): 
    movie_statistic = MovieService().read_movie_statistic()
    
    st.title("Estatistica de filmes")
    col1, col2, col3 = st.columns(3) #divd e colonas
    with col1:
        st.success(f'TOTAL DE FILMES:    {movie_statistic['total_movies']}')
    with col2:
       st.warning(f'TOTAL DE AVALIAÇÕES: {movie_statistic['total_Reviews']}')
    with col3:
        st.error(f'MÉDIA DAS AVALIAÇÕES: {movie_statistic['avg_stars']}')
    
    if len(movie_statistic['movie_by_genre']): #verifica se existe avaliações por genero

        fig = px.pie(
        data_frame=movie_statistic['movie_by_genre'],
        values='count',
        names='genre__name',
        title='Filmes por gênero'
    )
        st.plotly_chart(fig) #renderizando gráfico
        df=pd.json_normalize(movie_statistic['movie_by_genre'])
        df = df.rename(columns={'genre__name':'Gênero',"count":'Total'})
        AgGrid(data=df,reload_data=True, key='df', height=200 ) #criando tabela
        
        
    
    
        
    
    
