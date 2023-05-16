"""
game.py
_______


This module contains the Game class that implements the actual game mechanics as well as
the __main__ construct to make the game runnable.

"""

__author__ = "John Christopher Sloan"

import random

from skills import TryHard, RouteDefense
from climbers import Climber, Route


class Game:
    """
    The Game class implements the game mechanics. To understand the way the
    game works, read the documentation for the :meth:'run' method.
    """
    def __init__(self, player1, player2):
        """
        Create a new game with two players.

        :param player1: First player
        :type player1: :class:`Climber`
        :param player2: Second player
        :type player2: :class:`Route`
        """
        self.p1 = player1
        self.p2 = player2

    def run(self):
        """
        This method implements the game mechanics. The game loops until
        one of the players runs out of health. Every turn, one of the players
        is randomly chosen to attack. We call the :meth: 'skills.redpoint_attempt' method
        on that players skills. The damage dealt by this skill is applied to the player
        by calling :meth: 'climbers.Climber.take_hit'.

        """
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to the Red River Gorge Climbing Game")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.p1)
        print(self.p2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while self.p1.is_alive and self.p2.unsent:
            if random.choice([True, False]):
                attacker = self.p1
                defender = self.p2
            else:
                attacker = self.p2
                defender = self.p1
            dmg, sound = attacker.attribute.redpoint_attempt()
            print("The", attacker.name, "deals", sound)
            print("The", attacker.name, "did", dmg, "damage to the", defender.name)
            defender.take_hit(dmg)
            print(attacker.name, "has", attacker.health, "health")
            print(defender.name, "has", defender.health, "health")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("The", attacker.name, "won with", attacker.health, "health left")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    random.seed()
    g = Game(Climber("Climber", TryHard()), Route("Route", RouteDefense()))
    g.run()
