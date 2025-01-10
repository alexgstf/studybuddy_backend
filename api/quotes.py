from flask import Blueprint, jsonify
import random

# Create a blueprint for quotes
quotes_api = Blueprint('quotes_api', __name__)

# Local quotes stored in a list of dictionaries
QUOTES = [
    {"quote": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt", "date": "1945"},
    {"quote": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein", "date": "1920"},
    {"quote": "Success is not the key to happiness. Happiness is the key to success.", "author": "Albert Schweitzer", "date": "1952"},
    {"quote": "Life is 10% what happens to us and 90% how we react to it.", "author": "Charles R. Swindoll", "date": "1980"},
    {"quote": "Your time is limited, so don't waste it living someone else's life.", "author": "Steve Jobs", "date": "2005"}
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
    return jsonify(quote)
