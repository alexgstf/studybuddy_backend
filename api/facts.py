from flask import Blueprint, jsonify
import random

# Create a blueprint for facts
facts_api = Blueprint('facts_api', __name__)

# Local facts stored in a list
FACTS = [
    "Bananas are berries, but strawberries are not.",
    "Honey never spoils; archaeologists have found 3,000-year-old honey that is still edible.",
    "Octopuses have three hearts and blue blood.",
    "Sharks existed before trees.",
    "A day on Venus is longer than a year on Venus.",
    "There are more stars in the universe than grains of sand on all the Earth's beaches.",
    "Sloths can hold their breath longer than dolphins can."
]

def fetch_fact_from_json():
    """
    Fetch a random fact from the local JSON data.
    """
    return random.choice(FACTS)

@facts_api.route('/api/funfacts/random', methods=['GET'])
def random_fact():
    """
    Endpoint to return a random fun fact from the local JSON data.
    """
    fact = fetch_fact_from_json()
    return jsonify({"fact": fact})

