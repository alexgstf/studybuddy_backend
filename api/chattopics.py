from flask import Blueprint, jsonify

# Create a blueprint for tasks
topics_api = Blueprint('topics', __name__)

# Local tasks stored in a list
TOPICS = [
    {"topic": "General", "description": "A place for general discussion on various topics."},
    {"topic": "Math", "description": "Mathematical concepts, problems, and solutions."},
    {"topic": "Science", "description": "Scientific theories, experiments, and discoveries."},
    {"topic": "English", "description": "Literature, grammar, and language arts."},
    {"topic": "History", "description": "Historical events, figures, and periods."},
    {"topic": "CSP", "description": "Programming, algorithms, and computer science."}
]

@topics_api.route('/api/topics', methods=['GET'])
def return_topics():
    """
    Endpoint to return topics from the local JSON data.
    """
    return jsonify(TOPICS)
