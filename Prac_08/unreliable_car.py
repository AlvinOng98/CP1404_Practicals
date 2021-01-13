"""
CP1404/CP5632 Practical 8
Unreliable car class
"""

from Prac_08.car import Car
import random


class UnreliableCar(Car):
    """Unreliable version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if random.randint(1, 101) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            distance_driven = 0
            return distance_driven

    def __str__(self):
        """Return a string like a Car"""
        return "{}".format(super().__str__())
