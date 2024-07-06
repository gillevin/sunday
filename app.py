import logging
import sys
from flask import Flask, jsonify

# Set up logging to stdout
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def hello():
        logging.info("GET / endpoint called")
        return jsonify({"message": "Hello, World!"})

    @app.route('/hello', methods=['POST'])
    def hello_post():
        logging.info("POST /hello endpoint called")
        return jsonify({"message": "Hello, World from POST!"})

    return app


app = create_app()

if __name__ == "__main__":
    logging.info("Starting Flask app")
    app.run(host="0.0.0.0", port=8000)
else:
    logging.info("Flask app imported, not running directly")

# Add this line at the end of the file
logging.info("app.py module loaded")