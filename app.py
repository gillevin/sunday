import logging
import sys
import os
from flask import jsonify
from app import create_app
from app.utils.whatsapp_utils import send_message
from dotenv import load_dotenv

# Set up logging to both file and stdout
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.getenv("LOG_FILE")),
        logging.StreamHandler(sys.stdout)
    ]
)


def create():
    app = create_app()
    load_dotenv()
    RECIPIENT_WAID = os.getenv("RECIPIENT_WAID")

    @app.route('/', methods=['GET'])
    def hello():
        logging.info("GET / endpoint called")
        wapp_output = send_message("test")
        return jsonify({"wapp_output": wapp_output.text})

    @app.route('/hello', methods=['POST'])
    def hello_post():
        logging.info("POST /hello endpoint called")
        return jsonify({"message": f"Hello, World from POST! {RECIPIENT_WAID}"})

    return app


app = create()

if __name__ == "__main__":
    logging.info("Starting Flask app")
    app.run(host="0.0.0.0", port=8000)

logging.info("app.py module loaded")