from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')

# Sample facts stored in a list
FACTS = [
    "Bananas are berries, but strawberries are not.",
    "Honey never spoils; archaeologists have found 3,000-year-old honey that is still edible.",
    "Octopuses have three hearts and blue blood.",
    "Sharks existed before trees.",
    "A day on Venus is longer than a year on Venus.",
    "There are more stars in the universe than grains of sand on all the Earth's beaches.",
    "Sloths can hold their breath longer than dolphins can."
]

# Create a blueprint for facts
facts_api = Blueprint('facts_api', __name__)

def fetch_fact_from_json():
    """Fetch a random fact from the local JSON data"""
    return random.choice(FACTS)

@facts_api.route('/api/funfacts/random', methods=['GET'])
def random_fact():
    """API endpoint to return a random fun fact"""
    fact = fetch_fact_from_json()
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
