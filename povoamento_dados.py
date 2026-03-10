import psycopg2
from faker import Faker
import random
import re

# Configurações de conexão
DB_CONFIG = {
    "host": "aws-1-us-east-1.pooler.supabase.com",
    "user": "postgres.ltaxntxapuekaguwuylj",
    "password": "SUA_SENHA_AQUI", # Lembre de trocar pela sua senha
    "database": "postgres",
    "port": "6543"
}

def povoar_banco():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    fake = Faker('pt_BR')

    # Limpeza para evitar duplicidade nos testes
    cursor.execute("TRUNCATE vendas, clientes, produtos, estoque RESTART IDENTITY CASCADE;")

    # Criando 100 Clientes com e-mails coerentes
    clientes = []
    for _ in range(100):
        nome = fake.name()
        email = f"{re.sub(r'\s+', '.', nome.lower())}@{fake.free_email_domain()}"
        clientes.append((nome, email, fake.city(), fake.state_abbr()))
    cursor.executemany("INSERT INTO clientes (nome, email, cidade, estado) VALUES (%s, %s, %s, %s)", clientes)

    # Criando 20 Produtos e Estoque
    categorias = ['Eletrônicos', 'Casa', 'Vestuário', 'Alimentos']
    for i in range(1, 21):
        preco = round(random.uniform(10.0, 500.0), 2)
        cursor.execute("INSERT INTO produtos (nome_produto, categoria, preco_unitario) VALUES (%s, %s, %s)", 
                       (f"Produto {i}", random.choice(categorias), preco))
        cursor.execute("INSERT INTO estoque (id_produto, quantidade_atual) VALUES (%s, %s)", (i, random.randint(10, 100)))

    # Gerando 8.000 Vendas Históricas
    vendas = [(random.randint(1, 100), random.randint(1, 20), random.randint(1, 5), fake.date_between(start_date='-1y', end_date='today')) for _ in range(8000)]
    cursor.executemany("INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES (%s, %s, %s, %s)", vendas)

    conn.commit()
    print("✅ Banco povoado com 8.000 registros!")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    povoar_banco()