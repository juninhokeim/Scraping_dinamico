function executeScraping() {
    const urlInput = document.getElementById('urlInput').value;

    // Envie o link para o servidor Python
    fetch('/scrape', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: urlInput }),
    })
    .then(response => response.json())
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
        // Exiba os dados raspados na página
        const { title, description, price, rating } = data;
        resultContainer.innerHTML = `
            <h2>Dados Raspados:</h2>
            <p>Título: ${title}</p>
            <p>Descrição: ${description}</p>
            <p>Preço: ${price}</p>
            <p>Avaliação: ${rating}</p>
        `;
    }
}
