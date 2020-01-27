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

        self.batteries = batteries.batteries
        self.connected_houses = houses

        self.coordinates_house_x = []
        self.coordinates_house_y = []
        self.coordinates_battery_x = []
        self.coordinates_battery_y = []

        self.coord_cable_x = []
        self.coord_cable_y = []
        self.coords_all_x = []
        self.coords_all_y = []

        # self.get_values()
        # self.make_plot()
        self.color_plot()
        # self.test_plot()
    def get_values(self):
        """Setting x and y coordinates of batteries and houses in separate lists"""

        for house in self.connected_houses:

            # append x and y coords of houses separately
            self.coordinates_house_x.append(house.x)
            self.coordinates_house_y.append(house.y)
            #
            kabels = house.cables
            # print(kabels)
            # append x and y coords of cables separately
            for cablepoint in kabels[0]:

                # x = coordinates[0]
                # y = coordinates[1]

                self.coord_cable_x.append(cablepoint.x)
                self.coord_cable_y.append(cablepoint.y)

            # append x and y coords in lists
            self.coords_all_x.append(copy.deepcopy(self.coord_cable_x))
            self.coords_all_y.append(copy.deepcopy(self.coord_cable_y))

            # clear temporary list
            self.remove_coords()

        # same for batteries
        for battery in self.batteries:

            self.coordinates_battery_x.append(battery.x)
            self.coordinates_battery_y.append(battery.y)

    def make_plot(self):
        """Creates a gridplot with all the batteries and houses that are connected"""

        # empty grid
        grid = figure(plot_width = 1500 , plot_height = 600,
                        title='Smart Grid')
        # add houses
        grid.square(self.coordinates_house_x, self.coordinates_house_y, size=5)

        # add batteries
        grid.circle(self.coordinates_battery_x, self.coordinates_battery_y, size=10, color='red')

        # add cables to grid
        grid.multi_line(self.coords_all_x, self.coords_all_y)
        #
        # # plot
        show(grid)

    def remove_coords(self):
        """Clears the temporary lists"""

        self.coord_cable_x.clear()
        self.coord_cable_y.clear()

    def color_plot(self):

        color = ['blue','red','black','orange','green']
        i = -1
        color_list = []
        for battery in self.batteries:

            self.coordinates_battery_x.append(battery.x)
            self.coordinates_battery_y.append(battery.y)


            i += 1
            for house in battery.houses:

                self.coordinates_house_x.append(house.x)
                self.coordinates_house_y.append(house.y)

                color_list.append(color[i])
                cablez = house.cables[0]

                for cable in cablez:

                    self.coord_cable_x.append(cable.x)
                    self.coord_cable_y.append(cable.y)

                self.coords_all_x.append(copy.deepcopy(self.coord_cable_x))
                # print(self.coords_all_x)
                self.coords_all_y.append(copy.deepcopy(self.coord_cable_y))
                self.remove_coords()

        # empty grid
        grid = figure(plot_width = 1500 , plot_height = 600,
                        title='Smart Grid')
        # add houses
        grid.square(self.coordinates_house_x, self.coordinates_house_y, size=5)

        # add batteries
        grid.circle(self.coordinates_battery_x, self.coordinates_battery_y, size=10, color='red')

        # add cables to grid
        grid.multi_line(self.coords_all_x, self.coords_all_y, color=color_list)

        show(grid)


    def test_plot(self):
        # empty grid
        grid = figure(plot_width = 1500 , plot_height = 600,
                        title='Smart Grid')
        # add houses
        # grid.square(self.coordinates_house_x, self.coordinates_house_y, size=5)
        # # add batteries
        # grid.circle(self.coordinates_battery_x, self.coordinates_battery_y, size=10, color='red')

        for battery in self.batteries:
            print(battery.houses)
