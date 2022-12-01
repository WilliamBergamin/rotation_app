from logging import Logger
from slack_bolt import Complete
from slack_sdk import WebClient


def rotate_function(complete: Complete, logger: Logger):
    try:
        complete(outputs={"msg": f":wave: hello there"})
    except Exception as e:
        logger.error(e)
        complete(error="Cannot submit the message")
        raise e
