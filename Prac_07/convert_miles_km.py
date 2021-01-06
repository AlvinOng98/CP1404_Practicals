"""
CP1404 Practical 7
Student Name: Alvin Ong Zhi Xiang
Miles to KM converter
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesToKmConverter(App):
    """MilesToKmConverter calculates and converts Miles to Km"""

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_miles(self):
        try:
            value = float(self.root.ids.miles_input.text)
            return value
        except ValueError:
            return 0


MilesToKmConverter().run()
