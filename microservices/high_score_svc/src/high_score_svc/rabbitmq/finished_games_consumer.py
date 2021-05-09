import json
import os

import high_score_svc.database.db_access as db
from high_score_svc.models.finished_game import FinishedGame
from high_score_svc.rabbitmq.rabbitmq_base import LOGGER, get_channel

FINISHED_GAMES_QUEUE = os.getenv("FINISHED_GAMES_QUEUE")


def update_high_score(username, result):
    if db.get_high_score(username, False):
        db.update_high_score(username, result)
    else:
        db.create_high_score(username, result)


def consume_callback(channel, method, properties, body):
    LOGGER.log(f"Finished games consumer received message: {body}")
    try:
        game = FinishedGame.from_dict(json.loads(body))
        if any(getattr(game, attr) is None for attr in game.attribute_map.keys()):
            raise AttributeError
    except (json.decoder.JSONDecodeError, AttributeError):
        LOGGER.log(f"Incorrect message in queue!")
        return
    winner = game.player1 if game.p1winner else game.player2
    loser = game.player2 if game.p1winner else game.player1
    update_high_score(winner, db.GameResult.WIN)
    update_high_score(
        loser, db.GameResult.LOSE if game.completed else db.GameResult.RAGEQUIT
    )
    LOGGER.log("Consume successful")


def consume_finished_games():
    LOGGER.log("Starting up Finished games consumer")
    get_channel().queue_declare(FINISHED_GAMES_QUEUE, durable=True)
    get_channel().basic_consume(FINISHED_GAMES_QUEUE, consume_callback, auto_ack=True)
    get_channel().start_consuming()
