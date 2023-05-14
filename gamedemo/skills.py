"""
skills.py
_________

This module contains classes for Skills.
"""

__author__ = "John Christopher Sloan"

from abc import ABC, abstractmethod
import random


class Skills(ABC):
    """This abstract class defines the method :meth: 'tryhard' that should be implemented by subclasses."""

    @abstractmethod
    def redpoint_attempt(self, other):
        """This method should return a tuple (damage, text) : how much damage was dealt to the climber and what text to ouput.
        Text is a format string with placeholders for the climber.
        """


class Attempt(Skills):
    """This class is the subclass of :class: 'Skills'
    It represents the hold type the climber will implement to get through the route.
    """

    def redpoint_attempt(self):
        return (
            random.choice([10, 15]),
            random.choice(
                [
                    "Dyno for the jug",
                    "Crimp for dear life",
                    "Kneebar the way through a crux",
                ]
            ),
        )


class Flow(Skills):
    """Flow is only used by RockClimbingWizards or RockClimbingMuses.
    It can deal alot of damage, but has its drawbacks.
    There is a 30% chance that flow attempt will not work, and after a successful flow attempt you will need to wait a while
    before you will be able to access Flow again.
    """

    def __init__(self):
        # The amount of time you will have to wait until you can access FLOW.
        self._cooldown = 0

    def attack(self):
        if self._cooldown <= 0:
            dmg = random.choice([0, 40])
            if dmg > 0:
                self._cooldown = 2
                sound = "I've got this"
            else:
                sound = "Ok maybe I wasn't giving it my all"
            return dmg, sound
        else:
            self._cooldown -= 1
            return (
                0,
                "Awww man! That was a good attempt, I'll give it one more go, but I'm going to have to wait awhile.",
            )
