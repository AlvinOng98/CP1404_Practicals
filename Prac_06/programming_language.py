"""CP1404/CP5632 Practical - programming language"""


class ProgrammingLanguage:

    def __init__(self, typing, reflection, year):
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Static":
            return False
        else:
            return True
