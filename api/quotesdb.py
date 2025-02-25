from flask import request, jsonify, Blueprint
from model.quotesbase import db, Quotes

userquotes = Blueprint('userquotes', __name__)

@userquotes.route('/api/userquotes', methods=['POST'])
def add_user():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    subject = data.get('subject')

    if not all([title, content, subject]):
        return jsonify({'error': 'Missing data'}), 400

    new_user = Quotes(title=title, content=content, subject=subject)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Notes added successfully'}), 201

@userquotes.route('/api/userquotes', methods=['GET'])
def get_quotes():
    # Fetch all contents from the database
    contents = contents.query.all()
    result = [
        {
            'id': content.id,
            'title': content._title,
            'content': content._content,
            'subject': content._subject
        }
        for content in contents
    ]
    return jsonify(result), 200

@userquotes.route('/api/userquotes/<int:id>', methods=['DELETE'])
def delete_quote(id):
    content = Quotes.query.get(id)
    if not content:
        return jsonify({'error': 'Notes not found'}), 404

    db.session.delete(content)
    db.session.commit()
    return jsonify({'message': 'Notes deleted successfully'}), 200

@userquotes.route('/api/userquotes/<int:id>', methods=['PUT'])
def update_quote(id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    subject = data.get('subject')

    if not all([title, content, subject]):
        return jsonify({'error': 'Missing data'}), 400

    existing_content = Quotes.query.get(id)
    if not existing_content:
        return jsonify({'error': 'Notes not found'}), 404

    existing_content._title = title
    existing_content._content = content
    existing_content._subject = subject

    db.session.commit()

    return jsonify({'message': 'Notes updated successfully'}), 200
