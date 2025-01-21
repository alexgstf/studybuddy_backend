from flask import request, jsonify, Blueprint
from model.quotesbase import db, Quotes

userquotes = Blueprint('userquotes', __name__)

@userquotes.route('/api/userquotes', methods=['POST'])
def add_user():
    data = request.get_json()
    author = data.get('author')
    quote = data.get('quote')
    date = data.get('date')

    if not all([author, quote, date]):
        return jsonify({'error': 'Missing data'}), 400

    new_user = Quotes(author=author, quote=quote, date=date)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Quote added successfully'}), 201

@userquotes.route('/api/userquotes', methods=['GET'])
def get_quotes():
    # Fetch all quotes from the database
    quotes = Quotes.query.all()
    result = [
        {
            'id': quote.id,
            'author': quote._author,
            'quote': quote._quote,
            'date': quote._date
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
    author = data.get('author')
    quote = data.get('quote')
    date = data.get('date')

    if not all([author, quote, date]):
        return jsonify({'error': 'Missing data'}), 400

    existing_quote = Quotes.query.get(id)
    if not existing_quote:
        return jsonify({'error': 'Quote not found'}), 404

    existing_quote._author = author
    existing_quote._quote = quote
    existing_quote._date = date

    db.session.commit()

    return jsonify({'message': 'Quote updated successfully'}), 200
