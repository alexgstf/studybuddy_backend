from sqlite3 import IntegrityError
from __init__ import app, db
from model.user import User  # Ensure you have a User model

class Task(db.Model):
    """
    Task Model
    Represents a task assigned to a specific user.
    Attributes:
        id (db.Column): The primary key, an integer representing the unique identifier for the task.
        _task (db.Column): A string representing the task description.
        _user_id (db.Column): An integer representing the user who created the task.
    """
    __tablename__ = 'user_tasks'
    id = db.Column(db.Integer, primary_key=True)
    _task = db.Column(db.String(255), nullable=False, unique=True)
    _user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Link to User model

    # Establishing relationship with User model
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def __init__(self, task, user_id):
        """
        Constructor, initializes a task.
        Args:
            task (str): The description of the task.
            user_id (int): The ID of the user creating the task.
        """
        self._task = task
        self._user_id = user_id

    def __repr__(self):
        """
        Returns a string representation of the Task object.
        """
        return f"Task(id={self.id}, task={self._task}, user_id={self._user_id})"

    def create(self):
        """
        Adds the task to the database and commits the transaction.
        """
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def read(self):
        """
        Retrieves task details as a dictionary.
        """
        return {
            "id": self.id,
            "task": self._task,
            "user_id": self._user_id
        }

    def update(self, new_task):
        """
        Updates the task's description.
        Args:
            new_task (str): The new task description.
        """
        try:
            self._task = new_task
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
        """
        Removes the task from the database and commits the transaction.
        """
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def restore(data):
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
def inittasks():
    """
    Initializes database with sample tasks.
    """
    with app.app_context():
        db.create_all()  # Create tables

        # Sample tasks
        tasks = [
            Task(task='Review the key concepts from your last lesson.', user_id=1),
            Task(task='Read an article or a chapter from your textbook.', user_id=2),
            Task(task='Practice solving math problems for 30 minutes.', user_id=1),
            Task(task='Write a summary of what you learned today.', user_id=2)
        ]

        for task in tasks:
            try:
                task.create()
                print(f"Record created: {repr(task)}")
            except IntegrityError:
                db.session.remove()
                print(f"Task already exists or error occurred: {task._task}")
