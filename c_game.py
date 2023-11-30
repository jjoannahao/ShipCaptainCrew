"""
title: Game Engine for 'Ship, Captain, Crew!'
author: Joanna Hao
date-created: 2023-11-30
"""
# from a_dice import Dice
from b_player import Player


class Game:
    """
    Game class that has the rules of the game.
    """

    def __init__(self, PLAYER1, PLAYER2):
        self.__PLAYER1 = PLAYER1
        self.__PLAYER2 = PLAYER2

    def setup(self):
        print("Welcome to Ship, Captain, Crew!")

    def run(self):
        """
        where the majority of the game will happen. This section often loops
        :return:
        """
        while True:
            # --- Player 1 Turn --- #
            print(f"{self.__PLAYER1}'s turn!")
            ROLL = 0  # rolls that have happened
            while ROLL > 0:
                self.__PLAYER1.rollDice()  # roll all dice in player hand
                ROLLED_DICE = self.__PLAYER1.getDice()
                self.__PLAYER1.updateFound(ROLLED_DICE)
                if self.__PLAYER1.__CAPTAIN_FOUND and self.__PLAYER1.__SHIP_FOUND and self.__PLAYER1.__CREW_FOUND:
                    pass

