from sqlite3 import IntegrityError
from sqlalchemy import Text
from __init__ import app, db
from model.user import User
from model.group import Group

class Quotes(db.Model):
    """
    Quotes Model
    The Quotes class represents an individual quote stored in the database.
    Attributes:
        id (db.Column): The primary key, an integer representing the unique identifier for the quote.
        _title (db.Column): A string representing the title (author) of the quote.
        _content (db.Column): A Text blob representing the content (quote text).
        _subject (db.Column): A string representing the subject or category of the quote.
    """
    __tablename__ = 'user_quotes'
    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String(255), nullable=False)
    _content = db.Column(db.String(255), nullable=False)
    _subject = db.Column(db.String(255), nullable=True)

    def __init__(self, title, content, subject):
        """
        Constructor for Quotes.
        Args:
            title (str): The title (author) of the quote.
            content (str): The content (quote text).
            subject (str): The subject or category of the quote.
        """
        self._title = title
        self._content = content
        self._subject = subject

    def create(self):
        """Add the quote to the database."""
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def read(self):
        """Return the quote as a dictionary."""
        data = {
            "id": self.id,
            "title": self._title,
            "content": self._content,
            "subject": self._subject
        }
        return data

    def update(self):
        """Update the quote in the database."""
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
        """Delete the quote from the database."""
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def restore(data):
        """Restore quotes from a list of data."""
        for quote_data in data:
            quote_data.pop('id', None)
            title = quote_data.get("title", None)
            quote = Quotes.query.filter_by(_title=title).first()
            if quote:
                quote.update()
            else:
                new_quote = Quotes(**quote_data)
                new_quote.create()

def initquotes():
    """Initialize quotes with some test data."""
    with app.app_context():
        db.create_all()
        quotes = [
            Quotes(title='Franklin D. Roosevelt', content='The only limit to our realization of tomorrow is our doubts of today.', subject='Leadership'),
            Quotes(title='Nelson Mandela', content='It always seems impossible until it is done.', subject='Inspiration'),
            Quotes(title='Albert Einstein', content='Life is like riding a bicycle. To keep your balance you must keep moving.', subject='Philosophy'),
            Quotes(title='Mahatma Gandhi', content='Be the change that you wish to see in the world.', subject='Peace'),
            Quotes(title='Winston Churchill', content='Success is not final, failure is not fatal: It is the courage to continue that counts.', subject='Perseverance'),
            Quotes(title='Oscar Wilde', content='Be yourself; everyone else is already taken.', subject='Identity')
        ]
        for quote in quotes:
            try:
                quote.create()
                print(f"Record created: {repr(quote)}")
            except IntegrityError:
                db.session.remove()
                print(f"Records exist or error: {quote._title}")
