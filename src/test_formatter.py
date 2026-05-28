from formatter import format_email

# Simulando o retorno do /api/v1/summary
summary_mock = {
    "date": "2026-05-28",
    "currencies": {
        "USD": { "name": "Dólar Americano", "bid": "5.21", "pct_change": "-0.45" },
        "EUR": { "name": "Euro", "bid": "5.67", "pct_change": "+0.12" },
        "GBP": { "name": "Libra Esterlina", "bid": "6.89", "pct_change": "+0.30" },
    }
}

# Simulando o retorno do /api/v1/preferences/{email}
preferences_mock = {
    "email": "tomás@gmail.com",
    "currencies": ["USDBRL", "EURBRL"],
    "cryptos": ["bitcoin"]
}

# Chama o formatter com os dados falsos
resultado = format_email(summary_mock, preferences_mock)
with open("test_output.html", "w", encoding="utf-8") as f:
    f.write(resultado)

print("Arquivo test_output.html gerado!")