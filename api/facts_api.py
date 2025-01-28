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

@userfacts.route('/api/userfacts', methods=['GET'])
def get_fact():
    # Fetch all facts from the database
    facts = Facts.query.all()
    result = [
        {
            'id': fact.id,
            'name': fact._name,
            'fact': fact._fact,
        }
        for fact in facts
    ]
    return jsonify(result), 200

@userfacts.route('/api/userfacts/<int:id>', methods=['DELETE'])
def delete_facts(id):
    fact = Facts.query.get(id)
    if not fact:
        return jsonify({'error': 'Fact not found'}), 404

    db.session.delete(fact)
    db.session.commit()
    return jsonify({'message': 'Fact deleted successfully'}), 200

@userfacts.route('/api/userfacts/<int:id>', methods=['PUT'])
def update_fact(id):
    data = request.get_json()
    name = data.get('name')
    fact = data.get('fact')

    if not all([name, fact]):
        return jsonify({'error': 'Missing data'}), 400

    existing_fact = Facts.query.get(id)
    if not existing_fact:
        return jsonify({'error': 'Fact not found'}), 404
    existing_fact._name = name
    existing_fact._fact = fact
    db.session.commit()
    return jsonify({'message': 'Fact updated successfully'}), 200


