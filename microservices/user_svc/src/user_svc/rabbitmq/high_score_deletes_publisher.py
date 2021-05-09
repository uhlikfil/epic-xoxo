import os

from user_svc.rabbitmq.rabbitmq_base import LOGGER, get_channel

HIGH_SCORE_DELETES_QUEUE = os.getenv("HIGH_SCORE_DELETES_QUEUE")


def publish_high_score_delete(username: str):
    LOGGER.log("Publishing High score delete to queue")
    get_channel().queue_declare(HIGH_SCORE_DELETES_QUEUE, durable=True)
    get_channel().basic_publish(
        exchange="", routing_key=HIGH_SCORE_DELETES_QUEUE, body=username
    )
    LOGGER.log("Publish successful")
