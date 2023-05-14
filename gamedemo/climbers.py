"""
climbers.py
_________

This module contains the Climber class that represents game characters.
"""

__author__ = 'John Christopher Sloan'

class Climber:
    """
    The Climber class represents the climber in the game.
    """

    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100

    def take_hit(self, damage):
        self.health -= damage
        return self.health
    
    @property
    def is_alive(self):
        """True if :attr: 'health' is larger than 0, False otherwise"""
        return self.health > 0
    
    def __str__(self):
        return "Player {} has {} health and bring his {} to the fight".format(
            self.name, self.health, type(self.weapon).__name__
        )