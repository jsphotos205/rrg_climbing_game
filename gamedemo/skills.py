"""
skills.py
_________

This module contains classes for Skills.
"""

__author__ = "John Christopher Sloan"

from abc import ABC, abstractmethod
import random


class Skills(ABC):
    """This abstract class defines the method :meth: 'redpoint_attempt' that should be implemented by subclasses."""

    @abstractmethod
    def redpoint_attempt(self, other):
        """This method should return a tuple (damage, text) : how much damage was dealt to the climber and what text to ouput.
        Text is a format string with placeholders for the climber.
        """


class TryHard(Skills):
    """This class is the subclass of :class: 'Skills'
    It represents the skill type the climber will implement to get through the route.
    """

    def redpoint_attempt(self):
        return (
            random.randrange(1, 10),
            # random.choice([5, 10, 15, 25, 50]),
            random.choice(
                [
                    "dyno for a jug",
                    "full crimp",
                    "a creative kneebar rest",
                    "good beta",
                    "sick mono-pocket",
                    "heel hook",
                    "sneaky rest to recover",
                    "RECOVER!"
                ]
            ),
        )

class RouteDefense(Skills):
    """This class is the subclass of :class: 'Skills'
    It represents the attribute of the route that determines the routes difficulty. 
    """
    def redpoint_attempt(self):
        return(
            random.randrange(1,10),
            # random.choice([10, 15, 5, 20, 2, ]),
            random.choice(
                [
                    "sneaky missed hold.",
                    "left halfpad crimp",
                    "right halfpad crimp",
                    "sloper",
                    "razorblade crimp",
                    "credit card thin crimp",
                    "choss paddling",
                    "missed kneebar",
                    "pumpy climbing",
                    "choss",
                    "crumbly feet",
                    "hard to read beta",
                    "holds that are a bit too far"
                ]
            )
        )

# class Flow(Skills):
#     """Flow is only used by RockClimbingWizards or RockClimbingMuses.
#     It can deal alot of damage, but has its drawbacks.
#     There is a 30% chance that flow attempt will not work, and after a successful flow attempt you will need to wait a while
#     before you will be able to access Flow again.
#     """

#     def __init__(self):
#         # The amount of time you will have to wait until you can access FLOW.
#         self._cooldown = 0

#     def attack(self):
#         if self._cooldown <= 0:
#             dmg = random.choice([0, 40])
#             if dmg > 0:
#                 self._cooldown = 2
#                 sound = "I've got this"
#             else:
#                 sound = "Ok maybe I wasn't giving it my all"
#             return dmg, sound
#         else:
#             self._cooldown -= 1
#             return (
#                 0,
#                 "Awww man! That was a good attempt, I'll give it one more go, but I'm going to have to wait awhile.",
#             )
