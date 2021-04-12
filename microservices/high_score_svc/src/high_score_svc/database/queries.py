import os

TABLE_NAME = os.getenv("TABLE_NAME")

IS_RANKED = "(wins + loses + ragequits) >= 10"

# fmt: off
SELECT_ONE_RANKED = f"""SELECT * FROM 
                            (SELECT *, ROW_NUMBER() OVER(ORDER BY winrate desc) 
                            FROM HighScores WHERE {IS_RANKED}) AS ranked 
                        WHERE ranked.username = %s"""
SELECT_ONE = f"SELECT * FROM HighScores WHERE username = %s"
SELECT_TOP_RANKED = f"""SELECT *, ROW_NUMBER() OVER(ORDER BY winrate desc)
                        FROM HighScores WHERE {IS_RANKED} LIMIT 10"""
INSERT = {
    "won": f"INSERT INTO {TABLE_NAME} (username, wins) VALUES (%s, 1)",
    "lost": f"INSERT INTO {TABLE_NAME} (username, loses) VALUES (%s, 1)",
    "ragequit": f"INSERT INTO {TABLE_NAME} (username, ragequits) VALUES (%s, 1)",
}
UPDATE = {
    "won": f"UPDATE {TABLE_NAME} SET wins = wins + 1 WHERE username = %s",
    "lost": f"UPDATE {TABLE_NAME} SET loses = loses + 1 WHERE username = %s",
    "ragequit": f"UPDATE {TABLE_NAME} SET ragequits = ragequits + 1 WHERE username = %s",
}
