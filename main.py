"""
title: Main game file for Ship, Captain, Crew!
author: joanna hao
date-created: 2023-11-30
"""
from c_game import Game


class Main:
    GAME = Game()
    GAME.setup()
    GAME.run()


if __name__ == "__main__":
    Main()
