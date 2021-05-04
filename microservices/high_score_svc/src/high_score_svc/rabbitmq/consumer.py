import threading
import time

import pika
from high_score_svc.eureka.eureka_client import get_rabbitmq_host


def process_queue_async():
    threading.Thread(target=process_queue).start()


def process_queue():
    while True:
        print(get_rabbitmq_host())
        time.sleep(10)
