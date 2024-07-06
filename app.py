import logging
import sys
from flask import Flask, jsonify
from app import create_app

# Set up logging to both file and stdout
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/tmp/log/application.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


def create():
    app = create_app()

    @app.route('/', methods=['GET'])
    def hello():
        logging.info("GET / endpoint called")
        return jsonify({"message": "Hello, World!"})

    @app.route('/hello', methods=['POST'])
    def hello_post():
        logging.info("POST /hello endpoint called")
        return jsonify({"message": "Hello, World from POST!"})

    return app


app = create()

if __name__ == "__main__":
    logging.info("Starting Flask app")
    app.run(host="0.0.0.0", port=8000)

logging.info("app.py module loaded")