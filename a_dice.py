"""
title: dice class
author: joanna hao
date-created: 2023-11-28
"""
from random import randint


class Dice:
    """
    creates a die to roll for random numbers
    """
    def __init__(self, SIDES):
        """
        construct a die
        :param SIDES: int
        """
        self.__DIE_MAX = SIDES
        self.__DIE_NUMBER = 0

    # --- Modifier Methods
    def rolLDie(self):
        """
        updating DIE_NUMBER with a new number
        :return: None
        """
        self.__DIE_NUMBER = randint(1, self.__DIE_MAX)

    # --- Accessor Methods
    def getDieNumber(self):
        """
        send DIE_NUMBER to rest of program
        :return: int
        """
        return self.__DIE_NUMBER
