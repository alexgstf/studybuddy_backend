from flask import request, jsonify, Blueprint
from model.database import db, StudyBuddyUser

sbuserapi = Blueprint('sbuserapi', __name__)

@sbuserapi.route('/api/addsbuser', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    date_of_birth = data.get('date_of_birth')
    city = data.get('city')

    if not all([name, email, date_of_birth, city]):
        return jsonify({'error': 'Missing data'}), 400

    new_user = StudyBuddyUser(name=name, email=email, date_of_birth=date_of_birth, city=city)
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

    return jsonify({'message': 'User added successfully'}), 201


@sbuserapi.route('/api/getsbusers', methods=['GET'])
def get_sbusers():
    # Fetch all quotes from the database
    sbusers = StudyBuddyUser.query.all()
    result = [
        {
            'id': sbuser.id,
            'name': sbuser._name,
            'email': sbuser._email,
            'date_of_birth': sbuser._date_of_birth,
            'city': sbuser._city
        }
        for sbuser in sbusers
    ]
    return jsonify(result), 200

@sbuserapi.route('/api/deletesbuser/<int:id>', methods=['DELETE'])
def delete_user(id):
    sbuser = StudyBuddyUser.query.get(id)
    if not sbuser:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(sbuser)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

@sbuserapi.route('/api/updatesbuser/<int:id>', methods=['PUT'])
def update_quote(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    date_of_birth = data.get('date_of_birth')
    city = data.get('city')

    if not all([name, email, date_of_birth, city]):
        return jsonify({'error': 'Missing data'}), 400

    existing_sbuser = StudyBuddyUser.query.get(id)
    if not existing_sbuser:
        return jsonify({'error': 'User not found'}), 404

    existing_sbuser._name = name
    existing_sbuser._email = email
    existing_sbuser._date_of_birth = date_of_birth
    existing_sbuser._city = city

    db.session.commit()

    return jsonify({'message': 'User updated successfully'}), 200
