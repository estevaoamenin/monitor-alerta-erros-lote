import mysql.connector
import requests
import json
import time
from datetime import datetime

conexao = mysql.connector.connect(
    host="IP",
    port=PORTA,
    user="USUARIO",
    password="SENHA",
    database="BANCO"
)
cursor = conexao.cursor()
erro_anterior = 0

while True:
    cursor.execute("""
    QUERY
""")
    linhas = cursor.fetchall()
    erro = sum(linha[1] for linha in linhas)
        
    fornecedores = "\n".join(
        f"{linha[0]}: {linha[1]}"
        for linha in linhas
    )
    if erro > erro_anterior and erro > 0:
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        webhook_url = "WEBURL"

        payload = {
            "type": "message",
            "attachments": [
                {
                    "contentType": "application/vnd.microsoft.card.adaptive",
                    "content": {
                        "type": "AdaptiveCard",
                        "$schema": "http://adaptivecards.io",
                        "version": "1.4",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": "⚠️ ERRO DE LOTE",
                                "weight": "Bolder",
                                "size": "Medium"
                            },
                            {
                                "type": "TextBlock",
                                "text": f"Foram encontrados {erro} erros no serviço de WhatsApp."
                            },
                            {
                                "type": "TextBlock",
                                "text": f"Horário da identificação: {horario}"
                            },
                            {
                                "type": "TextBlock",
                                "text": "Fornecedores",
                                "weight": "Bolder"
                            },
                            {
                                "type": "TextBlock",
                                "text": fornecedores
                            },
                            {
                                "type": "TextBlock",
                                "text": "Favor verificar o lote e realizar a correção."
                            }
                        ]
                    }
                }
            ]
        }
        headers = {
            "Content-Type": "application/json"
            }

        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers=headers
        )

        if response.status_code != 200 and response.status_code != 202:
            print(f"Erro ao enviar: {response.status_code} - {response.text}")

    erro_anterior = erro
    time.sleep(30)