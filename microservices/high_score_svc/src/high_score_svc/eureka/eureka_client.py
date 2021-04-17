import os

import py_eureka_client.eureka_client as eureka_client

EUREKA_SERVER = f'{os.getenv("EUREKA_HOST")}:{os.getenv("EUREKA_PORT")}'


def register():
    eureka_client.init(
        eureka_server=EUREKA_SERVER,
        app_name=os.getenv("APP_NAME"),
        instance_host=os.getenv("APP_HOST_OUT"),
        instance_port=int(os.getenv("APP_PORT_OUT")),
    )
