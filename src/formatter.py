def format_email(summary, preferences):
    if not summary or not preferences:
        return "<p>Erro ao gerar relatório.</p>"

    VERDE = "#0F6E56"
    VERDE_CLARO = "#16a34a"
    VERMELHO = "#dc2626"
    CINZA_TEXTO = "#6b7280"
    CINZA_BORDA = "#e5e7eb"
    FUNDO = "#f4f6f5"

    # ---- CARDS DE MOEDA ----
    cards_html = ""
    for par in preferences['currencies']:
        limpo = par.replace("-", "")
        chave = limpo + "BRL" if len(limpo) == 3 else limpo
        codigo = limpo[:3]

        if chave in summary['currencies']:
            dados = summary['currencies'][chave]
            variacao = float(dados['pctChange'])
            cor = VERDE_CLARO if variacao >= 0 else VERMELHO
            seta = "▲" if variacao >= 0 else "▼"
            nome = dados['name'].split('/')[0]

            cards_html += f"""
            <tr>
              <td style="padding:6px 0;">
                <table width="100%" cellpadding="0" cellspacing="0" style="background:#ffffff; border:1px solid {CINZA_BORDA}; border-radius:12px;">
                  <tr>
                    <td style="padding:16px 20px;">
                      <div style="font-size:11px; letter-spacing:0.08em; text-transform:uppercase; color:{CINZA_TEXTO}; margin-bottom:4px;">{codigo} · BRL</div>
                      <div style="font-size:15px; font-weight:700; color:#111827; margin-bottom:8px;">{nome}</div>
                      <div style="font-size:22px; font-weight:700; color:#111827;">R$ {dados['bid']}</div>
                      <div style="display:inline-block; margin-top:8px; padding:3px 10px; border-radius:999px; background:{cor}1a; color:{cor}; font-size:13px; font-weight:600;">{seta} {variacao:.2f}%</div>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            """

    # ---- CARDS DE CRYPTO ----
    cryptos_html = ""
    for cripto in preferences.get('cryptos', []):
        if cripto in summary.get('cryptos', {}):
            dados = summary['cryptos'][cripto]
            variacao = float(dados['usd_24h_change'])
            cor = VERDE_CLARO if variacao >= 0 else VERMELHO
            seta = "▲" if variacao >= 0 else "▼"

            cryptos_html += f"""
            <tr>
              <td style="padding:6px 0;">
                <table width="100%" cellpadding="0" cellspacing="0" style="background:#ffffff; border:1px solid {CINZA_BORDA}; border-radius:12px;">
                  <tr>
                    <td style="padding:16px 20px;">
                      <div style="font-size:11px; letter-spacing:0.08em; text-transform:uppercase; color:{CINZA_TEXTO}; margin-bottom:4px;">Cripto</div>
                      <div style="font-size:15px; font-weight:700; color:#111827; margin-bottom:8px;">{cripto.capitalize()}</div>
                      <div style="font-size:20px; font-weight:700; color:#111827;">R$ {dados['brl']:,.2f}</div>
                      <div style="font-size:13px; color:{CINZA_TEXTO}; margin-top:2px;">$ {dados['usd']:,.2f}</div>
                      <div style="display:inline-block; margin-top:8px; padding:3px 10px; border-radius:999px; background:{cor}1a; color:{cor}; font-size:13px; font-weight:600;">{seta} {variacao:.2f}% (24h)</div>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            """

    if not cards_html:
        cards_html = f'<tr><td style="padding:8px 0; color:{CINZA_TEXTO}; font-size:14px;">Nenhuma moeda disponível hoje.</td></tr>'
    if not cryptos_html:
        cryptos_html = f'<tr><td style="padding:8px 0; color:{CINZA_TEXTO}; font-size:14px;">Nenhuma cripto disponível hoje.</td></tr>'

    html = f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0; padding:0; background:{FUNDO}; font-family:Arial, Helvetica, sans-serif;">
      <table width="100%" cellpadding="0" cellspacing="0" style="background:{FUNDO}; padding:24px 0;">
        <tr>
          <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;">

              <!-- HEADER -->
              <tr>
                <td style="background:{VERDE}; border-radius:16px 16px 0 0; padding:32px 32px 28px 32px;">
                  <div style="font-size:26px; font-weight:800; color:#ffffff; letter-spacing:-0.02em;">Currency<span style="color:#7CE0C3;">.Dash</span></div>
                  <div style="font-size:11px; color:#bfe9dc; letter-spacing:0.15em; margin-top:2px;">TRAVEL · INVEST · TRACK</div>
                  <div style="margin-top:18px; font-size:13px; color:#d6f3ea;">Relatório diário — {summary['date']}</div>
                </td>
              </tr>

              <!-- CORPO -->
              <tr>
                <td style="background:#ffffff; padding:28px 32px;">
                  <p style="font-size:15px; color:#111827; margin:0 0 4px 0;">Olá! 👋</p>
                  <p style="font-size:14px; color:{CINZA_TEXTO}; margin:0 0 24px 0;">Aqui está o seu resumo das cotações de hoje.</p>

                  <div style="font-size:13px; font-weight:700; color:{VERDE}; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:8px;">💱 Moedas</div>
                  <table width="100%" cellpadding="0" cellspacing="0">{cards_html}</table>

                  <div style="font-size:13px; font-weight:700; color:{VERDE}; text-transform:uppercase; letter-spacing:0.05em; margin:24px 0 8px 0;">₿ Criptomoedas</div>
                  <table width="100%" cellpadding="0" cellspacing="0">{cryptos_html}</table>
                </td>
              </tr>

              <!-- CTA / LINKS -->
              <tr>
                <td style="background:{VERDE}; padding:20px 32px;">
                  <table width="100%" cellpadding="0" cellspacing="0">
                    <tr>
                      <td style="font-size:13px; font-weight:700; color:#7CE0C3;">Acompanhe o projeto:</td>
                      <td align="right" style="font-size:13px;">
                        <a href="https://currency-dashboard-beryl.vercel.app" style="color:#ffffff; text-decoration:none; margin-left:14px;">🌐 Site</a>
                        <a href="https://github.com/tomasbraga-c" style="color:#ffffff; text-decoration:none; margin-left:14px;">💻 GitHub</a>
                        <a href="https://linkedin.com/in/tomás-braga" style="color:#ffffff; text-decoration:none; margin-left:14px;">🔗 LinkedIn</a>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>

              <!-- RODAPÉ -->
              <tr>
                <td style="background:#ffffff; border-radius:0 0 16px 16px; padding:18px 32px; text-align:center;">
                  <p style="font-size:11px; color:{CINZA_TEXTO}; margin:0; line-height:1.6;">
                    Dados de câmbio comercial fornecidos por AwesomeAPI e CoinGecko.<br>
                    © Currency.Dash · Você recebe este e-mail por ter se inscrito no dashboard.
                  </p>
                </td>
              </tr>

            </table>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """
    return html