"""CP1404/CP5632 Practical - guitar class."""


class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name, year, cost):
        self.name = ""
        self.year = 0
        self.cost = 0
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        CURRENT_YEAR = 2020
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        if self.get_age(self.year) >= 50:
            return True
        else:
            return False
