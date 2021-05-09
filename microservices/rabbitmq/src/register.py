import os
import time

import py_eureka_client.eureka_client as eureka_client

EUREKA_SERVER = f'{os.getenv("EUREKA_HOST")}:{os.getenv("EUREKA_PORT")}'
HEARTBEAT_INTERVAL = 20  # seconds


def register():
    eureka_client.init(
        eureka_server=EUREKA_SERVER,
        app_name=os.getenv("APP_NAME"),
        instance_host=os.getenv("APP_HOST_OUT"),
        instance_port=int(os.getenv("APP_PORT_OUT")),
    )


def ping_app() -> int:
    return os.system(f'ping rabbitmq -c 1 -p {os.getenv("APP_PORT")}')


def keepalive():
    register()
    while ping_app() == 0:
        print("rabbit is alive and well")
        time.sleep(HEARTBEAT_INTERVAL)
    print("rabbit is dieded, i'm dying too")


if __name__ == "__main__":
    keepalive()
