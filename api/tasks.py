from flask import Blueprint, jsonify
import random

# Create a blueprint for tasks
tasks_api = Blueprint('tasks_api', __name__)

# Local tasks stored in a list
TASKS = [
    "Organize your workspace.",
    "Read for 20 minutes.",
    "Practice coding for 30 minutes.",
    "Go for a 10-minute walk.",
    "Write down three things you're grateful for.",
    "Try a new recipe.",
    "Call a friend you haven't spoken to in a while."
]

def fetch_task_from_json():
    """
    Fetch a random task from the local JSON data.
    """
    return random.choice(TASKS)

@tasks_api.route('/api/tasks/random', methods=['GET'])
def random_task():
    """
    Endpoint to return a random task from the local JSON data.
    """
    task = fetch_task_from_json()
    return jsonify({"task": task})
