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
    base_url = API_URL.replace("/api/v1", "")
    tentativas = 0
    while tentativas < MAX_TENTATIVAS:
        try:
            response = requests.get(f"{base_url}/health", timeout=5)
            if response.status_code == 200:
                print("Servidor acordado!")
                time.sleep(3)
                return True
        except requests.RequestException as e:
            print(f"Erro de conexão: {e}")
        tentativas += 1
        time.sleep(WAIT_SECONDS)
    print("Falha ao acordar o servidor.")
    return False

#######################################################

def fetch_summary():
    try:
        response = requests.get(f"{API_URL}/summary", timeout=15)
        print(f"Status do summary: {response.status_code}") 
        print(f"Resposta: {response.text[:200]}")
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
    
#######################################################

def fetch_all_recipients():
    try:
        response = requests.get(f"{API_URL}/preferences", timeout=10)
        if response.status_code == 200:
            return response.json()
        print(f"Erro ao buscar destinatários: {response.status_code}")
        return []
    except requests.RequestException as e:
        print(f"Erro ao buscar destinatários: {e}")
        return []