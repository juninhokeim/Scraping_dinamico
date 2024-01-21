from flask import Flask, request, jsonify
from flask_cors import CORS  # Certifique-se de ter instalado o Flask-CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.get_json()
        link = data.get('url')

        requisicao = requests.get(link)
        site = BeautifulSoup(requisicao.text, "html.parser")

        titulo = site.find("title").get_text()

        precoNormal = site.find_all("span", class_="andes-money-amount__fraction")[0].get_text()
        centavos = site.find_all("span", class_="andes-money-amount__cents")[0].get_text()
        resultado_normal = f"R$ {precoNormal},{centavos}"

        precoPromo = site.find_all("span", class_="andes-money-amount__fraction")[1].get_text()
        centavos_promo = site.find_all("span", class_="andes-money-amount__cents")[0].get_text()
        resultado_promo = f"R$ {precoPromo},{centavos_promo}"

        oferta = site.find("div", class_="ui-pdp-promotions-pill-label", string="OFERTA DO DIA")
        if oferta:
            oferta_texto = "ATENÇÃO: Oferta do dia!"
        else:
            oferta_texto = "OFERTA DO DIA não encontrada."

        return jsonify({
            'title': titulo,
            'normal_price': resultado_normal,
            'promo_price': resultado_promo,
            'offer_info': oferta_texto
        })

    except Exception as e:
        return jsonify({'error': f'Erro durante a solicitação de scraping: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
