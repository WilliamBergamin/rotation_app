from logging import Logger
from slack_bolt import Complete
from slack_sdk import WebClient
import json


def read_function(body, client:WebClient, complete: Complete, logger: Logger):
    try:
        response = client.api_call("workflows.triggers.list", json={
            "app_id":body["api_app_id"]
        })
        logger.info(response.status_code)
        trigger_ids = [trigger["id"] for trigger in response.data["triggers"] if trigger["name"] == "trigger rotate function"]
        logger.info(trigger_ids)
        complete(outputs={"trigger_ids": trigger_ids, "interactivity": complete.function_execution_id})
    except Exception as e:
        logger.error(e)
        complete(error="Cannot submit the message")
        raise e
