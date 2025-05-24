async function askTipsy() {
  const question = document.getElementById("question").value;

  const res = await fetch("/ask", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: question })
  });

  const data = await res.json();
  document.getElementById("response").innerText = data.reply;
}
