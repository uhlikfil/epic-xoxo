#!/usr/bin/env python3
import os

import connexion

from high_score_svc import encoder


def main():
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api("swagger.yaml", arguments={"title": "High Score"}, pythonic_params=True)
    app.run(port=os.getenv("APP_PORT"))


if __name__ == "__main__":
    main()
