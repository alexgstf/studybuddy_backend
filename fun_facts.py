import requests
from flask import Flask, jsonify, Blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')

API_KEY = 'wst0VfOlvrz1Ez8qZ0kwlA==ieAYvEeSNj6O7jNx'  # API key from API Ninja
API_URL = 'https://api.api-ninjas.com/v1/facts'

# Create a blueprint for facts
facts_api = Blueprint('facts_api', __name__)

def fetch_fact_from_api():
    """Fetch a random fact from the API Ninja service"""
    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            fact_data = response.json()
            return fact_data[0]['fact'] if fact_data else 'No fact available at the moment.'
        else:
            return f'Failed to fetch fact. Status code: {response.status_code}'
    except Exception as e:
        return f'Error: {str(e)}'

@facts_api.route('/api/funfacts/random', methods=['GET'])
def random_fact():
    """API endpoint to return a random fun fact"""
    fact = fetch_fact_from_api()
    return jsonify({"fact": fact})

# Register the facts_api blueprint
app.register_blueprint(facts_api)

@app.route('/')
def home_page():
    return """
    <html>
    <head>
        <title>Fun Fact Generator</title>
    </head>
    <body>
        <h1>Welcome to the Fun Fact Generator!</h1>
        <p>Click the button below to generate a random fun fact!</p>
        <button id="fetch-fact">Get Fun Fact</button>
        <p id="fact">Your fun fact will appear here.</p>
        <script>
            async function fetchRandomFact() {
                try {
                    const response = await fetch('http://127.0.0.1:5001/api/funfacts/random');
                    if (response.ok) {
                        const data = await response.json();
                        document.getElementById('fact').innerText = data.fact;
                    } else {
                        console.error('Failed to fetch fact');
                    }
                } catch (error) {
                    console.error('Error fetching fact:', error);
                }
            }
            document.getElementById('fetch-fact').addEventListener('click', fetchRandomFact);
        </script>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run(port=5001)
