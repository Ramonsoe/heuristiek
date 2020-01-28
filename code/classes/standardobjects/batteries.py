"""
batteries.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File where battery objects are saved in a list of all batteries.
"""


import csv
from .battery import Battery


class Batteries():
    """batteries are loaded from the csv file"""

    def __init__(self, battery_file):
        self.batteries = self.read_batteries(battery_file)


    def read_batteries(self, battery_file):
        """Loads all the batteries into a list"""

        battery_objects = []
        with open(battery_file, "r") as csv_file:
            reader = csv.reader(csv_file)
            batteries = list(reader)
            batteries.pop(0)

            for b in batteries:
                xy = b[0]
                xy = xy.strip('[]')
                xy = xy.split(", ")
                capacity = b[1].strip(' ')
                battery = Battery(xy[0], xy[1], capacity)
                battery_objects.append(battery)

        return battery_objects
