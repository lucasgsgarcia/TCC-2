import psycopg2
import random
from datetime import datetime
import json

db_config = {
    'host': 'localhost',
    'database': 'jogos',
    'user': 'postgres',
    'password': '123'
}

def insert_resposta(conn, cursor, id_aluno, id_aplicacao, id_questao):
    resposta_aluno = {'resposta': 'exemplo de resposta JSONB'}
    resposta_aluno_json = json.dumps(resposta_aluno)

    quando = datetime.now()
    tempo = random.randint(1, 60)
    status = random.choice(['A', 'B', 'C', 'D', 'E'])

    insert_query = """
    INSERT INTO public.resposta (resposta_aluno, quando, tempo, status, id_questao, id_aluno, id_aplicacao)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(insert_query, (resposta_aluno_json, quando, tempo, status, id_questao, id_aluno, id_aplicacao))
    conn.commit()

try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    for _ in range(200000):
        id_aluno = random.randint(1, 20000)
        id_aplicacao = random.randint(1, 5)
        id_questao = random.randint(1, 39)

        insert_resposta(conn, cursor, id_aluno, id_aplicacao, id_questao)

    print("Dados inseridos com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    cursor.close()
    conn.close()
