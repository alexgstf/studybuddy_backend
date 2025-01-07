import requests
from flask import Blueprint, jsonify

# Create a blueprint for facts
facts_api = Blueprint('facts_api', __name__)

# API key and endpoint configuration
API_KEY = 'wst0VfOlvrz1Ez8qZ0kwlA==ieAYvEeSNj6O7jNx'  # Replace with your actual API key
API_URL = 'https://api.api-ninjas.com/v1/facts'

def fetch_fact_from_api():
    """
    Fetch a random fact from the external API.
    """
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
    """
    Endpoint to return a random fun fact.
    """
    fact = fetch_fact_from_api()
    return jsonify({"fact": fact})

