# Imports necessários
import os
import requests
import time
from dotenv import load_dotenv

# Constantes (MAX_TENTATIVAS, WAIT_SECONDS, API_URL)
MAX_TENTATIVAS = 10
WAIT_SECONDS = 25
API_URL = os.getenv("CURRENCY_API_URL", "https://currency-dashboard-api.onrender.com/api/v1")


def wake_up_server():
    tentativas = 0
    while tentativas < MAX_TENTATIVAS:
        try:
            response = requests.get(f"{API_URL}/summary", timeout=5)
            if response.status_code == 200:
                print("Servidor acordado!")
                return True
            elif response.status_code == 503:
                print(f"Servidor acordando... Tentativa {tentativas + 1}/{MAX_TENTATIVAS}")
                tentativas += 1
                time.sleep(WAIT_SECONDS)
        except requests.RequestException as e:
            print(f"Erro de conexão: {e}")
            tentativas += 1
            time.sleep(WAIT_SECONDS)
    print("Falha ao acordar o servidor.")
    return False

#######################################################

def fetch_summary():
    try:
        response = requests.get(f"{API_URL}/summary", timeout=10)
        if response.status_code == 200:
            return response.json()
        print(f"Erro ao buscar resumo: {response.status_code}")
        return None
    except requests.RequestException as e:
        print(f"Erro ao buscar resumo: {e}")
        return None

#######################################################
    
def fetch_preferences(email):
    try:
        response = requests.get(f"{API_URL}/preferences/{email}", timeout=10)
        if response.status_code == 200:
            return response.json()
        print(f"Erro ao buscar preferências: {response.status_code}")
        return None
    except requests.RequestException as e:
        print(f"Erro ao buscar preferências: {e}")
        return None