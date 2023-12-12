"""
title: scoreboard functions and relevant code
author: joanna hao
date-created: 2023-12-12
"""
import pathlib
import sqlite3


# ---------- SCOREBOARD FUNCTIONS ---------- #
def setupScoreboard():
    global CURSOR, CONNECTION
    CURSOR.execute("""
        CREATE TABLE
            scoreboard (
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
    ;""")
    CONNECTION.commit()


def addScore(SCORE):
    """
    add score to leaderboard
    :param SCORE: tuple (int, str)
    :return: None
    """
    global CURSOR, CONNECTION
    CURSOR.execute("""
        INSERT INTO
            scoreboard (
                score,
                player_name
            )
        VALUES (
            ?, ?
        )
    ;""", SCORE)
    CONNECTION.commit()


def getTopScores():
    """
    retrieve top 3 scores
    :return: tuple (int)
    """
    global CURSOR, CONNECTION
    TOP_SCORES = CURSOR.execute("""
        SELECT
            score
        FROM
            scoreboard
        ORDER BY
            score DESC
    ;""").fetchall()
    if len(TOP_SCORES) > 3:
        return TOP_SCORES[:3]
    else:
        return TOP_SCORES


def getScoreboard():
    """
    retrieve scoreboard for user to see
    :return: list (str)
    """
    global CURSOR, CONNECTION
    SCORE_DATA = CURSOR.execute("""
        SELECT
            score, player_name
        FROM
            scoreboard
        ORDER BY
            score DESC
    ;""").fetchall()  # returns 2D array in form [(score, name), ...]
    return SCORE_DATA


def displayScoreboard(SCOREBOARD):
    """
    show top 1-3 scores to user
    :param SCOREBOARD: list of tuples
    :return: None
    """
    if len(SCOREBOARD) > 0:
        # print(SCOREBOARD)
        for i in range(min(3, len(SCOREBOARD))):
            print(f"{i+1}. {SCOREBOARD[i][1]} - {SCOREBOARD[i][0]} gold")
    else:
        print("There are no 'Ship, Captain, Crew!' winning scores yet!")


# ----- SETUP ----- #
DATABASE_FILE = "scoreboard.db"
FIRST_RUN = True
if (pathlib.Path.cwd() / DATABASE_FILE).exists():
    FIRST_RUN = False
CONNECTION = sqlite3.connect(DATABASE_FILE)
CURSOR = CONNECTION.cursor()
