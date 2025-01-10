from flask import Blueprint, jsonify
import random

# Create a blueprint for quotes
quotes_api = Blueprint('quotes_api', __name__)

# Local quotes stored in a list of dictionaries
QUOTES = [
    {"quote": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt", "date": "1945"},
    {"quote": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein", "date": "1920"},
    {"quote": "Success is not the key to happiness. Happiness is the key to success.", "author": "Albert Schweitzer", "date": "1952"},
    {"quote": "Life is 10% what happens to us and 90% how we react to it.", "author": "Charles R. Swindoll", "date": "1980"},
    {"quote": "Your time is limited, so don't waste it living someone else's life.", "author": "Steve Jobs", "date": "2005"},
    {"quote": "The best way to predict the future is to create it.", "author": "Abraham Lincoln", "date": "1862"},
    {"quote": "It always seems impossible until it's done.", "author": "Nelson Mandela", "date": "1994"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt", "date": "1900"},
    {"quote": "You miss 100% of the shots you don't take.", "author": "Wayne Gretzky", "date": "1983"},
    {"quote": "Do not go where the path may lead, go instead where there is no path and leave a trail.", "author": "Ralph Waldo Emerson", "date": "1860"},
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs", "date": "2005"},
    {"quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us.", "author": "Ralph Waldo Emerson", "date": "1841"},
    {"quote": "The journey of a thousand miles begins with one step.", "author": "Lao Tzu", "date": "6th century BC"},
    {"quote": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson", "date": "1980"},
    {"quote": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau", "date": "1854"},
    {"quote": "Hardships often prepare ordinary people for an extraordinary destiny.", "author": "C.S. Lewis", "date": "1952"},
    {"quote": "Opportunities don't happen, you create them.", "author": "Chris Grosser", "date": "2011"},
    {"quote": "Everything you can imagine is real.", "author": "Pablo Picasso", "date": "1955"},
    {"quote": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis", "date": "1955"},
    {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius", "date": "5th century BC"},
    {"quote": "Success is not in what you have, but who you are.", "author": "Bo Bennett", "date": "2007"},
    {"quote": "Don't limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you.", "author": "Mary Kay Ash", "date": "1995"},
    {"quote": "You have to be odd to be number one.", "author": "Dr. Seuss", "date": "1971"},
    {"quote": "Keep your face always toward the sunshine—and shadows will fall behind you.", "author": "Walt Whitman", "date": "1888"},
    {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt", "date": "1960"},
    {"quote": "We cannot solve our problems with the same thinking we used when we created them.", "author": "Albert Einstein", "date": "1946"},
    {"quote": "In the end, we only regret the chances we didn't take.", "author": "Lewis Carroll", "date": "1865"},
    {"quote": "It’s not whether you get knocked down, it’s whether you get up.", "author": "Vince Lombardi", "date": "1969"},
    {"quote": "Don’t wait for the perfect moment. Take the moment and make it perfect.", "author": "Zoey Sayward", "date": "2015"},
    {"quote": "Act as if what you do makes a difference. It does.", "author": "William James", "date": "1900"},
    {"quote": "The harder you work for something, the greater you'll feel when you achieve it.", "author": "Unknown", "date": "2020"},
    {"quote": "You can't go back and change the beginning, but you can start where you are and change the ending.", "author": "C.S. Lewis", "date": "1955"},
    {"quote": "Doubt kills more dreams than failure ever will.", "author": "Suzy Kassem", "date": "2012"},
    {"quote": "It’s never too late to be what you might have been.", "author": "George Eliot", "date": "1860"},
    {"quote": "Everything you’ve ever wanted is on the other side of fear.", "author": "George Addair", "date": "2004"}
]

def fetch_quote_from_json():
    """
    Fetch a random quote from the local JSON data.
    """
    return random.choice(QUOTES)

@quotes_api.route('/api/quotes/random', methods=['GET'])
def random_quote():
    """
    Endpoint to return a random quote from the local JSON data.
    """
    quote = fetch_quote_from_json()
    return jsonify(quote)
