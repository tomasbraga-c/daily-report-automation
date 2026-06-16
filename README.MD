# 📧 Daily Report Automation

Automação que coleta dados de variação de moedas e criptomoedas do [Currency.Dash](https://currency-dashboard-beryl.vercel.app) e envia um relatório diário formatado por e-mail automaticamente via GitHub Actions.

## 🚀 Sobre o projeto

Este projeto consome diretamente a API do [Currency.Dash](https://github.com/tomasbraga-c/currency-dashboard) — um dashboard fullstack de cotações em tempo real. Todo dia de manhã, de segunda a sábado, um script Python acorda o servidor, busca todos os usuários ativos cadastrados, e envia um e-mail HTML personalizado para cada um com as variações do dia. Cada e-mail inclui um link de cancelamento de inscrição.

## 🛠️ Tecnologias

- Python 3.11
- GitHub Actions (agendamento via cron)
- SMTP Gmail (envio de e-mail)
- API REST do Currency.Dash

## ⚙️ Como funciona

1. GitHub Actions aciona o script às 8h (horário de Brasília)
2. Wake-up do servidor Render via endpoint /health (plano gratuito hiberna após inatividade)
3. Busca todos os usuários ativos via GET /api/v1/preferences
4. Coleta os dados do dia via GET /api/v1/summary
5. Para cada usuário:
   - Filtra as moedas e criptos de sua preferência
   - Busca individualmente as criptos que não vêm no resumo padrão (GET /api/v1/cryptos/{id})
   - Formata e-mail HTML responsivo com a identidade visual do Currency.Dash
   - Inclui link de cancelamento de inscrição no rodapé
   - Envia via SMTP do Gmail

## 🔧 Como rodar localmente

**1. Clone o repositório**

```bash
git clone https://github.com/tomasbraga-c/daily-report-automation.git
cd daily-report-automation
```

**2. Instale as dependências**

```bash
pip install -r requirements.txt
```

**3. Configure as variáveis de ambiente**

```bash
cp .env.example .env
```

**4. Rode o script**

```bash
python src/main.py
```

## 🔑 Variáveis de ambiente

| Variável | Descrição |
|----------|-----------|
| `CURRENCY_API_URL` | URL da API do Currency.Dash |
| `EMAIL_USER` | E-mail do remetente (Gmail) |
| `EMAIL_PASS` | App Password do Gmail |

> ⚠️ Para usar o Gmail, é necessário gerar uma [App Password](https://myaccount.google.com/apppasswords) com a verificação em duas etapas ativada.

## ⏰ Agendamento

O script é executado automaticamente via GitHub Actions com o seguinte cron:
0 11 * * 1-6  →  8h horário de Brasília, de segunda a sábado

Também é possível disparar manualmente pela aba **Actions** do repositório.

## ✉️ Cancelamento de inscrição

Cada e-mail enviado contém um link de cancelamento no rodapé. Ao clicar, o usuário é direcionado para o endpoint GET /api/v1/unsubscribe do Currency.Dash, que marca sua inscrição como inativa no banco de dados. A partir daí, ele deixa de receber os relatórios.

## 🔗 Projeto relacionado — Currency.Dash

Este projeto é um consumidor da API do [Currency.Dash](https://github.com/tomasbraga-c/currency-dashboard). Os dois projetos se complementam:

| Projeto | Responsabilidade |
|---------|-----------------|
| [Currency.Dash](https://currency-dashboard-beryl.vercel.app) | Coleta e expõe os dados em tempo real. Usuários se cadastram pelo botão "Relatório" no site e suas preferências são salvas no banco (Supabase) |
| Daily Report Automation | Consome a API e distribui os dados por e-mail todo dia às 8h |

Para receber o relatório diário, basta acessar o [Currency.Dash](https://currency-dashboard-beryl.vercel.app), clicar em **Relatório** e cadastrar seu e-mail com as moedas de preferência.

## 🔮 Melhorias futuras

- **Relatório em PDF** — gerar e anexar um PDF além do e-mail HTML
- **Frequência personalizável** — permitir que o usuário escolha receber diário, semanal ou apenas em grandes variações
- **Templates de e-mail** — separar o HTML em templates (Jinja2) para facilitar manutenção

## 👨‍💻 Autor

**Tomás Braga**
[LinkedIn](https://linkedin.com/in/tomás-braga) • [GitHub](https://github.com/tomasbraga-c) • [Portfólio](https://portfoliotomasb.vercel.app)
