# from code import classes
# from house import House
import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid, Range1d
from bokeh.models.glyphs import MultiLine, ImageURL
from bokeh.io import curdoc, show
from code.classes import cableslayla, batteries, houses
import copy

class Visual():

    def __init__(self, houses, batteries, x, y):

        self.batteries = batteries.batteries
        self.connected_houses = houses

        self.coordinates_house_x = []
        self.coordinates_house_y = []

        self.coordinates_battery_x = []
        self.coordinates_battery_y = []

        self.x_coordinates_cables = x
        self.y_coordinates_cables = y

        self.get_values()
        self.make_plot()

    def get_values(self):
        """Setting x and y coordinates of batteries and houses in separate lists"""

        for house in self.connected_houses:

            # append x and y coords of houses separately
            self.coordinates_house_x.append(house.x_house)
            self.coordinates_house_y.append(house.y_house)

        # same for batteries
        for bat in self.batteries:

            self.coordinates_battery_x.append(bat.x_battery)
            self.coordinates_battery_y.append(bat.y_battery)

    def make_plot(self):
        """Creates a grid plot with all the batteries and houses that are connected"""
        
        # url = "static/house.png"

        list_squares = copy.deepcopy(self.coordinates_house_y)
        list_bats = copy.deepcopy(self.coordinates_battery_x)

        for i in range(len(list_squares)):
            list_squares[i] -= 0.35

        for i in range(len(list_bats)):
            list_bats[i] -= 0.1

        # empty grid
        grid = figure(plot_width = 1500 , plot_height = 600,
                        title='Smart Grid')
        
        # add cables to grid
        grid.multi_line(self.x_coordinates_cables, self.y_coordinates_cables, alpha=0.3)

        # add houses
        grid.square(self.coordinates_house_x, list_squares, size=5, color='#cc6600')
        grid.triangle(self.coordinates_house_x, self.coordinates_house_y, size=5, color='#cc6600')

        # add batteries
        grid.rect(self.coordinates_battery_x, self.coordinates_battery_y, width=0.5, height=0.8, color='green')
        grid.rect(list_bats, self.coordinates_battery_y, width=0.5, height=0.4, color='green')


        # plot
        show(grid)

