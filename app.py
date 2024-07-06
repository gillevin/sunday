import logging
from datetime import datetime
from flask import jsonify, request

from apscheduler.schedulers.background import BackgroundScheduler

from app import create_app
from app.services.openai_service import get_llm_message_to_push
from app.utils.whatsapp_utils import send_message
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# TEMP TEST
def morning_task(name, number):
    """Task to be run every morning at a scheduled time."""
    current_time = datetime.now()
    logging.info(f"Morning task running at: {current_time}")

    prompt = (
        f"Today is {current_time}. "
        "Wish Sarah a good day and remind her of the upcoming tasks."
    )
    # llm_msg = get_llm_message_to_push(prompt, number, name)
    llm_msg = "test"
    send_message(llm_msg)


def main():
    app = create_app()

    # Add the new POST endpoint
    @app.route('/hello', methods=['POST'])
    def hello_world():
        return jsonify({"message": "Hello, World!"})

    scheduler = BackgroundScheduler()
    # scheduler.add_job(morning_task(app.config["TEST_NAME"], app.config["TEST_NUMBER"]), 'cron', hour=10, minute=0)
    scheduler.start()
    send_message("app started")
    # morning_task(app.config["TEST_NAME"], app.config["TEST_NUMBER"])
    logging.info("Scheduler started and Flask app initialized")
    try:
        app.run(host="0.0.0.0", port=8000)
        logging.info("App started!")
    except Exception as e:
        scheduler.shutdown()
        logging.error(f"An error occurred: {str(e)}")
        raise


if __name__ == "__main__":
    main()
