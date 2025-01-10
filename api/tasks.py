from flask import Blueprint, jsonify
import random

# Create a blueprint for tasks
tasks_api = Blueprint('tasks_api', __name__)

# Local tasks stored in a list
TASKS = [
    "Review the key concepts from your last lesson.",
    "Read an article or a chapter from your textbook.",
    "Practice solving math problems for 30 minutes.",
    "Write a summary of what you learned today.",
    "Watch a tutorial on a subject you're struggling with.",
    "Teach someone else a concept you just learned.",
    "Practice a foreign language for 20 minutes.",
    "Complete a set of practice questions.",
    "Create a mind map to visualize your learning.",
    "Research a topic related to your studies and take notes.",
    "Read a scientific paper or journal article.",
    "Summarize a lecture you attended recently.",
    "Create flashcards for important concepts.",
    "Work on an online quiz related to your subject.",
    "Set specific goals for your next study session.",
    "Organize your study materials and notes.",
    "Review your last exam or quiz and identify areas for improvement.",
    "Watch an educational video related to your field of study.",
    "Join an online study group to discuss challenging topics.",
    "Write a reflection on your learning progress this week."
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
