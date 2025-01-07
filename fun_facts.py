from flask import Flask
from flask_cors import CORS
from API.facts import facts_api  # Import the facts blueprint from the API folder

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')

# Register the facts_api blueprint
app.register_blueprint(facts_api)

@app.route('/')
def home_page():
    return """
    <html>
    <head>
        <title>Fun Fact Generator</title>
    </head>
    <body>
        <h1>Welcome to the Fun Fact Generator!</h1>
        <p>Click the button below to generate a random fun fact!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=5001)
