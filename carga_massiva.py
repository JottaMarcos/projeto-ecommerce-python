import psycopg2
import random
from datetime import datetime, timedelta

# Credenciais do seu Supabase
DB_CONFIG = {
    "host": "aws-1-us-east-1.pooler.supabase.com",
    "user": "postgres.ltaxntxapuekaguwuylj",
    "password": "Jottamarcos07", # <--- COLOQUE SUA SENHA AQUI
    "database": "postgres",
    "port": "6543"
}

def gerar_10k_vendas():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        print("🚀 Iniciando carga de 10.000 registros... Isso pode levar uns 2 minutos.")
        
        for i in range(1, 10001):
            id_cliente = random.randint(1, 100) 
            id_produto = random.randint(1, 30) # Os 14 produtos novos que criamos
            id_filial = random.randint(1, 6)   # As 6 filiais (SP, RJ, PR, MG, BA, GO)
            quantidade = random.randint(1, 5)
            
            # Gerando datas dos últimos 2 anos
            dias_atras = random.randint(0, 730)
            data_venda = datetime.now() - timedelta(days=dias_atras)
            
            cur.execute(
                "INSERT INTO vendas (id_cliente, id_produto, id_filial, quantidade, data_venda) VALUES (%s, %s, %s, %s, %s)",
                (id_cliente, id_produto, id_filial, quantidade, data_venda)
            )
            
            # Feedback visual para você não achar que travou
            if i % 1000 == 0:
                print(f"📦 {i} vendas inseridas...")
        
        conn.commit()
        print("\n✅ FINALIZADO! 10.000 vendas registradas com sucesso.")
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Erro na carga: {e}")

if __name__ == "__main__":
    gerar_10k_vendas()