from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load Mistral model once at startup
model_name = "mistralai/Mistral-7B-Instruct-v0.2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16,
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # Simple prompt formatting
    prompt = f"[INST] {user_input} [/INST]"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=200, temperature=0.7)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract assistant response
    assistant_reply = reply.split("[/INST]")[-1].strip()

    return jsonify({"reply": assistant_reply})

if __name__ == "__main__":
    app.run(debug=True)
