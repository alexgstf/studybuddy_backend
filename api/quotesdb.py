from flask import request, jsonify, Blueprint
from model.quotesbase import db, Quotes

userquotes = Blueprint('userquotes', __name__)

@userquotes.route('/api/userquotes', methods=['POST'])
def add_user():
    data = request.get_json()
    title = data.get('title')  # Changed from 'author' to 'title'
    content = data.get('content')  # Changed from 'quote' to 'content'
    subject = data.get('subject')  # Changed from 'date' to 'subject'

    if not all([title, content, subject]):
        return jsonify({'error': 'Missing data'}), 400

    new_quote = Quotes(title=title, content=content, subject=subject)
    db.session.add(new_quote)
    db.session.commit()

    return jsonify({'message': 'Quote added successfully'}), 201

@userquotes.route('/api/userquotes', methods=['GET'])
def get_quotes():
    quotes = Quotes.query.all()
    result = [
        {
            'id': quote.id,
            'title': quote._title,  # Changed from '_author' to '_title'
            'content': quote._content,  # Changed from '_quote' to '_content'
            'subject': quote._subject  # Changed from '_date' to '_subject'
        }
        for quote in quotes
    ]
    return jsonify(result), 200

@userquotes.route('/api/userquotes/<int:id>', methods=['DELETE'])
def delete_quote(id):
    quote = Quotes.query.get(id)
    if not quote:
        return jsonify({'error': 'Quote not found'}), 404

    db.session.delete(quote)
    db.session.commit()
    return jsonify({'message': 'Quote deleted successfully'}), 200

@userquotes.route('/api/userquotes/<int:id>', methods=['PUT'])
def update_quote(id):
    data = request.get_json()
    title = data.get('title')  # Changed from 'author' to 'title'
    content = data.get('content')  # Changed from 'quote' to 'content'
    subject = data.get('subject')  # Changed from 'date' to 'subject'

    if not all([title, content, subject]):
        return jsonify({'error': 'Missing data'}), 400

    existing_quote = Quotes.query.get(id)
    if not existing_quote:
        return jsonify({'error': 'Quote not found'}), 404

    existing_quote._title = title  # Changed from '_author' to '_title'
    existing_quote._content = content  # Changed from '_quote' to '_content'
    existing_quote._subject = subject  # Changed from '_date' to '_subject'

    db.session.commit()

    return jsonify({'message': 'Quote updated successfully'}), 200
