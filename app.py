from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML file

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Simple echo response for now
    response = {
        'reply': f"You said: {user_input}"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
