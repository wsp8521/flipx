import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from .service import GenreService

#visulaizar tabela
def show_genres():
    genres = GenreService()
    st.write("Lista de Gêneros")

        #TABELA
    if genres.read_genre():
        genre_df = pd.json_normalize(genres.read_genre())
        genre_df = genre_df.rename(columns={'name':'Gênero'})# Renomeando as colunas
        AgGrid(data=genre_df, reload_data=True, key='genere', height=250, ) #criando tabela
    else:
        st.warning("Nenhum gênro encontrado")
    show_form_genre(genres.create_genre) #mostra o formulário

#visualizar formulário
def show_form_genre(instance_class):
    st.write("Cadastrar novo gênero")

    with st.form("cadastro", True):
        input_name = st.text_input("Nome do gênero", key='input_text') #criando campo text input
        
        if st.form_submit_button("Cadastrar"): #criando button com label cadatrar
            if input_name: #validando campos
                instance_class(name=input_name)
                st.success(f'gênero {input_name} cadastrado com sucesso!') #ativa mensagem quando clicar no botao
                st.rerun()
            else:
                st.error("Erro ao cadastrar. Preencha todos os campos")