from logging import Logger
from slack_bolt import Complete
from slack_sdk import WebClient
from datetime import datetime
import time


def setup_function(client:WebClient, complete: Complete, logger: Logger):
    try:
        logger.error(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(time.time() + 3)))
        response = client.api_call("workflows.triggers.create", json={
            "name": "trigger rotate function",
            "type": "scheduled",
            "workflow": "#/workflows/rotate_workflow",
            "inputs": {
                "interactivity": {
                    "value": "{{data.interactivity}}"
                },
            },
            "schedule": {
                "start_time": time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime(time.time() + 5)),
                "frequency": {
                    "type": "daily",
                    "repeats_every": 1440,
                }
            }
        })
        logger.info(response.status_code)
        logger.info(response.data)
        TRIGGER_ID = response.data["trigger"]["id"]
        logger.info(TRIGGER_ID)
        complete(outputs={"msg": f":wave: you set up a rotation"})
    except Exception as e:
        logger.error(e)
        complete(error="Cannot submit the message")
        raise e
