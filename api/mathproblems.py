from flask import Blueprint, jsonify
import random

# Create a blueprint for math problems
math_api = Blueprint('math_api', __name__)

# Local math problems stored in a list
MATH_PROBLEMS = [
    "What is 5 + 7?",
    "Solve for x: 2x + 3 = 7",
    "What is the area of a circle with radius 4?",
    "Simplify: (3 + 5) * 2",
    "What is 12 divided by 4?"
]

def fetch_math_problem_from_json():
    """
    Fetch a random math problem from the local JSON data.
    """
    return random.choice(MATH_PROBLEMS)

@math_api.route('/api/math/random', methods=['GET'])
def random_math_problem():
    """
    Endpoint to return a random math problem from the local JSON data.
    """
    problem = fetch_math_problem_from_json()
    return jsonify({"math_problem": problem})
