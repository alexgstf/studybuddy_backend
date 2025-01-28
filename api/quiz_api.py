from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from model.quizbase import db, Statistics

userstats = Blueprint('userstats', __name__, url_prefix='/api')
api = Api(userstats)

class QuizAPI:
    # Helper function to calculate XP threshold for the current level
    @staticmethod
    def xp_threshold(level):
        return level * 10  # Threshold increases linearly with level

    # Function to handle leveling up
    @staticmethod
    def level_up(user_stats):
        while user_stats._xp >= QuizAPI.xp_threshold(user_stats._level):
            user_stats._xp -= QuizAPI.xp_threshold(user_stats._level)
            user_stats._level += 1

    # Endpoint to submit quiz results
    class _SubmitQuiz(Resource):
        def post(self):
            data = request.json
            user = data.get('user')
            correct_answers = data.get('correct', 0)
            total_questions = data.get('total', 0)

            if not user:
                return {"message": "User parameter is required"}, 400

            if total_questions == 0:
                return {"message": "Invalid quiz data"}, 400

            # Fetch or create user stats
            user_stats = Statistics.query.filter_by(_user=user).first()
            if not user_stats:
                user_stats = Statistics(xp=0, level=1, user=user)
                db.session.add(user_stats)

            # Calculate percentage of correct answers
            percentage_correct = (correct_answers / total_questions) * 100

            # Award XP if at least 75% correct
            if percentage_correct >= 75:
                user_stats._xp += correct_answers

            # Handle leveling up
            QuizAPI.level_up(user_stats)

            # Save changes to the database
            db.session.commit()

            return jsonify({"xp": user_stats._xp, "level": user_stats._level, "user": user})

    # Register endpoints
    api.add_resource(_SubmitQuiz, '/userstats')
