from flask import Flask, Blueprint, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS


quiz_api = Blueprint('quiz_api', __name__, url_prefix='/api')
api = Api(quiz_api)

class QuizAPI:
    # Data storage for a single student's stats
    stats = {
        "xp": 0,
        "level": 1
    }

    # Helper function to calculate XP threshold for the current level
    @staticmethod
    def xp_threshold(level):
        return level * 10  # Threshold increases linearly with level

    # Function to handle leveling up
    @staticmethod
    def level_up():
        while QuizAPI.stats["xp"] >= QuizAPI.xp_threshold(QuizAPI.stats["level"]):
            QuizAPI.stats["xp"] -= QuizAPI.xp_threshold(QuizAPI.stats["level"])
            QuizAPI.stats["level"] += 1

    # Endpoint to retrieve current stats
    class _AllStats(Resource):
        def get(self):
            return jsonify(QuizAPI.stats)

    # Endpoint to submit quiz results
    class _SubmitQuiz(Resource):
        def post(self):
            data = request.json
            correct_answers = data.get('correct', 0)
            total_questions = data.get('total', 0)

            if total_questions == 0:
                return {"message": "Invalid quiz data"}, 400

            # Calculate percentage of correct answers
            percentage_correct = (correct_answers / total_questions) * 100

            # Award XP if at least 75% correct
            if percentage_correct >= 75:
                QuizAPI.stats["xp"] += correct_answers

            # Handle leveling up
            QuizAPI.level_up()

            return jsonify(QuizAPI.stats)

    # Register endpoints
    api.add_resource(_AllStats, '/stats')
    api.add_resource(_SubmitQuiz, '/submit')


