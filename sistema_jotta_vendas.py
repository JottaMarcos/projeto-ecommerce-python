import psycopg2
import requests
import random
from datetime import datetime

# --- CONFIGURAÇÕES ---
TOKEN_TELEGRAM = "8214055262:AAH_Iw4wIDPjYbnq5LtnxajYbGcmxY1a4f4"
CHAT_ID = "6201145010"
DB_CONFIG = {
    "host": "aws-1-us-east-1.pooler.supabase.com",
    "user": "postgres.ltaxntxapuekaguwuylj",
    "password": "Jottamarcos07", 
    "database": "postgres",
    "port": "6543"
}

def executar_fluxo_completo():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        agora_full = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 1. GERAÇÃO DE VENDA ALEATÓRIA
        print(f"🎲 [{agora_full}] Registrando nova venda...")
        cursor.execute(
            "INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES (%s, %s, %s, %s)",
            (random.randint(1, 100), random.randint(1, 20), random.randint(1, 3), agora_full)
        )
        conn.commit()

        # 2. BUSCA TODAS AS MÉTRICAS EM UMA SÓ CONSULTA (Mais rápido!)
        cursor.execute("""
            SELECT 
                SUM(v.quantidade * p.preco_unitario) AS fat_total, 
                COUNT(v.id_venda) AS qtd_total,
                SUM(CASE WHEN DATE(v.data_venda) = CURRENT_DATE THEN v.quantidade * p.preco_unitario ELSE 0 END) AS fat_hoje,
                COUNT(CASE WHEN DATE(v.data_venda) = CURRENT_DATE THEN v.id_venda END) AS qtd_hoje
            FROM vendas v 
            JOIN produtos p ON v.id_produto = p.id_produto
        """)
        ac_f, ac_v, hj_f, hj_v = cursor.fetchone()
        conn.close()

        # 3. MENSAGEM TURBINADA PARA O TELEGRAM
        texto = (
            "🚀 *DASHBOARD REAL-TIME JOTTA*\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "📅 *RESULTADO DE HOJE*\n"
            f"💰 Receita: R$ {hj_f or 0:,.2f}\n"
            f"📦 Pedidos: {hj_v or 0}\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🏛️ *HISTÓRICO ACUMULADO*\n"
            f"💰 Receita Total: R$ {ac_f:,.2f}\n"
            f"📦 Total Pedidos: {ac_v}\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "✅ _Sincronizado via Python & Supabase_"
        )
        
        requests.post(f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage", 
                      data={"chat_id": CHAT_ID, "text": texto, "parse_mode": "Markdown"})
        
        print(f"✅ Relatório enviado! Total acumulado agora é de {ac_v} vendas.")

    except Exception as e:
        print(f"❌ Erro na operação: {e}")

executar_fluxo_completo()