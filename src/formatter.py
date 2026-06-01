def format_email(summary, preferences):
    if not summary or not preferences:
        return "<p>Erro ao gerar relatório.</p>"

    cards_html = ""
    for par in preferences['currencies']:
        if len(par) == 3:
            chave = par + "BRL"  
        else:
            chave = par          

        codigo = par[:3]  

        if chave in summary['currencies']:
            dados = summary['currencies'][chave]
            variacao = float(dados['pctChange'])
            cor = "#16a34a" if variacao >= 0 else "#dc2626"
            seta = "▲" if variacao >= 0 else "▼"

            cards_html += f"""
            <div style="border: 1px solid #e5e7eb; border-radius: 8px; padding: 16px; margin: 8px 0;">
                <strong>{dados['name']} ({codigo})</strong>
                <p>R$ {dados['bid']}</p>
                <p style="color:{cor}">{seta} {dados['pctChange']}%</p>
            </div>
            """

    html = f"""
    <html>
      <body style="max-width: 600px; margin: auto; font-family: Arial, sans-serif;">
        <div style="background:#0F6E56; padding:24px;">
          <h1 style="color:white;">Currency.Dash</h1>
          <p style="color:white;">Relatório diário — {summary['date']}</p>
        </div>
        <div style="padding:24px;">
          <p>Olá, {preferences['email']}!</p>
          {cards_html}
        </div>
        <div style="padding:16px; text-align:center; color:#6b7280;">
          <p>© Currency.Dash</p>
        </div>
      </body>
    </html>
    """

    return html