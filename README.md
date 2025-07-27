# 🎓 EduBot

**EduBot** is a simple yet powerful educational chatbot designed to provide users with career guidance and helpful academic information via a conversational interface.

![EduBot Interface Demo](static/demo-screenshot.png)
*Above: Example screenshot of the EduBot web interface*

---

## ✨ Features

- 💬 **Conversational Chatbot** — Offers real-time, text-based guidance on education and careers.
- 📚 **Career Data Integration** — Answers career-related queries using a structured dataset (`career_data.json`).
- 🌐 **Web-based Interface** — Fully responsive front end accessible via any modern web browser.
- 🧩 **Easily Extensible** — Simple to update or expand with new educational or career data.

---



---

## 🛠️ Requirements

- **Python:** 3.x
- **Flask:** Lightweight web framework
- **OS:** Windows, macOS, or Linux
- **Browser:** Any modern browser (Chrome, Firefox, Edge, etc.)

---

## 🚀 Getting Started

To run EduBot locally:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Shristk/EduBot.git
    cd EduBot
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate         # On Windows: env\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python app.py
    ```

5. **Access it in your browser:**
    ```
    http://localhost:5000
    ```

---

## 🖼️ Screenshots

| Home Page                    | Chat in Action                  |
|------------------------------|---------------------------------|
| ![Home](static/home.png)     | ![Chat](static/chat.png)        |

---

## ⚙️ How It Works

EduBot is powered by Flask on the backend. When a user submits a message, the bot interprets their intent and searches `career_data.json` for relevant information. It then constructs and sends an appropriate response, simulating a helpful conversation.

---

## 🗺️ Project Roadmap

- [ ] Enable multi-turn conversation flow
- [ ] Deploy to cloud (Heroku, Render, etc.) for public access
- [ ] Expand dataset with rich, real-world guidance
- [ ] Add external API integrations (e.g., job market trends, course recommendations)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork this repo
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-xyz`)
5. Open a pull request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute.

---

> Made with ❤️ to support learners on their educational journey.
