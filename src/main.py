from fetcher import wake_up_server, fetch_summary, fetch_preferences
from formatter import format_email
from mailer import send_email
import os
from dotenv import load_dotenv

load_dotenv()

def main():

    wake_up_server()
    if not wake_up_server():
        print("Servidor não respondeu. Encerrando.")
    return

#########################################

    summary = fetch_summary()
    if not summary:
        print("Não foi possível obter o resumo. Encerrando.")
        return 

#########################################

    recipients = os.getenv("EMAIL_RECIPIENTS", "").split(",")
    if not recipients:
        print("Nenhum destinatário configurado. Encerrando.")
        return

#########################################

    for email in recipients:
        email = email.strip()
        if not email:
            continue
        preferences = fetch_preferences(email)
        if not preferences:
            print(f"Não foi possível obter preferências para {email}. Pulando.")
            continue
        html_content = format_email(summary, preferences)
        send_email(email, "Resumo Diário de Moedas", html_content)

#########################################

if __name__ == "__main__":
    main()