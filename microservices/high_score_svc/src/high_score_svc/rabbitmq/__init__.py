import threading

from high_score_svc.rabbitmq.finished_games_consumer import consume_finished_games
from high_score_svc.rabbitmq.high_score_deletes_consumer import (
    consume_high_score_deletes,
)


def run_all_consumers_async():
    threading.Thread(target=consume_finished_games).start()
    threading.Thread(target=consume_high_score_deletes).start()
