from sqlite3 import IntegrityError
from sqlalchemy import Text
from __init__ import app, db
from model.user import User
from model.group import Group

class Quotes(db.Model):
    """
    NestPost Model
    The Post class represents an individual contribution or discussion within a group.
    Attributes:
        id (db.Column): The primary key, an integer representing the unique identifier for the post.
        _title (db.Column): A string representing the title of the post.
        _content (db.Column): A Text blob representing the content of the post.
        _user_id (db.Column): An integer representing the user who created the post.
        _group_id (db.Column): An integer representing the group to which the post belongs.
    """
    __tablename__ = 'user_quotes'
    id = db.Column(db.Integer, primary_key=True)
    _author = db.Column(db.String(255), nullable=False)
    _quote = db.Column(db.String(255), nullable=False, unique=True)
    _date = db.Column(db.String(255), nullable=True)
   
    def __init__(self, author, quote, date):
        """
        Constructor, 1st step in object creation.
        Args:
            title (str): The title of the post.
            content (str): The content of the post.
            user_id (int): The user who created the post.
            group_id (int): The group to which the post belongs.
            image_url (str): The url path to the image
        """
        self._author = author
        self._quote = quote
        self._date = date
    # def __repr__(self):
    #     """
    #     The __repr__ method is a special method used to represent the object in a string format.
    #     Called by the repr(post) built-in function, where post is an instance of the Post class.
    #     Returns:
    #         str: A text representation of how to create the object.
    #     """
    #     return f"Post(id={self.id}, title={self._name}, content={self._email}, user_id={self._date_of_birth}, post_id={self._city})"
    def create(self):
        """
        The create method adds the object to the database and commits the transaction.
        Uses:
            The db ORM methods to add and commit the transaction.
        Raises:
            Exception: An error occurred when adding the object to the database.
        """
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    def read(self):
        """
        The read method retrieves the object data from the object's attributes and returns it as a dictionary.
        Uses:
            The Group.query and User.query methods to retrieve the group and user objects.
        Returns:
            dict: A dictionary containing the post data, including user and group names.
        """
        
        data = {
            "id": self.id,
            "author": self._author,
            "quote": self._quote,
            "date": self._date
        }
        return data
    def update(self, users):
        """
        The update method commits the transaction to the database.
        Uses:
            The db ORM method to commit the transaction.
        Raises:
            Exception: An error occurred when updating the object in the database.
        """
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    def delete(self):
        """
        The delete method removes the object from the database and commits the transaction.
        Uses:
            The db ORM methods to delete and commit the transaction.
        Raises:
            Exception: An error occurred when deleting the object from the database.
        """
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    @staticmethod
    def restore(data):
        for sbuser_data in data:
            _ = sbuser_data.pop('id', None)
            author = sbuser_data.get("author", None)
            sbuser = Quotes.query.filter_by(_author=author).first()
            if sbuser:
                sbuser.update(sbuser_data)
            else:
                sbuser = Quotes(**sbuser_data)
                sbuser.update(sbuser_data)
                sbuser.create()
# No inital data currently, deemed unnecessary at the current moment due to the lack of need in testing
def initquotes():
    """
    The initPosts function creates the Post table and adds tester data to the table.
    Uses:
        The db ORM methods to create the table.
    Instantiates:
        Post objects with tester data.
    Raises:
        IntegrityError: An error occurred when adding the tester data to the table.
    """
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        p1 = Quotes(author='Franklin D. Roosevelt', quote='The only limit to our realization of tomorrow is our doubts of today.', date='1945')
        p2 = Quotes(author='Nelson Mandela', quote='It always seems impossible until it is done.', date='1990')
        p3 = Quotes(author='Albert Einstein', quote='Life is like riding a bicycle. To keep your balance you must keep moving.', date='1930')
        p4 = Quotes(author='Mahatma Gandhi', quote='Be the change that you wish to see in the world.', date='1915')
        p5 = Quotes(author='Winston Churchill', quote='Success is not final, failure is not fatal: It is the courage to continue that counts.', date='1941')
        p6 = Quotes(author='Oscar Wilde', quote='Be yourself; everyone else is already taken.', date='1890')

        for post in [p1, p2, p3, p4, p5, p6]:
            try:
                post.create()
                print(f"Record created: {repr(post)}")
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {post.uid}")