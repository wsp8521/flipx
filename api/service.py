import requests


#Classe responsável pela obtenção de token
class Auth:
    def __init__(self):
        self.__url_base = 'https://wesley8521.pythonanywhere.com/api/v1/'
        self.__url_token = f'{self.__url_base}/authentication/token'

    #obtendo token da requisiçao
    def get_token(self, username, password):
        auth_data = {'username':username,'password':password} #armazenando dados da autenticação
        auth_response = requests.post(url=self.__url_token, data=auth_data) #enviando dados de autenticação
        
        if auth_response.status_code == 200: #verificando o status da requisição
            return auth_response.json() #retornando dados token da requisição
        
        #retorno formato json que será usando em sessions por meio da chave 'error'
        return {'error': f'Falha na autenticação: Status Code: {auth_response.status_code}'} 
