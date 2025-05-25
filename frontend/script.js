const chatBox = document.getElementById("chat-box");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const question = userInput.value.trim();
  if (!question) return;

  // Show user message
  appendMessage("You", question, "user");
  userInput.value = "";
  userInput.disabled = true;

  // Show loading...
  appendMessage("Ms Tipsy", "<em>Typing...</em>", "bot", true);

  try {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt: question }),
    });
    const data = await res.json();

    // Remove loading and show bot message
    removeLoading();
    appendMessage("Ms Tipsy", data.response, "bot");
  } catch (err) {
    removeLoading();
    appendMessage("Ms Tipsy", "Sorry, there was a connection error.", "bot");
  }
  userInput.disabled = false;
  userInput.focus();
});

function appendMessage(sender, text, cls, loading=false) {
  const div = document.createElement("div");
  div.className = `message ${cls}` + (loading ? " loading" : "");
  div.innerHTML = `<strong>${sender}:</strong> ${text}`;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function removeLoading() {
  const loadingMsg = chatBox.querySelector(".loading");
  if (loadingMsg) loadingMsg.remove();
}