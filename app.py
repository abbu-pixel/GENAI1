from flask import Flask, render_template, request, jsonify
from llm_engine import GenAILLM

app = Flask(__name__)
llm = GenAILLM()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    reply = llm.generate_response(user_input)  # Use correct method name
    return jsonify({"reply": reply})
