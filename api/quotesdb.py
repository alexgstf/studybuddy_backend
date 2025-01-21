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
