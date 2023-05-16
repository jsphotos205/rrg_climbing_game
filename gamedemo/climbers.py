"""
climbers.py
___________

This module contains the Climber class that represents game characters.
"""

__author__ = "John Christopher Sloan"


class Climber:
    """
    The Climber class represents the climber in the game.
    :ivar health: The current health of the climber. Statrts at 100.
    Once the health reaches 0 the climber falls off the route.
    """

    def __init__(self, name, attribute):
        """
        Create a new Climber
        :param name: The name of the Climber.
        :param attribute: Is the skill the climber chooses to use.
        """
        self.name = name
        self.attribute = attribute
        self.health = 100

    def take_hit(self, damage):
        """
        This method gets called when the Climber takes a hit from Route.
        :param damage: The damage the climber takes. This will be subtracted from
        :attr:'health'.
        :return: The new value of :attr: health
        """
        self.health -= damage
        return self.health

    @property
    def is_alive(self):
        """True if :attr: 'health' is larger than 0, False otherwise"""
        return self.health > 0

    def __str__(self):
        return "The {} has {} health and brings his {} to the climb!".format(
            self.name, self.health, type(self.attribute).__name__
        )


class Route:
    """
    The Route class represents the route the climber is trying to climb.
    :ivar health: The current health of the route. Starts at 100.
    Once the health reaches 0 the route has been sent by the climber.
    """

    def __init__(self, name, attribute):
        """
        Create a new Route
        :param name: The name of the Route.
        :param attribute: Is the attribute the route has that determines the difficulty of the Route.
        """
        self.name = name
        self.attribute = attribute
        self.health = 100

    def take_hit(self, damage):
        """
        This method gets called when the Route takes a hit from the Climber.
        :param damage: The damage the route takes. This will be subtracted from
        :attr:'health'.
        :return: The new value of :attr: health
        """
        self.health -= damage
        return self.health

    @property
    def unsent(self):
        """True if :attr: 'health' is larger than 0, False otherwise"""
        return self.health > 0

    def __str__(self):
        return "The {} is still standing with {} feet left to climb!".format(
            self.name, self.health
        )
