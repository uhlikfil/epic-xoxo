CREATE TABLE IF NOT EXISTS Users (
    username VARCHAR(64) NOT NULL,
    origin_ip VARCHAR(64) NOT NULL,
    last_ip VARCHAR(64) NOT NULL,
    created TIMESTAMP DEfAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (username)
) ENGINE=InnoDB
