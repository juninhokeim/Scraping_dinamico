function executeScraping() {
    const urlInput = document.getElementById('urlInput').value;

    // Envie o link para o servidor Python
    fetch('http://127.0.0.1:5000/scrape', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: urlInput }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erro durante a solicitação: ${response.status} ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        displayResult(data);
    })
    .catch(error => {
        console.error('Erro durante a solicitação de scraping:', error);
        displayResult({ error: 'Erro durante a solicitação de scraping.' });
    });
}

function displayResult(data) {
    const resultContainer = document.getElementById('resultContainer');
    resultContainer.innerHTML = '';

    if (data.error) {
        resultContainer.innerHTML = `<p>${data.error}</p>`;
    } else {
        resultContainer.innerHTML = `
            <h2>Dados Raspados:</h2>
            <p>Título: ${data.title}</p>
            <p>Preço Normal: ${data.normal_price}</p>
            <p>Preço Promoção: ${data.promo_price}</p>
            <p>${data.offer_info}</p>
        `;
    }
}
