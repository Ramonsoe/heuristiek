"""
cablepoint.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File in which cable point objects are created.
"""

class Cablepoint(object):

    def __init__(self, x, y, battery):

        self.x = x
        self.y = y
        self.battery = battery

    def __repr__(self):

        return f"|{self.x, self.y}, {self.battery}|"
