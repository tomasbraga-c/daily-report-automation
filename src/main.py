from fetcher import fetch_all_recipients, wake_up_server, fetch_summary, fetch_crypto, fetch_preferences
from formatter import format_email
from mailer import send_email
from dotenv import load_dotenv

load_dotenv()

def main():

    if not wake_up_server():
        print("Servidor não respondeu. Encerrando.")
        return

    summary = fetch_summary()
    if not summary:
        print("Não foi possível obter o resumo. Encerrando.")
        return
    print("Summary obtido!")

    recipients = fetch_all_recipients()
    print(f"Destinatários: {recipients}")
    if not recipients:
        print("Nenhum destinatário configurado. Encerrando.")
        return

    for user in recipients:
        email = user['email']
        print(f"Processando: {email}")

    
        for cripto in user.get('cryptos', []):
            if cripto not in summary['cryptos']:
                dados = fetch_crypto(cripto)
                if dados and cripto in dados:
                    summary['cryptos'][cripto] = dados[cripto]

        html_content = format_email(summary, user)
        send_email(email, "Resumo Diário de Moedas", html_content)

if __name__ == "__main__":
    main()