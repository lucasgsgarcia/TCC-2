import pymongo
import timeit

def perform_query(collection):
    filter = {"aluno.email": "juquinha@ig.com.br", "respostaAluno.resposta": "exemplo de resposta"}
    return collection.find(filter)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["jogos"]
collection = db["coordenadas5m"]

if __name__ == "__main__":
    elapsed_time_seconds = timeit.timeit(lambda: perform_query(collection), number=1)

    elapsed_time_ms = elapsed_time_seconds * 1000
    print(f"Tempo decorrido para a busca: {elapsed_time_ms:.3f} ms")


    # num_documents = collection.count_documents({"aluno.email": "juquinha@ig.com.br", "respostaAluno.resposta": "exemplo de resposta"})
    # print(f"Número de documentos encontrados: {num_documents}")

    results = perform_query(collection).limit(10)
    for idx, result in enumerate(results, start=1):
        print(f"Resultado {idx}: {result}")

client.close()
