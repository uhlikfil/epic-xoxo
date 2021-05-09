import json
import os
from urllib.error import URLError

import py_eureka_client.eureka_client as eureka_client
from user_svc.logger import PrintLogger
from user_svc.models.high_score import HighScore

LOGGER = PrintLogger("EUREKA")

EUREKA_SERVER = f'{os.getenv("EUREKA_HOST")}:{os.getenv("EUREKA_PORT")}'

UNAVAILABLE = "Unavailable"
UNAVAILABLE_HS = HighScore(
    UNAVAILABLE, UNAVAILABLE, UNAVAILABLE, UNAVAILABLE, UNAVAILABLE
)


def register():
    LOGGER.log(f'Registering {os.getenv("APP_NAME")}')
    eureka_client.init(
        eureka_server=EUREKA_SERVER,
        app_name=os.getenv("APP_NAME"),
        instance_host=os.getenv("APP_HOST_OUT"),
        instance_port=int(os.getenv("APP_PORT_OUT")),
    )


def get_high_score(username: str):
    LOGGER.log(f"Getting high score of {username}")
    try:
        high_score = eureka_client.do_service(
            "HIGH_SCORE_SVC", f"api/v1/high_score/{username}", method="GET"
        )
        LOGGER.log("High score found")
        return HighScore.from_dict(json.loads(high_score))
    except URLError:
        LOGGER.log("High score unavailable")
        return UNAVAILABLE_HS


def get_rabbitmq_host() -> tuple:
    try:
        rabbitmq_instance = (
            eureka_client.get_client()
            .applications.get_application("RABBITMQ")
            .up_instances[0]
        )
        host = (rabbitmq_instance.ipAddr, rabbitmq_instance.port.port)
        LOGGER.log(f"Found RabbitMQ instance at {host}")
        return host
    except IndexError:
        return None
