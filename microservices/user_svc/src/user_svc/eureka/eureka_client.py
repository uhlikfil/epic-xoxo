import json
import os
from urllib.error import URLError

import py_eureka_client.eureka_client as eureka_client
from user_svc.models.high_score import HighScore

EUREKA_SERVER = f'{os.getenv("EUREKA_SERVER")}:{os.getenv("EUREKA_PORT")}'

UNAVAILABLE = "Unavailable"
UNAVAILABLE_HS = HighScore(
    UNAVAILABLE, UNAVAILABLE, UNAVAILABLE, UNAVAILABLE, UNAVAILABLE
)


def register():
    eureka_client.init(
        eureka_server=EUREKA_SERVER,
        app_name=os.getenv("APP_NAME"),
        instance_host=os.getenv("APP_HOST_OUT"),
        instance_port=int(os.getenv("APP_PORT_OUT")),
    )


def get_high_score(username: str):
    try:
        high_score = eureka_client.do_service(
            "HIGH_SCORE_SVC", f"api/v1/high_score/{username}"
        )
        return HighScore.from_dict(json.loads(high_score))
    except URLError:
        return UNAVAILABLE_HS
