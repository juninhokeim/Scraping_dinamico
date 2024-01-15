from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def scrape_data(url):
    # Seu código de scraping aqui
    # Exemplo básico com Beautiful Soup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.text.strip()
    description = soup.find('meta', {'name': 'description'}).get('content').strip()
    # Adicione mais lógica conforme necessário

    return {'title': title, 'description': description}

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')

    try:
        result = scrape_data(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
