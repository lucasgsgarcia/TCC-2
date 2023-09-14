import pymongo
import random
import string
from datetime import datetime

def generate_random_oid():
    return ''.join(random.choices(string.hexdigits, k=24))

def generate_random_name():
    names = ["Lucas Garcia", "Ana Silva", "João Santos", "Maria Oliveira", "Pedro Costa"]
    return random.choice(names)

def generate_random_email():
    names = ["asdasd@asdasd.com", "testemail@gmail.com", "juquinha@ig.com.br", "email2@algumdominio.com.br", "apenasteste@teste123.com"]
    return random.choice(names)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["jogos"]
collection = db["coordenadas5m"]

num_documents = 5000000

batch_size = 100000

batch_documents = []

for _ in range(num_documents):
    document = {
        "aluno": {
            "id": random.randint(1, 999),
            "nome": generate_random_name(),
            "email": generate_random_email()
        },
        "respostaAluno": {
            "resposta": "exemplo de resposta",
        },
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
        "tempo": random.randint(1, 100),
        "status": random.choice(["A", "B", "C", "D", "E"]),
        "questao": {
            "id": random.randint(1, 999),
            "descricao": "Pergunta aqui"
        },
        "aplicacao": {
            "id": random.randint(100, 999),
            "descricao": "Descrição da Aplicação"
        }
    }

    batch_documents.append(document)

    if len(batch_documents) == batch_size:
        collection.insert_many(batch_documents)
        batch_documents = []

if batch_documents:
    collection.insert_many(batch_documents)

print(f"{num_documents} dados inseridos com sucesso!")
