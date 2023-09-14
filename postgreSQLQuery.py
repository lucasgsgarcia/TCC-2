import psycopg2
import timeit


def perform_query(cursor):

    query = """
    SELECT *
    FROM resposta
    WHERE id_aluno IN (
        SELECT id
        FROM aluno
        WHERE email = 'aluno01@ig.com.br'
    )
    AND resposta_aluno->>'resposta' = 'exemplo de resposta JSONB'
    """
    cursor.execute(query)

connection = psycopg2.connect(
    host="localhost",
    database="jogos",
    user="postgres",
    password="123"
)

elapsed_time_seconds = timeit.timeit(lambda: perform_query(connection.cursor()), number=1)
elapsed_time_ms = elapsed_time_seconds * 1000

print(f"Tempo decorrido para a busca: {elapsed_time_ms:.3f} ms")

connection.cursor().close()
connection.close()