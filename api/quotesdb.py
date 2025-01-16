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

    return jsonify({'message': 'User added successfully'}), 201


