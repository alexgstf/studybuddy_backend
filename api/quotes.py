from flask import Blueprint, jsonify
import random

# Create a blueprint for quotes
quotes_api = Blueprint('quotes_api', __name__)

# Local quotes stored in a list
QUOTES = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "In the middle of every difficulty lies opportunity.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Your time is limited, so don't waste it living someone else's life."
]

def fetch_quote_from_json():
    """
    Fetch a random quote from the local JSON data.
    """
    return random.choice(QUOTES)

@quotes_api.route('/api/quotes/random', methods=['GET'])
def random_quote():
    """
    Endpoint to return a random quote from the local JSON data.
    """
    quote = fetch_quote_from_json()
    return jsonify({"quote": quote})
