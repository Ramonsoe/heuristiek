# from code import classes
# from house import House
import numpy as np

from bokeh.plotting import figure, show


class Visual():

    def __init__(self, batteries, houses):

        self.batteries = batteries
        self.houses = houses
        self.coordinates_house_x = []
        self.coordinates_house_y = []
        self.coordinates_battery_x = []
        self.coordinates_battery_y = []

    def get_values(self):

        for house in self.houses:

            self.coordinates_house_x.append(house.x_house)
            self.coordinates_house_y.append(house.y_house)

        for bat in self.batteries:

            self.coordinates_battery_x.append(bat.x_battery)
            self.coordinates_battery_y.append(bat.y_battery)

        return self.coordinates_house_x, self.coordinates_house_y, self.coordinates_battery_x, self.coordinates_battery_y


    def make_plot(self, house_x, house_y, battery_x, battery_y):
        """Creates a gridplot with all the batteries and houses that are connected"""

        # empty grid
        grid = figure(plot_width = 1500 , plot_height = 600,
                        title='Smart Grid')
        # add houses
        grid.square(house_x, house_y, size=5)

        # add batteries
        grid.circle(battery_x, battery_y, size=10, color='red')

        #add cables
        # TO DO: Get all the cable sequences in separated x and y lists
        # grid.line([10,10],[10,40], line_width=0.5, color='black')

        return show(grid)
