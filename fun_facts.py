import requests
from flask import Flask, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')

API_KEY = 'wst0VfOlvrz1Ez8qZ0kwlA==ieAYvEeSNj6O7jNx'  # Replace with your actual API key

def fetch_fact_from_api():
    api_url = 'https://api.api-ninjas.com/v1/facts'
    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            fact_data = response.json()
            return fact_data[0]['fact'] if fact_data else 'No fact available at the moment.'
        else:
            return f'Failed to fetch fact. Status code: {response.status_code}'
    except Exception as e:
        return f'Error: {str(e)}'

@app.route('/api/funfacts/random')
def random_fact():
    fact = fetch_fact_from_api()
    return jsonify({"fact": fact})

@app.route('/')
def home_page():
    html_content = """
    <html>
    <head>
        <title>Fun Fact Generator</title>
        <script>
            async function fetchRandomFact() {
                const response = await fetch('/api/funfacts/random');
                const data = await response.json();
                const factElement = document.getElementById('fact');
                
                // Add animation effect
                factElement.classList.add('fade-out');
                setTimeout(() => {
                    factElement.innerText = data.fact;
                    factElement.classList.remove('fade-out');
                    factElement.classList.add('fade-in');
                }, 500);
                setTimeout(() => {
                    factElement.classList.remove('fade-in');
                }, 1500);
            }
        </script>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
                color: #333;
            }
            h1 {
                color: #007BFF;
                font-size: 36px;
            }
            button {
                padding: 12px 24px;
                font-size: 18px;
                color: white;
                background-color: #28a745;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
                transition: background-color 0.3s, transform 0.2s;
            }
            button:hover {
                background-color: #218838;
                transform: translateY(-2px);
            }
            button:active {
                transform: translateY(2px);
            }
            #fact {
                margin-top: 20px;
                font-size: 20px;
                font-weight: 500;
                text-align: center;
                padding: 20px;
                max-width: 600px;
                background-color: #fff;
                border: 2px solid #007BFF;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                opacity: 1;
                transition: opacity 0.5s;
            }
            #fact.fade-out {
                opacity: 0;
            }
            #fact.fade-in {
                opacity: 1;
            }
        </style>
    </head>
    <body>
        <h1>Fun Fact Generator</h1>
        <p>Click the button below to learn something fascinating!</p>
        <button onclick="fetchRandomFact()">Generate Fun Fact</button>
        <p id="fact">Your fun fact will appear here!</p>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(port=5001)
