"""
title: Game Engine for 'Ship, Captain, Crew!'
author: Joanna Hao
date-created: 2023-11-30
"""
import b_player
from a_dice import Dice


class Game:
    """
    Game class that has the rules of the game.
    """

    def __init__(self, PLAYER1:b_player.Player, PLAYER2:b_player.Player):
        self.__PLAYER1 = PLAYER1
        self.__PLAYER2 = PLAYER2

    def setup(self):
        ###
        # Database stuff
        ###
        print("Welcome to Ship, Captain, Crew!")

    def run(self):
        """
        where the majority of the game will happen. This section often loops
        :return:
        """
        # while True:  # for rerunning the game
        # --- Player 1 Turn --- #
        print(f"{self.__PLAYER1}'s turn!")
        ROLL = 0  # rolls that have happened
        while ROLL < 3:
            self.__PLAYER1.rollDice()  # roll all dice in player hand
            ROLLED_DICE = self.__PLAYER1.getDice()
            self.__PLAYER1.updateFound(ROLLED_DICE)
            self.__PLAYER1.displayDice()
            if self.__PLAYER1.getCaptainFound() and self.__PLAYER1.getShipFound() and self.__PLAYER1.getCrewFound():
                # if all required found (ideal case), total up points
                POINTS = 0
                self.__PLAYER1.addScore(POINTS)

            ROLL += 1


