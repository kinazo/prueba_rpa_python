from flask import Flask, jsonify, request
import requests
import threading

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from the API!"})

def create_api():
    """Crea y ejecuta la API en un hilo separado."""
    thread = threading.Thread(target=lambda: app.run(port=5000, debug=False))
    thread.start()

def consume_api():
    """Consume la API creada."""
    response = requests.get("http://127.0.0.1:5000/api/data")
    print(f"Respuesta de la API: {response.json()}")

