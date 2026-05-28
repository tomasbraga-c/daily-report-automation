def format_email(summary, preferences):
    if not summary or not preferences:
        return "Não foi possível gerar o relatório devido a erros na obtenção dos dados."

    html = "<html><body>"
    html += f"<h2>Olá {preferences['email']},</h2>" 
    html += "<p>Aqui está o seu relatório diário de moedas:</p>"

    for par in preferences['currencies']:
        codigo = par[:3]

        if codigo in summary['currencies']:

            dados = summary['currencies'][codigo]

            html += f"<p>- Código: {codigo}</p>"
            html += f"<p>  Nome: {dados['name']}</p>"
            html += f"<p>  Valor: R$ {dados['bid']}</p>"
           
            variacao = float(dados['pct_change'])
            cor = "green" if variacao >= 0 else "red"
            
            html += f"<p style='color:{cor}'>  Variação: {dados['pct_change']}%</p>"
    
    html += "</body></html>"
    
    return html