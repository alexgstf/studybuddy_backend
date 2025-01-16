from flask import request, jsonify, Blueprint
from model.database import db, StudyBuddyUser

sbuserapi = Blueprint('sbuserapi', __name__)

@sbuserapi.route('/api/add_sb_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    date_of_birth = data.get('date_of_birth')
    city = data.get('city')

    if not all([name, email, date_of_birth, city]):
        return jsonify({'error': 'Missing data'}), 400

    new_user = StudyBuddyUser(name=name, email=email, date_of_birth=date_of_birth, city=city)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201