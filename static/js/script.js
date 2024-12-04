// career_advisor/app/static/js/app.js

async function getCareerAdvice() {
    const userInput = document.getElementById("userInput").value.trim();
    const responseDiv = document.getElementById("response");

    if (!userInput) {
        responseDiv.innerHTML = "Please enter a skill.";
        responseDiv.style.color = "red";
        return;
    }

    responseDiv.innerHTML = "Thinking...";
    responseDiv.style.color = "#333";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ skill: userInput }),
        });

        if (!response.ok) {
            throw new Error("Failed to fetch career advice");
        }

        const data = await response.json();
        responseDiv.innerHTML = `Recommended Career: <strong>${data.career}</strong>`;
        responseDiv.style.color = "#007bff";
    } catch (error) {
        responseDiv.innerHTML = "Something went wrong. Please try again.";
        responseDiv.style.color = "red";
    }
}
