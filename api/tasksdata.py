from flask import Blueprint, jsonify, request
from model.database import db, StudyTask
from sqlalchemy.exc import SQLAlchemyError
import random

# Create a blueprint for tasks
tasks_api = Blueprint('tasks_api', __name__)

@tasks_api.route('/api/tasks/add', methods=['POST'])
def add_task():
    """
    Endpoint to add a new task to the database.
    """
    data = request.get_json()
    description = data.get('description')

    if not description:
        return jsonify({'error': 'Task description is required'}), 400

    new_task = StudyTask(description=description)
    try:
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task added successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@tasks_api.route('/api/tasks/random', methods=['GET'])
def random_task():
    """
    Endpoint to return a random task from the database.
    """
    try:
        tasks = StudyTask.query.all()  # Fetch all tasks
        if not tasks:
            return jsonify({"message": "No tasks available"}), 404

        task = random.choice(tasks)  # Select a random task
        return jsonify({"task": task.description}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500


@tasks_api.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    """
    Endpoint to fetch all tasks.
    """
    try:
        tasks = StudyTask.query.all()
        tasks_list = [{"id": task.id, "description": task.description} for task in tasks]
        return jsonify(tasks_list), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500
