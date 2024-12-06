document.getElementById("send-btn").addEventListener("click", sendMessage);

function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    if (!userInput.trim()) {
        return;
    }

    const userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    document.getElementById("user-input").value = "";

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement("div");
        botMessage.className = "message bot";
        botMessage.textContent = data.response;
        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(() => {
        const botMessage = document.createElement("div");
        botMessage.className = "message bot";
        botMessage.textContent = "Oops! Something went wrong. Please try again.";
        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;
    });
}
