"""
title: player class
author: joanna hao
date-created: 2023-11-28
"""
from a_dice import Dice


class Player:
    """
    the player for the game 'Ship, Captain, Crew!'
    """
    def __init__(self, NAME):
        self.__NAME = NAME
        self.__DICE = [Dice(6), Dice(6), Dice(6), Dice(6), Dice(6)]
        self.__SCORE = 0
        self.__CAPTAIN_FOUND = False
        self.__SHIP_FOUND = False
        self.__CREW_FOUND = False
        self.__ALL_FOUND = False

    # --- Modifier Methods
    def addScore(self, POINTS):
        """
        update score of player
        :param POINTS: int
        :return: None
        """
        self.__SCORE += POINTS

    def rollDice(self):
        """
        rolls all dice in DICE
        :return: None
        """
        for die in self.__DICE:
            die.rolLDie()

    def updateCaptainFound(self, DIE):
        """
        update whether captain found
        :param DIE: list of Dice()
        :return:
        """
        if not self.__CAPTAIN_FOUND and 6 in DIE:
            self.__CAPTAIN_FOUND = True
            print("> Captain is found!")

    def updateShipFound(self, DIE):
        if self.__CAPTAIN_FOUND and not self.__SHIP_FOUND and 5 in DIE:
            self.__SHIP_FOUND = True
            print("> Ship is found!")

    def updateCrewFound(self, DIE):
        if self.__CAPTAIN_FOUND and self.__SHIP_FOUND and not self.__CREW_FOUND and 4 in DIE:
            self.__CREW_FOUND = True
            print("> Crew is found!")

    def updateAllFound(self):
        if self.__CAPTAIN_FOUND and self.__SHIP_FOUND and self.__CREW_FOUND:
            self.__ALL_FOUND = True

    # --- Accessor Methods
    def __str__(self):
        return f"{self.__NAME}"

    def __repr__(self):
        return f"{self.__str__()}"

    def getName(self):
        return self.__NAME

    def getDice(self):
        return self.__DICE

    def getScore(self):
        return self.__SCORE

    def getCaptainFound(self):
        return self.__CAPTAIN_FOUND

    def getShipFound(self):
        return self.__SHIP_FOUND

    def getCrewFound(self):
        return self.__CREW_FOUND

    def getAllFound(self):
        return self.__ALL_FOUND
