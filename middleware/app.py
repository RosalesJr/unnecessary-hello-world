from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/hello')
def hello():
    # This is the bridge to the backend API
    backend_response = requests.get('http://backend:8080/hello')
    return jsonify(message=backend_response.text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
