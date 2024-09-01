import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from .service import MovieService
from genres.service import GenreService
from actors.service import ActorService
from datetime import datetime

 

def show_movie(): 
    movie = MovieService() 
    st.write("Lista de filmes")
    if movie.read_movie(): #verifica se ha registros cadastrados
        movie_df = pd.json_normalize(movie.read_movie())
        movie_df = movie_df.drop(columns=['actors','genre.id','sinpse']) #removendo colunas
        movie_df = movie_df[['id','title','realese_data','genre.name','rate']] #reorganizando as colunas

         #Convertendo a coluna realese_data para datetime, se necessário
        if movie_df['realese_data'].dtype == 'object':
                movie_df['realese_data'] = pd.to_datetime(movie_df['realese_data'])

        # Formatando a coluna de data para o formato desejado (dd/mm/yyyy)
        movie_df['realese_data'] = movie_df['realese_data'].dt.strftime('%d/%m/%Y')
        
        # Renomeando as colunas
        movie_df = movie_df.rename(
            columns={ 
                'title':'Título', 
                'realese_data':'Data de lançamento',
                'genre.name':'Gênero',
                'sinpse':'Resumo',
                'rate':'Avaliação'
                })
       
        AgGrid(data=movie_df,reload_data=True, key='ator', height=250, ) #criando tabela
    else:
        st.warning("Nenhum ator/atriz encontrado")
    show_form_movies(movie.create_movie) #exibindo formulários

def show_form_movies(instance_class):
    genres = GenreService().read_genre()
    actors = ActorService().read_actor()
    
    st.write("Cadastrar novo filme")
    with st.form('cadastro', True):
        input_name = st.text_input("Nome do filme", key='name') #criando campo text input
        input_date = st.date_input("Data de lançamento",value=None,  max_value=datetime.today(), format="DD/MM/YYYY", key='year')

        '''fazendo tratamento na lista de generos para ser usado no slectBox. Na lista aparecerá o nome do gênero, mas ao selecionar
        será armazenado na base de dados o id do generos'''
        genre_name = {genre['name']:genre['id'] for genre in genres} #cria dicionário na estrutura genre:id
        selectBox = st.selectbox("Genero",list(genre_name.keys()), index=None, placeholder="Selecione uma opção") #exibo o nome do gênero no selectBox
        get_id_genre = genre_name[selectBox] if selectBox else None #operador usuado quando hover propriedade index=None no  st.selectbox
    
        '''fazendo tratamento na lista de atores para ser usado no slectBox. Na lista aparecerá o nome do ator, mas ao selecionar
        será armazenado na base de dados o id do ator'''
        actors_name = {name['nameActor']:name['id'] for name in actors} #criar diacionário na eestrutur nameActor:id
        select_actors = st.multiselect("Selecione atores", list(actors_name.keys()),placeholder="Escolha uma opção")
        select_id_actors = { actors_name[name]  for name in select_actors} #pegando o dia dos atores
        input_sinopse = st.text_area('Resumo do filme')        
        
        if st.form_submit_button("Cadastrar"): 
            if input_name and genre_name and selectBox and actors_name: #verificando se os campos estão preenchidos
                instance_class(
                    title = input_name,
                    genre = get_id_genre,
                    actors = select_id_actors,
                    realese_data = input_date,
                    sinpse = input_sinopse
                    )

                st.success(f'filme {input_name} cadastrado com sucesso!') #ativa mensagem quando clicar no botao
                st.rerun()
            else:
                st.error("Erro ao cadastrar. Preencha todos os campos")

    
    
    