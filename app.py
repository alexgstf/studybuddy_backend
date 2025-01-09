from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')

@app.route('/api/darsh') 
def get_darsh():

    InfoDb = []

    InfoDb.append({
        "FirstName": "Darsh",
        "LastName": "Darsh",
        "DOB": "22 may 2007",
        "Residence": "San Diego",
        "Email": "darshdarsh@gmail.com",
        "Age": "17", 
        "Favorite Food": "Butter Chicken", 
    })
    
    return jsonify(InfoDb)

@app.route('/api/alexgustaf')
def get_alexgustaf():

    InfoDb = []

    InfoDb.append({
        "FirstName": "Alex",
        "LastName": "Gustaf",
        "DOB": "May 6 2007",
        "Residence": "San Diego",
        "Email": "alexgstf@gmail.com",
        "Age": "17",
        "Favorite Food": "Pizza"
    })

    return jsonify(InfoDb)
    
@app.route('/api/alexrubio')
def get_alexrubio():

    InfoDb = []

    InfoDb.append({
        "FirstName": "Alex",
        "LastName": "Rubio",
        "DOB": "July 11 2009",
        "Residence": "San Diego",
        "Email": "rubioalex688@gmail.com",
        "Age": "15"
    })
    
    return jsonify(InfoDb)

@app.route('/api/traviscallow')
def get_traviscallow():

    InfoDb = []
    InfoDb.append({
        "FirstName": "Travis",
        "LastName": "Callow",
        "DOB": "August 22 2008",
        "Residence": "San Diego",
        "Email": "travisgcallow@gmail.com",
        "Age": "16"
    })
    
    return jsonify(InfoDb)

@app.route('/api/marti') 
def get_marti():

    InfoDb = []

    InfoDb.append({
        "FirstName": "Marti",
        "LastName": "Jorba",
        "DOB": "24 june 2008",
        "Residence": "San Diego",
        "Email": "marti.jorba.mateu@gmail.com",
        "Age": "16",
        "Favorite Food": "Pasta",
        
    })
    
    return jsonify(InfoDb)

@app.route('/')
def say_hello():
    html_content = """
    <html>
    <head>
        <title>Study Buddy Team</title>
    </head>
    <body>
        <h2>Welcome to the apis of the study buddies</h2>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(port=5000)