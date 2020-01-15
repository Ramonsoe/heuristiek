# from code import classes
# from house import House
import numpy as np

from bokeh.plotting import figure, show

from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid
from bokeh.models.glyphs import MultiLine
from bokeh.io import curdoc, show
from code.classes import cables, batteries, houses
import copy

class Visual():

    def __init__(self, houses, batteries):

        self.batteries = batteries
        self.connected_houses = houses


        self.coordinates_house_x = []
        self.coordinates_house_y = []
        self.coordinates_battery_x = []
        self.coordinates_battery_y = []

        self.coord_cable_x = []
        self.coord_cable_y = []
        self.coords_all_x = []
        self.coords_all_y = []

    def get_values(self):
        """Setting x and y coordinates of batteries and houses in separate lists"""

        for house in self.connected_houses:

            self.coordinates_house_x.append(house.x_house)
            self.coordinates_house_y.append(house.y_house)

        for bat in self.batteries:

            self.coordinates_battery_x.append(bat.x_battery)
            self.coordinates_battery_y.append(bat.y_battery)

        return self.coordinates_house_x, self.coordinates_house_y, self.coordinates_battery_x, self.coordinates_battery_y

    def houses_to_cables(self):
        """Creates two lists of x and y cable coordinates per house"""

        pass

    def make_plot(self, house_x, house_y, battery_x, battery_y):
        """Creates a gridplot with all the batteries and houses that are connected"""

        # empty grid
        grid = figure(plot_width = 1500 , plot_height = 600,
                        title='Smart Grid')
        # add houses
        grid.square(house_x, house_y, size=5)

        # add batteries
        grid.circle(battery_x, battery_y, size=10, color='red')

        # add cables to grid
        for house in self.connected_houses:

            kabels = house.cables

            # append x and y coords separately
            for coordinates in kabels[0]:

                x = coordinates[0]
                y = coordinates[1]

                self.coord_cable_x.append(x)
                self.coord_cable_y.append(y)

            # append x and y coords in lists
            self.coords_all_x.append(copy.deepcopy(self.coord_cable_x))
            self.coords_all_y.append(copy.deepcopy(self.coord_cable_y))

            # clear temporary list
            self.remove_coords()

        x_all = self.coords_all_x
        y_all = self.coords_all_y
        # print(x_all)
        grid.multi_line(x_all, y_all)
        show(grid)

    def remove_coords(self):
        """Clears the temporary lists"""

        self.coord_cable_x.clear()
        self.coord_cable_y.clear()
