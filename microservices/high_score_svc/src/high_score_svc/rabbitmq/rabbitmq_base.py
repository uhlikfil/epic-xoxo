import threading

import pika
from high_score_svc.eureka.eureka_client import get_rabbitmq_host
from high_score_svc.logger import PrintLogger

LOGGER = PrintLogger("CONSUMER")
CHANNEL = "CHANNEL"

thread_local_vars = threading.local()


def get_channel():
    global thread_local_vars
    channel = getattr(thread_local_vars, CHANNEL, None)
    if channel is None or channel.is_closed:
        channel = pika.BlockingConnection(
            pika.ConnectionParameters(*get_rabbitmq_host())
        ).channel()
        setattr(thread_local_vars, CHANNEL, channel)
    return channel
