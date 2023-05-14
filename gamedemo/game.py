"""
game.py
_______


This module contains the Game class that implements the actual game mechanics as well as
the __main__ construct to make the game runnable.

"""

__author__ = "John Christopher Sloan"

import random

from skills import Attempt, Flow
from climbers import Climber

class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    def run(self):
        print('Welcome to the Red River Gorge Climbing Game')
        print(self.p1)
        print(self.p2)
        while self.p1.is_alive and self.p2.is_alive:
            if random.choice([True, False]):
                attacker = self.p1
                defender = self.p2
            else:
                attacker = self.p2
                defender = self.p1
            dmg, sound = attacker.weapon.redpoint_attempt()
            print(attacker.name, 'attacks:', sound)
            print(attacker.name, 'did', dmg, 'damage')
            defender.take_hit(dmg)
        print(attacker.name, 'won with', attacker.health, 'health left')


if __name__ == '__main__':
    random.seed()
    g = Game(Climber('Climber', Attempt()), Climber('Route', Attempt()))
    g.run()