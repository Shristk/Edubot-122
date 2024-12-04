# career_advisor/app/chatbot.py

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load data
data = pd.read_csv("data/career_datacopy.csv")

# Vectorize Skills
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["Skill"])
y = data["Recommended_Career"]

# Train a model
model = MultinomialNB()
model.fit(X, y)

# Save the model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Model and vectorizer saved to model.pkl.")
