# pip install pymongofor conexao in conexao.find():
from pymongo import MongoClient
cliente = MongoClient('mongodb://localhost:27017/')

db = cliente.dbmidias
conexao = db.posts

print(conexao.find_one())
print(conexao.find_one({"nome":"José"}))

for conexao in conexao.find():
    print(conexao)