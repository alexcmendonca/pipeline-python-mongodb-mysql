from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
import os
from dotenv import load_dotenv

def connect_mongo(uri):
    # Criando um novo cliente e conectando ao servidor
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Enviando um ping pra conferir se a conexão foi realizada
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    
    return client

def create_connect_db(client, db_name):
    db = client[db_name]
    return db

def create_connect_collection(db, col_name):
    collection = db[col_name]
    return collection

def extract_api_data(url):
    return requests.get(url).json()

def insert_data(col, data):
    docs = col.insert_many(data)
    n_docs_inseridos = len(docs.inserted_ids)
    return n_docs_inseridos

# função do if é permitir ou impedir partes do código serem executados quando são importados
if __name__ == '__main__':

    # carregando as variáveis de conexão, usuário e senha
    load_dotenv()

    uri = os.getenv('MONGODB_URI')
    
    # estabelece a conexão com nossa instância do MongoDB
    client = connect_mongo(uri)

    # cria/conecta à base de dados específica dentro da instância do MongoDB
    db = create_connect_db(client, 'db_produtos_desafio')

    # cria/conecta à coleção específica dentro da base de dados
    col = create_connect_collection(db, 'produtos')

    data = extract_api_data('https://labdados.com/produtos')
    print(f'\nQuantiade de dados extraídos: {len(data)}')

    n_docs = insert_data(col, data)
    print(f'\nQuantiade de dados inseridos: {n_docs}')

    client.close()