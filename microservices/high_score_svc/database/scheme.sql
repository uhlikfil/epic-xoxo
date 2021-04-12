CREATE TABLE IF NOT EXISTS HighScores (
    username VARCHAR(64) NOT NULL,
    wins INTEGER NOT NULL DEFAULT 0,
    loses INTEGER NOT NULL DEFAULT 0,
    ragequits INTEGER NOT NULL DEFAULT 0,
    winrate FLOAT AS (wins / (wins + loses + ragequits)),
    PRIMARY KEY (username)
) ENGINE=InnoDB
