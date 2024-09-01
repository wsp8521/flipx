import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from .service import ReviwService
from movie.service import MovieService

#visulaizar tabela
def show_reviews():
    get_movie = MovieService().read_movie()
    review = ReviwService()
    st.write("Avaliações")

    #TABELA
    if review.read_reviw():
        review_df = pd.json_normalize(review.read_reviw())
        movies_dict = {movie['id']: movie['title'] for movie in get_movie} # Criando um dicionário com os títulos dos filmes
        review_df['Nome do Filme'] = review_df['movie'].map(movies_dict)  # Mapeando os títulos dos filmes para o DataFrame
        review_df = review_df.drop(columns=['movie']) #removendo colunas
        review_df = review_df[['id','Nome do Filme','stars','comment']] #reorganizando as colunas
        review_df = review_df.rename(columns={'stars':'Estrelas','comment':'Comentários'})# Renomeando as colunas
       
        AgGrid(data=review_df, reload_data=True, key='genere', height=250, ) #criando tabela
    else:
        st.warning("Nehuma avaliação encontrado")
    show_form_reviw(review.create_review) #mostra o formulário

#visualizar formulário
def show_form_reviw(instance_class):
    movies = MovieService()
    
    st.write("Avaliar filmes")
    with st.form("cadastro", True):
        '''fazendo tratamento na lista de filmes para ser usado no slectBox. Na lista aparecerá o nome do filmes, mas ao selecionar
            será armazenado na base de dados o id do filmes'''
        movie_name = {movie['title']:movie['id'] for movie in movies.read_movie()} #cria dicionário na estrutura movie:id
        select_movie = st.selectbox("Selecione um filme", list(movie_name.keys()), index=None, placeholder="Escolha uma opção") #obtando o id do filme
        get_id_movie = movie_name[select_movie] if select_movie else None #operador usuado quando hover propriedade index=None no  st.selectbox
        
        stars = st.number_input("Nota de 0 a 5", min_value=0, max_value=5)
        coment = st.text_area("Comentários")    
        if st.form_submit_button("Cadastrar"): #criando button com label cadatrar
            if movie_name and stars : #validando campos
                instance_class(movie=get_id_movie, stars = stars, comment = coment)
                st.success(f'{get_id_movie} avaliado com sucesso!') #ativa mensagem quando clicar no botao
                st.rerun()
            else:
                 st.error("os campos filmes e estrelas são de preenchimento obrigatórios")