import pandas as pd
import requests
import os
import pywhatkit as kit
from datetime import date
from dotenv import load_dotenv
import time

load_dotenv()

api = os.getenv("API")
diretorio = os.getenv("CAMINHO")
numero_celular = os.getenv("NUMERO")

# 1. Configuração e Coleta
hoje = date.today().strftime("%d-%m-%Y")

print(f"Iniciando consulta para o dia {hoje}...")

response = requests.get(api)

df = pd.DataFrame(response.json())

# 2. Tratamento do Relatório
relatorio = df[['symbol', 'name', 'current_price', 'price_change_percentage_24h']].copy()

relatorio.columns = ['Sigla', 'Moeda', 'Preço (USD)', '% 24h']

nome_arquivo = f"Relatorio_Cripto_{hoje}.xlsx"

caminho_final = os.path.join(diretorio, nome_arquivo)

# Cria a pasta caso não exista
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Salva o Excel
relatorio.to_excel(caminho_final, index=False)

print(f"Excel salvo em: {caminho_final}")

mensagem = f"🚀 Relatório de Cripto ({hoje}) gerado com sucesso na pasta de estudos! O Bitcoin está custando USD {relatorio.iloc[0]['Preço (USD)']}"

print("Abrindo WhatsApp Web para enviar...")

# Envia a mensagem (ele vai abrir o navegador sozinho)
# wait_time=15 (espera 15s para carregar o WhatsApp), tab_close=True (fecha a aba depois)
kit.sendwhatmsg_instantly(numero_celular, mensagem, wait_time=15, tab_close=True)

print("Processo finalizado!")