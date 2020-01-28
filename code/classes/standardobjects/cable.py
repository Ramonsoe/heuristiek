"""
cable.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File where cable objects are created.
"""


class Cable():

    def __init__(self, x1, y1, x2, y2):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


    def __repr__(self):

        return f"({x1,y1}) to ({x2,y2})"
