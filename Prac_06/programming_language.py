"""CP1404/CP5632 Practical - programming language"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """initialise a programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """checks if programming language is dynamic or not"""
        if self.typing == "Static":
            return False
        else:
            return True

    def __str__(self):
        return "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)