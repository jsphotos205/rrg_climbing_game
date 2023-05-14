# Notes

redriver = pluralsight

## init = init

    Just a simple explination of the layout of the game and how I would like for it to work.

## climbers.py = player.py

Climber is the character in the game

* The climber has a name, skill, and health meter
* The climber is either falling or still_climbing and  it has affects on the health meter.
* When the climber uses bad_beta, the health meter is decreased.
* When the climber is still_climbing, the health meter is increased.
* When the climber is sending, the health meter is > | = 60
* When the climber is not_sending, the health meter is < | = 60
* When the climber is falling, the health meter is 0 and the climber did not SEND the route.

## skills.py = weapons.py

    uses modules[abc](https://docs.python.org/3/library/abc.html)(abstractclassmethod) and [random](https://docs.python.org/3/library/random.html)

* class Skill
  * contains a method that is a redpoint attempt by the climber
* class Attempt
  * uses the methods found in Skills in order to determine if the climber will send the route
* class Flow
  * uses methods found in Skills
  * _cooldown is the time you have until you can access FLOW again
