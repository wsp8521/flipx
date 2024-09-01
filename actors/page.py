import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from .service import ActorService
from datetime import datetime

 

def show_actor(): 
    actor = ActorService() 
    st.write("Elenco")
    if actor.read_actor():
        actor_df = pd.json_normalize(actor.read_actor())
        actor_df = actor_df.rename(columns={'nameActor':'Nome do Ator/Atriz', 'birthday_date':'Data de Nascimento','nationality':'Nacionalidade'})# Renomeando as colunas
       
        # Convertendo a coluna 'Data de Nascimento' para datetime, se necessário
        if actor_df['Data de Nascimento'].dtype == 'object':
            actor_df['Data de Nascimento'] = pd.to_datetime(actor_df['Data de Nascimento'])

        # Formatando a coluna de data para o formato desejado (dd/mm/yyyy)
        actor_df['Data de Nascimento'] = actor_df['Data de Nascimento'].dt.strftime('%d/%m/%Y')
        AgGrid(data=actor_df,reload_data=True, key='ator', height=250, ) #criando tabela
    else:
        st.warning("Nenhum ator/atriz encontrado")

    show_form_actors(actor.create_actor) #exibindo formulários


def show_form_actors(instance_class):
    st.write("Cadastrar novo atro/atriz")
    with st.form('cadastro', True):
        input_name = st.text_input("Nome do ator", key='name') #criando campo text input
        input_date = st.date_input("Data de nascimento",value=None,  max_value=datetime.today(), format="DD/MM/YYYY", key='year')
        input_nationallity=st.selectbox("selecione",["","Brasil","Estados Unidos"], key='nationallity')
        
        if st.form_submit_button("Cadastrar"): #criando button com label cadatrar
            if input_name and input_date and input_nationallity: #verificando se os campos estão preenchidos
                instance_class(
                    nameActor=input_name,
                    birthday_date=input_date,
                    nationality=input_nationallity
                )
                st.success(f'Ator {input_name} cadastrado com sucesso!') #ativa mensagem quando clicar no botao
                st.rerun()
            else:
                st.error("Erro ao cadastrar. Preencha todos os campos")

   
    
    