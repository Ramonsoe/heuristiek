
class Powersource():
    """Als een huis of kabel verbonden is, wordt het een powersource"""

    def __init__(self, object):
        """init hier objecten uit (kabels, batterijen en huizen)"""

        self.x_power = object.x
        self.y_power = object.y
        # self.battery = battery

"""To do:

    - Powersource wordt elk nieuw punt waaraan iets verbonden kan worden
        - Dus elk connect_huis en elk coordinaat van een kabel is nieuwe bat
    -
    -
    -



"""
