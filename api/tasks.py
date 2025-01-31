from flask import Blueprint, jsonify, request
import random

# Create a blueprint for tasks
tasks_api = Blueprint('tasks_api', __name__)

# Tasks categorized by College Board Big Idea 1
TASKS = {
    "Big Idea 1 - Creative Development": [
        "Review the key concepts from your last CSP lesson.",
        "Read a chapter from your CSP textbook or an article on a related topic.",
        "Teach someone else a concept you just learned in CSP.",
        "Brainstorm ideas for a new coding project related to CSP.",
        "Create a flowchart or diagram to help explain a concept you just learned.",
        "Work on a creative coding project to apply what you've learned in CSP.",
        "Explore different programming languages and see how they relate to CSP concepts."
    ],
    "Big Idea 1 - Algorithms and Programming": [
        "Practice solving coding problems for 30 minutes.",
        "Write a summary of what you learned today in your CSP course.",
        "Work on an online coding quiz or challenge related to CSP.",
        "Write a simple algorithm to solve a real-world problem.",
        "Create a program that implements sorting or searching algorithms.",
        "Test an algorithm with different datasets and observe its performance.",
        "Debug a piece of code and explain what went wrong and how you fixed it."
    ],
    "Big Idea 1 - Data and Analysis": [
        "Create a mind map to visualize concepts in your CSP coursework.",
        "Research a topic related to your CSP studies and take notes.",
        "Summarize a CSP lecture or class discussion you attended recently.",
        "Collect and analyze data for a coding project or experiment.",
        "Create a spreadsheet to organize your study materials or project data.",
        "Use a tool to visualize a set of data and explain the patterns.",
        "Review your notes on databases and relational data models."
    ]
}


def fetch_task_from_category(category):
    """
    Fetch a random task from the specified category.
    """
    if category in TASKS:
        return random.choice(TASKS[category])
    else:
        return None


@tasks_api.route('/api/random-tasks', methods=['GET'])
def random_task():
    """
    Endpoint to return a random task from the local JSON data or based on a specific category.
    """
    category = request.args.get('category')
    if category:
        task = fetch_task_from_category(category)
        if task:
            return jsonify({"task": task})
        else:
            return jsonify({"error": "Category not found"}), 404
    else:
        task = random.choice([task for category in TASKS.values() for task in category])
        return jsonify({"task": task})
