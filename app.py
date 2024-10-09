from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

if __name__ == '__main__':
    app.run()


@app.route('/ask', methods=['POST'])
def ask():
    query = request.json.get('query')
    # Add logic to process the query and generate a response
    return jsonify({"response": f"You asked: {query}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
