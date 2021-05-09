import os

import high_score_svc.database.db_access as db
import high_score_svc.validators as valid
from high_score_svc.rabbitmq.rabbitmq_base import LOGGER, get_channel

HIGH_SCORE_DELETES_QUEUE = os.getenv("HIGH_SCORE_DELETES_QUEUE")


def consume_callback(channel, method, properties, username):
    LOGGER.log(f"High score deletes consumer received message: {username}")
    if not valid.is_valid_username(username):
        LOGGER.log("Incorrent message in queue!")
        return
    db.delete_high_score(username)
    LOGGER.log("Consume successful")


def consume_high_score_deletes():
    LOGGER.log("Starting up High score deletes consumer")
    get_channel().queue_declare(HIGH_SCORE_DELETES_QUEUE, durable=True)
    get_channel().basic_consume(
        HIGH_SCORE_DELETES_QUEUE, consume_callback, auto_ack=True
    )
    get_channel().start_consuming()
