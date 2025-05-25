async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const userMsg = input.value;
  chatBox.innerHTML += `<div><strong>You:</strong> ${userMsg}</div>`;
  input.value = "";

  const res = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt: userMsg }),
  });

  const data = await res.json();
  chatBox.innerHTML += `<div><strong>Ms Tipsy:</strong> ${data.response}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
