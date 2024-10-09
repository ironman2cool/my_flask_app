from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

app = Flask(__name__)
CORS(app)

# Set your Hugging Face token here
HUGGINGFACE_TOKEN = "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"  # Replace with your actual token

# Load the Mistral model and tokenizer from Hugging Face
model_name = "mistral/mistral-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=HUGGINGFACE_TOKEN)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=HUGGINGFACE_TOKEN)

@app.route('/')
def home():
    return "Welcome to my Flask chatbot!"

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')
    
    # Encode the input text and generate a response
    inputs = tokenizer.encode(user_input, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    
    # Decode the generated response and return it
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
