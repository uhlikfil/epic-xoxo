CREATE DATABASE dta_db;

\c dta_db;

CREATE TABLE IF NOT EXISTS replays (
    id SERIAL primary key,
    player1Id VARCHAR(64),
    player2Id VARCHAR(64),
    winnerId VARCHAR(64),
    startingId VARCHAR(64),
    rounds INTEGER,
    date TIMESTAMP,
    completed BOOLEAN,
    plays TEXT
)
