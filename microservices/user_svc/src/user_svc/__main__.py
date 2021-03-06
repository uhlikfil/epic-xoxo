#!/usr/bin/env python3
import os

import connexion

from user_svc import encoder
from user_svc.eureka import eureka_client


def main():
    if os.getenv("SKIP_EUREKA") is None:
        eureka_client.register()
    app = connexion.App(os.getenv("APP_NAME"), specification_dir="./swagger/")
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api("swagger.yaml", arguments={"title": "Users"}, pythonic_params=True)
    app.run(port=os.getenv("APP_PORT"))


if __name__ == "__main__":
    main()
