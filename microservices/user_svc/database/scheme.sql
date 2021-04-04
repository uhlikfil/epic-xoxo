CREATE TABLE IF NOT EXISTS Users (
    username varchar(64) NOT NULL,
    email varchar(64) NOT NULL,
    password_hash varchar(64) NOT NULL,
    PRIMARY KEY (username)
) ENGINE=InnoDB