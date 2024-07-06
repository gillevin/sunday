import logging
from flask import Flask, jsonify

# Set up logging
logging.basicConfig(level=logging.INFO)

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def hello():
        return jsonify({"message": "Hello, World!"})

    @app.route('/hello', methods=['POST'])
    def hello_post():
        return jsonify({"message": "Hello, World from POST!"})

    return app

app = create_app()

if __name__ == "__main__":
    logging.info("Starting Flask app")
    app.run(host="0.0.0.0", port=8000)