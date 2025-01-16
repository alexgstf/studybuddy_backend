from sqlite3 import IntegrityError
from sqlalchemy import Text
from __init__ import app, db
from model.user import User
from model.group import Group

class StudyBuddyUser(db.Model):
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
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), nullable=False, unique=True)
    _email = db.Column(db.String(255), nullable=False, unique=True)
    _date_of_birth = db.Column(db.Date, nullable=False)
    _city = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, date_of_birth, city):
        """
        Constructor, 1st step in object creation.
        Args:
            title (str): The title of the post.
            content (str): The content of the post.
            user_id (int): The user who created the post.
            group_id (int): The group to which the post belongs.
            image_url (str): The url path to the image
        """
        self._name = name
        self._email = email
        self._date_of_birth = date_of_birth
        self._city = city
    def __repr__(self):
        """
        The __repr__ method is a special method used to represent the object in a string format.
        Called by the repr(post) built-in function, where post is an instance of the Post class.
        Returns:
            str: A text representation of how to create the object.
        """
        return f"Post(id={self.id}, title={self._name}, content={self._email}, user_id={self._date_of_birth}, post_id={self._city})"
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
        user = User.query.get(self._user_id)
        data = {
            "id": self.id,
            "name": self._name,
            "email": self._email,
            "user_name": user.name if user else None,
            # Review information as this may not work as this is a quick workaround
            "date_of_birth": self._date_of_birth,
            "city": self._city
        }
        return data
    def update(self):
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
# No inital data currently, deemed unnecessary at the current moment due to the lack of need in testing
def initNestPosts():
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
        p1 = StudyBuddyUser(name='Alice', email='alice@example.com', date_of_birth='1990-01-01', city='New York')
        p2 = StudyBuddyUser(name='Bob', email='bob@example.com', date_of_birth='1985-05-12', city='Los Angeles')
        p3 = StudyBuddyUser(name='Charlie', email='charlie@example.com', date_of_birth='1992-08-23', city='Chicago')
        p4 = StudyBuddyUser(name='Diana', email='diana@example.com', date_of_birth='1988-11-30', city='Houston')
        for post in [p1, p2, p3, p4]:
            try:
                post.create()
                print(f"Record created: {repr(post)}")
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {post.uid}")