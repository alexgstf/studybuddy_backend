from flask import Blueprint, jsonify
from flask_restful import Api, Resource

student_api = Blueprint('student_api', __name__, url_prefix='/api')
api = Api(student_api)

class StudentAPI:
    # Data storage for all students
    students = {
        "alex": {"name": "Alex", "age": "17", "class": "CSP"},
        "alejandro": {"name": "Alejandro", "age": "15", "class": "CSP"},
        "darsh": {"name": "Darsh", "age": "17", "class": "CSP"},
        "marti": {"name": "Marti", "age": "16", "class": "CSP"},
        "travis": {"name": "Travis", "age": "16", "class": "CSP"}
    }

    # Endpoint for all students
    class _AllStudents(Resource):
        def get(self):
            return jsonify(StudentAPI.students)

    # Endpoint for a specific student
    class _Student(Resource):
        def get(self, name):
            student = StudentAPI.students.get(name.lower())  # Case-insensitive lookup
            if student:
                return jsonify(student)
            return {"message": "Student not found"}, 404

    # Register endpoints
    api.add_resource(_AllStudents, '/student')
    api.add_resource(_Student, '/student/<string:name>')