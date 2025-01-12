import logging
from flask import request, jsonify
from app.utils.whatsapp_utils import send_message
from app import create_app

def create():
    app = create_app()

    @app.route('/', methods=['GET'])
    def hello_get():
        logging.debug("GET / endpoint called")
        return jsonify({"message": f"Hello, World from GET!"})

    @app.route('/hello', methods=['POST'])
    def hello_post():
        logging.debug("POST /hello endpoint called")

        payload = request.json
        wapp_output = send_message(f"Hi! {payload.get('message', '')}")
        return jsonify({"wapp_output": wapp_output.text})

    return app


app = create()

if __name__ == "__main__":
    logging.info("Starting Flask app")
    app.run(host="0.0.0.0", port=8000)

logging.info("app.py module loaded")