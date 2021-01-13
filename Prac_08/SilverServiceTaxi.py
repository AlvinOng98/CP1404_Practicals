"""
CP1404/CP5632 Practical 8
Silver Service Taxi class
"""
from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * Taxi.price_per_km

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance + self.flagfall

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)