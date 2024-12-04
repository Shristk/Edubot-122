# career_advisor/app/app.py

from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load model and vectorizer
with open("model/model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.json["skill"]
    X = vectorizer.transform([user_input])
    prediction = model.predict(X)[0]
    return jsonify({"career": prediction})

if __name__ == "__main__":
    app.run(debug=True)
