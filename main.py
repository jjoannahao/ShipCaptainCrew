"""
title: Main game file for Ship, Captain, Crew!
author: joanna hao
date-created: 2023-11-30
"""
import pathlib
import sqlite3
from b_player import Player
from c_game import Game


def menu():
    """
    display menu of user interaction options
    :return: int
    """
    print("""
1. See game instructions
2. Start a new game
3. See leaderboard
4. Exit""")
    USER_CHOICE = input("> ")
    if USER_CHOICE.isdigit() and 1 <= int(USER_CHOICE) <= 4:
        return int(USER_CHOICE)
    else:
        print("Please enter a valid number between 1 and 4!")
        return menu()


def instructions():
    """
    print game instructions for user
    :return: None
    """
    print("""
Find your ship, captain, and crew to collect as much gold as you can!

Each player gets 3 dice rolls per turn. 
First, players must roll a 6, 5, and 4 in that order in any number of rolls. This signifies that they have found their ship, captain, and crew.

Afterwards, the remaining numbers on the player's dice add up to gold the player can collect, if they choose to hold their dice (and collect the gold). 
If players have rolls left, they can re-roll their dice to get potentially a new amount of gold they can collect.""")
    # break up text chunks so that user presses any key to continue


def getScoreboard():
    """
    retrieve scoreboard for user to see
    :return: list (str)
    """
    pass


class Main:
    # --- input --- #
    PLAYER1_NAME = input("Player 1 Name: ")
    PLAYER2_NAME = input("Player 2 Name: ")

    # --- processing --- #
    PLAYER_1 = Player(PLAYER1_NAME)
    PLAYER_2 = Player(PLAYER2_NAME)
    GAME = Game(PLAYER_1, PLAYER_2)

    # --- output --- #
    GAME.run()


if __name__ == "__main__":
    # ----- SETUP ----- #
    DATABASE_FILE = "scoreboard.db"
    FIRST_RUN = True
    if (pathlib.Path.cwd() / DATABASE_FILE).exists():
        FIRST_RUN = False
    CONNECTION = sqlite3.connect(DATABASE_FILE)
    CURSOR = CONNECTION.cursor()

    # --- RUNNING PROGRAM --- #
    while True:
        print("Welcome to Ship, Captain, Crew!")
        # --- INPUTS --- #
        USER_CHOICE = menu()

        # --- PROCESSING --- #
        if USER_CHOICE == 1:  # see game instructions
            instructions()
        elif USER_CHOICE == 2:  # run game
            Main()
        elif USER_CHOICE == 3:  # see leaderboard
            getScoreboard()  # currently 'pass' as function
        else:
            break
