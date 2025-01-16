from flask import request, jsonify, Blueprint
from model.factsbase import db, Facts

userfacts = Blueprint('userfacts', __name__)

@userfacts.route('/api/userfacts', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    fact = data.get('fact')
    

    if not all([name, fact]):
        return jsonify({'error': 'Missing data'}), 400

    new_user = Facts(name=name, fact=fact)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Fact added successfully'}), 201


