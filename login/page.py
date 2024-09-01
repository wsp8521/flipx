import streamlit as st
from .service import Login


def show_login():
     st.write("Login")
     input_user = st.text_input("Usuário")
     inpt_pass = st.text_input(label='senha', type= "password")

     if st.button("Entrar"):
          login = Login(username=input_user, password=inpt_pass)
          return login.get_login()
          