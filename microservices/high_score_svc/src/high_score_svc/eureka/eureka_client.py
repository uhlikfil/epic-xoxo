import os

import py_eureka_client.eureka_client as eureka_client
from high_score_svc.logger import PrintLogger

LOGGER = PrintLogger("EUREKA")
EUREKA_SERVER = f'http://{os.getenv("EUREKA_HOST")}:{os.getenv("EUREKA_PORT")}'


def register():
    LOGGER.log(f'Registering {os.getenv("APP_NAME")}')
    eureka_client.init(
        eureka_server=EUREKA_SERVER,
        app_name=os.getenv("APP_NAME"),
        instance_host=os.getenv("APP_HOST_OUT"),
        instance_port=int(os.getenv("APP_PORT_OUT")),
    )


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
