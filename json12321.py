import json

# Define a function to create the JSON structure
def generate_career_support_intents():
    career_support_intents = {
        "intents": [
            {
                "tag": "career_advice",
                "patterns": [
                    "What career options are available after graduation?",
                    "Can you guide me on career choices?",
                    "What should I do after college?",
                    "Which field is best for me?",
                    "What are some good career paths?"
                ],
                "responses": [
                    "There are many career options depending on your interests and skills. For example, you can pursue higher studies, look for job opportunities in your field, or explore entrepreneurship.",
                    "Your career path depends on your passion and aptitude. Consider fields like IT, healthcare, finance, or creative arts based on your strengths.",
                    "Let me help you. Can you tell me your educational background and interests?"
                ],
                "context": ["general"],
                "examples": ["Example: 'What are some good career options after engineering?'", "Example: 'Can you guide me on a career in finance?'"],
                "metadata": {
                    "priority": 1,
                    "language": "English",
                    "categories": ["career_guidance", "decision_making"],
                    "intent_type": "information_provided"
                },
                "related_intents": ["skills_development", "higher_studies", "job_preparation"]
            },
            {
                "tag": "skills_development",
                "patterns": [
                    "What skills should I learn for a career in IT?",
                    "Which technical skills are in demand?",
                    "Can you suggest some soft skills to improve?",
                    "How can I develop leadership skills?",
                    "What are the top skills employers look for?"
                ],
                "responses": [
                    "Technical skills like coding, data analysis, and cloud computing are highly valued in IT. Soft skills such as communication, teamwork, and adaptability are equally important.",
                    "To develop leadership skills, consider taking on team projects, participating in workshops, or reading books on management and strategy.",
                    "The top skills employers value include problem-solving, emotional intelligence, and technical expertise in your field."
                ],
                "context": ["career_development"],
                "examples": ["Example: 'What skills do I need to succeed in a tech career?'", "Example: 'How can I improve my communication skills?'"],
                "metadata": {
                    "priority": 2,
                    "language": "English",
                    "categories": ["skills", "career_development"],
                    "intent_type": "advice"
                },
                "related_intents": ["career_advice", "job_preparation", "internship_advice"]
            },
            {
                "tag": "job_preparation",
                "patterns": [
                    "How do I prepare for job interviews?",
                    "Can you help with resume writing?",
                    "What are some common interview questions?",
                    "How do I get ready for a technical interview?",
                    "What should I include in a cover letter?"
                ],
                "responses": [
                    "For interviews, research the company, practice common questions, and be ready to showcase your skills and achievements.",
                    "A strong resume should highlight your accomplishments, relevant skills, and experiences. Keep it concise and tailored to the job.",
                    "For technical interviews, practice coding problems, algorithms, and system design. Platforms like LeetCode and HackerRank can help."
                ],
                "context": ["job_search"],
                "examples": ["Example: 'How do I create an impactful resume?'", "Example: 'What are the best tips for acing interviews?'"],
                "metadata": {
                    "priority": 3,
                    "language": "English",
                    "categories": ["job_search", "preparation"],
                    "intent_type": "advice"
                },
                "related_intents": ["skills_development", "internship_advice", "networking"]
            },
            {
                "tag": "internship_advice",
                "patterns": [
                    "How do I find internships?",
                    "What are some good platforms for internships?",
                    "Can you help me with an internship application?",
                    "What should I include in my internship portfolio?",
                    "How do internships help in building a career?"
                ],
                "responses": [
                    "Internships provide valuable experience and networking opportunities. Platforms like LinkedIn, Internshala, and Handshake are great for finding internships.",
                    "Tailor your applications to the role and highlight relevant projects or skills in your portfolio.",
                    "Internships can help you understand industry practices and boost your resume for future job applications."
                ],
                "context": ["career_exploration"],
                "examples": ["Example: 'Where can I find internships in data science?'", "Example: 'How can I get an internship at a tech company?'"],
                "metadata": {
                    "priority": 4,
                    "language": "English",
                    "categories": ["career_development", "entry_level"],
                    "intent_type": "information_provided"
                },
                "related_intents": ["job_preparation", "skills_development", "career_advice"]
            },
            {
                "tag": "industry_insights",
                "patterns": [
                    "What are the latest trends in technology?",
                    "Can you tell me about careers in AI?",
                    "What are some growing industries?",
                    "Which industries are hiring the most?",
                    "What are some high-paying jobs?"
                ],
                "responses": [
                    "AI, cloud computing, and cybersecurity are among the fastest-growing fields in technology.",
                    "Healthcare, green energy, and remote work solutions are booming industries with high demand for skilled professionals.",
                    "High-paying careers often require specialized skills, such as data science, software development, or management roles."
                ],
                "context": ["career_guidance"],
                "examples": ["Example: 'What are the top jobs in technology?'", "Example: 'Can you guide me on AI careers?'"],
                "metadata": {
                    "priority": 5,
                    "language": "English",
                    "categories": ["industry_insights", "future_trends"],
                    "intent_type": "advice"
                },
                "related_intents": ["career_advice", "higher_studies", "skills_development"]
            },
            {
                "tag": "higher_studies",
                "patterns": [
                    "Should I go for higher studies?",
                    "What are the benefits of a master's degree?",
                    "Which universities are best for computer science?",
                    "How do I prepare for GRE or GMAT?",
                    "Can you suggest courses after graduation?"
                ],
                "responses": [
                    "Higher studies can open up advanced career opportunities and increase your expertise. It depends on your goals and field of interest.",
                    "Top universities like MIT, Stanford, and IITs offer excellent computer science programs. Prepare early for entrance exams.",
                    "Consider courses like MBA, M.Tech, or certifications in emerging fields like data science, AI, or project management."
                ],
                "context": ["career_guidance"],
                "examples": ["Example: 'Is a master's degree worth it?'", "Example: 'What are the best courses after B.Tech?'"],
                "metadata": {
                    "priority": 6,
                    "language": "English",
                    "categories": ["education", "higher_studies"],
                    "intent_type": "information_provided"
                },
                "related_intents": ["career_advice", "skills_development", "industry_insights"]
            }
            # Add more intents here if needed
        ]
    }
    return career_support_intents

# Generate the career support intents
intents_data = generate_career_support_intents()

# Save to a JSON file
output_file = "career_support_intents.json"
with open(output_file, "w") as json_file:
    json.dump(intents_data, json_file, indent=4)

print(f"JSON file '{output_file}' has been created with career support intents.")
