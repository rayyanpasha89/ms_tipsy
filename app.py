from flask import Flask, request, jsonify, render_template
from rag_engine import load_faq_data, search_faq

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    answer = search_faq(user_input)
    return jsonify({"reply": answer})

if __name__ == "__main__":
    load_faq_data()
    app.run(debug=True)
