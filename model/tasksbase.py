from sqlite3 import IntegrityError
from __init__ import app, db
from model.user import User

class Task(db.Model):
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
    __tablename__ = 'user_tasks'
    id = db.Column(db.Integer, primary_key=True)
    _task = db.Column(db.String(255), nullable=False, unique=True)

<<<<<<< HEAD
    # Establishing relationship with User model
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def __init__(self, task, user_id):
=======
    def __init__(self, task):
>>>>>>> parent of d1ba34a (bakcend)
        """
        Constructor, 1st step in object creation.
        Args:
            title (str): The title of the post.
            content (str): The content of the post.
            user_id (int): The user who created the post.
            group_id (int): The group to which the post belongs.
            image_url (str): The url path to the image
        """
        self._task = task
    def __repr__(self):
        """
        The __repr__ method is a special method used to represent the object in a string format.
        Called by the repr(post) built-in function, where post is an instance of the Post class.
        Returns:
            str: A text representation of how to create the object.
        """
        return f"Task(id={self._task})"
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
            "task": self._task,
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
<<<<<<< HEAD
        """
        Restores tasks from given data.
        """
        for task_data in data:
            _ = task_data.pop('id', None)  # Remove 'id' to allow task to be added as a new task
            task = task_data.get("task", None)
            user_id = task_data.get("user_id", None)

            # Check if the task already exists for this user
            existing_task = Task.query.filter_by(_task=task, _user_id=user_id).first()
            if existing_task:
                existing_task.update(task_data)  # Update if task exists
            else:
                new_task = Task(**task_data)  # Create new task if it doesn't exist
                new_task.create()

# Function to initialize sample tasks
=======
        for sbuser_data in data:
            _ = sbuser_data.pop('id', None)
            task = sbuser_data.get("task", None)
            sbuser = Task.query.filter_by(_task=task).first()
            if sbuser:
                sbuser.update(sbuser_data)
            else:
                sbuser = Task(**sbuser_data)
                sbuser.update(sbuser_data)
                sbuser.create()
# No inital data currently, deemed unnecessary at the current moment due to the lack of need in testing
>>>>>>> parent of d1ba34a (bakcend)
def inittasks():
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
<<<<<<< HEAD
        db.create_all()  # Create tables

        # Sample tasks
        tasks = [
            Task(task='Review the key concepts from your last lesson.', user_id=1),
            Task(task='Read an article or a chapter from your textbook.', user_id=2),
            Task(task='Practice solving math problems for 30 minutes.', user_id=1),
            Task(task='Write a summary of what you learned today.', user_id=2)
        ]

        for task in tasks:
=======
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        p1 = Task(task='Review the key concepts from your last lesson.')
        p2 = Task(task='Read an article or a chapter from your textbook.')
        p3 = Task(task='Practice solving math problems for 30 minutes.')
        p4 = Task(task='Write a summary of what you learned today.')
        for post in [p1, p2, p3, p4]:
>>>>>>> parent of d1ba34a (bakcend)
            try:
                post.create()
                print(f"Record created: {repr(post)}")
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {post.uid}")