import psycopg2
import random
from datetime import datetime, timedelta

conn = psycopg2.connect(
    host="localhost",
    database="jogos",
    user="postgres",
    password="123"
)

nomes = ["Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace", "Helen", "Ivan", "Jack"]
dominios_email = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "example.com"]

def generate_email():
    nome = random.choice(nomes)
    dominio = random.choice(dominios_email)
    return f"{nome.lower()}@{dominio}"

def populate_aluno_table(conn):
    cursor = conn.cursor()
    for _ in range(29969):  # Quantidade de alunos a serem inseridos
        nome = random.choice(nomes)
        email = generate_email()
        senha = "senha_aleatoria"
        id_turma_atual = random.randint(1, 5)
        ingresso_turma = datetime.now() - timedelta(days=random.randint(1, 365))

        cursor.execute(
            "INSERT INTO aluno (nome, email, senha, id_turma_atual, ingresso_turma) VALUES (%s, %s, %s, %s, %s)",
            (nome, email, senha, id_turma_atual, ingresso_turma)
        )
    conn.commit()
    cursor.close()

populate_aluno_table(conn)

conn.close()

print("Tabela aluno populada com sucesso.")
