"""
title: Game Engine for 'Ship, Captain, Crew!'
author: Joanna Hao
date-created: 2023-11-30
"""

import b_player
from scoreboard import *


def holdGold(POINTS_SCORED):
    """
    determine if user wants to hold gold rolled
    :param POINTS_SCORED: int
    :return: bool
    """
    CHOICE = input(f"   LOOT: {POINTS_SCORED} gold! Keep coins? (Y/n) ")
    if CHOICE.lower() in {"n", "no"}:
        return False
    else:
        return True


def pause():
    """
    let user press any key when ready to continue to next player
    :return: str
    """
    USER_INPUT = input("> Press any key to continue to the next player: ")
    return True


class Game:
    """
    Game class that has the running of th game
    """

    def __init__(self, PLAYER1:b_player.Player, PLAYER2:b_player.Player):
        self.__PLAYER1 = PLAYER1
        self.__PLAYER2 = PLAYER2

    def run(self):
        """
        where the majority of the game will happen
        :return:
        """
        # ----- Player 1 Turn ----- #
        print(f"{self.__PLAYER1}'s turn!")
        ROLL = 0  # rolls that have happened
        while ROLL < 3:
            self.__PLAYER1.rollDice()  # roll all dice in player hand

            ROLLED_DICE_OBJ = self.__PLAYER1.getDice()
            ROLLED_DICE = []
            for i in range(len(ROLLED_DICE_OBJ)):  # convert list items from obj to int
                ROLLED_DICE.append(ROLLED_DICE_OBJ[i].getDieNumber())
            DICE_FOUND = []  # special dice found in this roll
            # ROLLED_DICE = [6, 5, 4, 1, 1]  ### TESTING

            print(f"ROLL {ROLL+1}: {ROLLED_DICE}")

            # --- check if ship, captain, crew found
            if not self.__PLAYER1.getAllFound():  # check if ship, captain, crew found
                # self.__PLAYER1.updateFound(ROLLED_DICE)
                self.__PLAYER1.updateCaptainFound(ROLLED_DICE)
                if self.__PLAYER1.getCaptainFound():
                    DICE_FOUND.append(6)
                self.__PLAYER1.updateShipFound(ROLLED_DICE)
                if self.__PLAYER1.getShipFound():
                    DICE_FOUND.append(5)
                self.__PLAYER1.updateCrewFound(ROLLED_DICE)
                if self.__PLAYER1.getCrewFound():
                    DICE_FOUND.append(4)
            self.__PLAYER1.updateAllFound()

            # --- calculate & add points if player can
            if self.__PLAYER1.getAllFound():
                POINTS = 0
                # remove special dice found in current roll
                for i in range(len(DICE_FOUND)):
                    if DICE_FOUND[i] in ROLLED_DICE:
                        ROLLED_DICE.remove(DICE_FOUND[i])  # only removes 1 occurrence
                # total up points
                for i in range(len(ROLLED_DICE)):
                    POINTS += ROLLED_DICE[i]

                # input: ask user if they want to hold gold
                HOLD_GOLD = holdGold(POINTS)

                # processing: see if player wants to keep coins
                if HOLD_GOLD:
                    self.__PLAYER1.addScore(POINTS)
                    print(f"{self.__PLAYER1}'s ends turn with {self.__PLAYER1.getScore()} gold!\n")
                    break
            ROLL += 1

        # ----- pause ----- #
        PROCEED = pause()

        # ----- Player 2 Turn ----- #
        print(f"\n{self.__PLAYER2}'s turn!")
        ROLL = 0  # rolls that have happened
        while ROLL < 3:
            self.__PLAYER2.rollDice()  # roll all dice in player hand

            ROLLED_DICE_OBJ = self.__PLAYER2.getDice()
            ROLLED_DICE = []
            for i in range(len(ROLLED_DICE_OBJ)):  # convert list items from obj to int
                ROLLED_DICE.append(ROLLED_DICE_OBJ[i].getDieNumber())
            DICE_FOUND = []  # special dice found in this roll

            print(f"ROLL {ROLL + 1}: {ROLLED_DICE}")

            # --- check if ship, captain, crew found
            if not self.__PLAYER2.getAllFound():  # check if ship, captain, crew found
                self.__PLAYER2.updateCaptainFound(ROLLED_DICE)
                if self.__PLAYER2.getCaptainFound():
                    DICE_FOUND.append(6)
                self.__PLAYER2.updateShipFound(ROLLED_DICE)
                if self.__PLAYER2.getShipFound():
                    DICE_FOUND.append(5)
                self.__PLAYER2.updateCrewFound(ROLLED_DICE)
                if self.__PLAYER2.getCrewFound():
                    DICE_FOUND.append(4)
            self.__PLAYER2.updateAllFound()

            # --- calculate & add points if player can
            if self.__PLAYER2.getAllFound():
                POINTS = 0
                # remove special dice found in current roll
                for i in range(len(DICE_FOUND)):
                    if DICE_FOUND[i] in ROLLED_DICE:
                        ROLLED_DICE.remove(DICE_FOUND[i])  # only removes 1 occurrence
                # total up points
                for i in range(len(ROLLED_DICE)):
                    POINTS += ROLLED_DICE[i]

                # input: ask user if they want to hold gold
                HOLD_GOLD = holdGold(POINTS)

                # processing: see if player wants to keep coins
                if HOLD_GOLD:
                    self.__PLAYER2.addScore(POINTS)
                    print(f"{self.__PLAYER2}'s ends turn with {self.__PLAYER2.getScore()} gold!\n")
                    break
            ROLL += 1

        # --- check which player won & whether new high score achieved --- #
        NEW_HIGH_SCORE = False
        TOP_SCORES = getTopScores()
        if self.__PLAYER1.getScore() > self.__PLAYER2.getScore():
            # check if new leaderboard score
            if len(TOP_SCORES) < 3 or self.__PLAYER1.getScore() > TOP_SCORES[-1][0]:
                NEW_HIGH_SCORE = True
                addScore([self.__PLAYER1.getScore(), self.__PLAYER1.getName()])

            # --- outputs
            print(f"\n{self.__PLAYER1.getName()} wins!")
            if NEW_HIGH_SCORE:
                print(f"New top score achieved! See the updated scoreboard!")
        elif self.__PLAYER2.getScore() > self.__PLAYER1.getScore():
            # check if new leaderboard score
            if len(TOP_SCORES) < 3 or self.__PLAYER2.getScore() > TOP_SCORES[-1][0]:
                NEW_HIGH_SCORE = True
                addScore([self.__PLAYER2.getScore(), self.__PLAYER2.getName()])

            # --- outputs
            print(f"\n{self.__PLAYER2.getName()} wins!")
            if NEW_HIGH_SCORE:
                print(f"New top score achieved! See the updated scoreboard!")
        else:
            print("Tie!")
