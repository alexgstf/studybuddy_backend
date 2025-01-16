from flask import request, jsonify, Blueprint
from model.quizbase import db, Statistics

userstats = Blueprint('userstats', __name__)

@userstats.route('/api/userstats', methods=['POST'])
def add_user():
    data = request.get_json()
    xp = data.get('xp')
    level = data.get('level')
    

    if not all([xp, level]):
        return jsonify({'error': 'Missing data'}), 400

    new_user = Statistics(xp=xp, level=level)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201