"""
title: Main game file for Ship, Captain, Crew!
author: joanna hao
date-created: 2023-11-30
"""
from b_player import Player
from c_game import Game


class Main:
    # --- input --- #
    PLAYER1_NAME = input("Player 1 Name: ")
    PLAYER2_NAME = input("Player 2 Name: ")

    # --- processing --- #
    PLAYER_1 = Player(PLAYER1_NAME)
    PLAYER_2 = Player(PLAYER2_NAME)
    GAME = Game(PLAYER_1, PLAYER_2)
    GAME.setup()
    GAME.run()

    # --- output --- #


if __name__ == "__main__":
    Main()
