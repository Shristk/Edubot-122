from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

# Path to the JSON data file
DATA_FILE = os.path.join("data", "career_support_intents.json")

# Load intents from the JSON file
def load_intents():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Fetch response for user input based on the pattern-response pairing
def get_response(user_message):
    intents = load_intents()["intents"]
    user_message = user_message.lower()
    
    for intent in intents:
        # Iterate through pattern-response pairs
        for pr in intent["patterns_responses"]:
            if user_message == pr["pattern"].lower():
                return pr["response"]
    return "I'm sorry, I didn't understand that. Could you please rephrase?"

# Route for the home page
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint to handle predictions
@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"response": "Please type something to get advice!"})
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
