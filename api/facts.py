from flask import Blueprint, jsonify
import random

# Create a blueprint for facts
facts_api = Blueprint('facts_api', __name__)

# Local facts stored in a list
FACTS = [
    "Bananas are berries, but strawberries are not.",
    "Honey never spoils; archaeologists have found 3,000-year-old honey that is still edible.",
    "Octopuses have three hearts and blue blood.",
    "Sharks existed before trees.",
    "A day on Venus is longer than a year on Venus.",
    "There are more stars in the universe than grains of sand on all the Earth's beaches.",
    "Sloths can hold their breath longer than dolphins can.",
    "Wombat poop is cube-shaped.",
    "A group of flamingos is called a 'flamboyance.'",
    "The heart of a blue whale is the size of a small car.",
    "Pineapples take about two years to grow.",
    "A bolt of lightning is five times hotter than the surface of the sun.",
    "Cows have best friends and get stressed when separated from them.",
    "Butterflies taste with their feet.",
    "Antarctica is the only continent without native ants.",
    "Theres a species of jellyfish that can live forever by reverting to its immature state.",
    "The Eiffel Tower can grow up to six inches taller in summer due to heat expansion.",
    "Humans share about 60percent DNA with bananas.",
    "Theres enough DNA in the human body to stretch from the sun to Pluto and back — 17 times.",
    "The first oranges werent orange; they were green.",
    "Some cats are allergic to humans.",
    "The inventor of the Pringles can is buried in one.",
    "Koalas have fingerprints that are almost indistinguishable from humans.",
    "Your nose and ears never stop growing.",
    "Sea otters hold hands while they sleep to keep from drifting apart.",
    "A small child could swim through the veins of a blue whale.",
    "There are more trees on Earth than stars in the Milky Way.",
    "The Empire State Building has its own ZIP code.",
    "Coca-Cola was the first soft drink consumed in space.",
    "Mosquitoes are the deadliest animals in the world.",
    "The shortest war in history lasted only 38 minutes (Anglo-Zanzibar War).",
    "An octopus has nine brains: one central brain and a smaller one in each of its eight arms.",
    "Rats laugh when theyre tickled.",
    "A cloud can weigh more than a million pounds.",
    "The inventor of the modern flushing toilet was named Thomas Crapper.",
    "Some turtles can breathe through their butts.",
    "A cockroach can live for weeks without its head.",
    "Apples float because they are 25percent air.",
    "Elephants are the only animals that can't jump.",
    "A snail can sleep for three years.",
    "The fingerprints of a koala are so indistinguishable from humans that theyve been mistaken at crime scenes.",
    "The longest hiccuping spree lasted 68 years.",
    "Venus is the only planet in the solar system that spins clockwise.",
    "The average human will spend six months of their life waiting for red lights to turn green.",
    "More people are killed annually by vending machines than sharks.",
    "A shrimps heart is in its head.",
    "The dot over the lowercase letters 'i' and 'j' is called a tittle.",
    "A crocodile cannot stick its tongue out.",
    "A single strand of spaghetti is called a spaghetto.",
    "The word 'set' has the most definitions in the English language.",
    "Cats have fewer toes on their back paws than on their front paws.",
    "A sneeze can travel up to 100 miles per hour.",
    "Hot water freezes faster than cold water under certain conditions (known as the Mpemba effect).",
    "The smell of freshly cut grass is actually a plant distress call.",
    "Owls can't move their eyeballs.",
    "Goats have rectangular pupils, which give them a wide field of vision.",
    "The first alarm clock could only ring at 4 a.m.",
    "Dolphins have names for each other.",
    "An ant can lift 50 times its own weight.",
    "Humans have a second brain in their gut, called the enteric nervous system."
]

def fetch_fact_from_json():
    """
    Fetch a random fact from the local JSON data.
    """
    return random.choice(FACTS)

@facts_api.route('/api/funfacts/random', methods=['GET'])
def random_fact():
    """
    Endpoint to return a random fun fact from the local JSON data.
    """
    fact = fetch_fact_from_json()
    return jsonify({"fact": fact})

