from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from transformers import pipeline
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set your Hugging Face token
HUGGINGFACE_TOKEN = "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"  # Replace with your actual token

# Load the Mistral 7B model
generator = pipeline('text-generation', model='mistral-7b', 
                     tokenizer='mistral-7b', 
                     config={'use_auth_token': HUGGINGFACE_TOKEN})

@app.route('/')
def home():
    return "Welcome to the Mistral Chatbot Assistant!"

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('input')
    if user_input:
        response = generator(user_input, max_length=100, num_return_sequences=1)
        return jsonify(response[0]['generated_text'])
    else:
        return jsonify({"error": "No input provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Ensure the port matches Render's configuration
