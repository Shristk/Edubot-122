# career_advisor/data/generate_data.py

import pandas as pd
import random

def generate_synthetic_data():
    careers = [
        "Software Developer", "Data Scientist", "Web Designer",
        "Digital Marketer", "Civil Engineer", "Graphic Designer",
        "Doctor", "Teacher", "Content Writer", "Business Analyst"
    ]
    skills = [
        "Python", "JavaScript", "SQL", "Marketing", "Design",
        "Communication", "Management", "Research", "Teaching", "Writing"
    ]

    data = {
        "Name": [f"User{i}" for i in range(1, 101)],
        "Skill": [random.choice(skills) for _ in range(100)],
        "Recommended_Career": [random.choice(careers) for _ in range(100)]
    }
    
    df = pd.DataFrame(data)
    df.to_csv("data/career_datacopy.csv", index=False)
    print("Synthetic dataset generated and saved to career_data.csv.")

if __name__ == "__main__":
    generate_synthetic_data()
