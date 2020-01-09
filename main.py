<<<<<<< HEAD
from code.algorithms import *
from code.classes import batteries
from code.visualisation import *

if __name__ == "__main__":
    bat = Batteries()
    bat.read_batteries('data/wijk1_batterijen.csv')
=======
# from code.algorithms import read_batteries
from code.classes import batteries

# from code.visualisation import *

if __name__ == "__main__":

    bat = batteries.Batteries('data/wijk1_batterijen.csv')
>>>>>>> f2e732423c2696cba1ab807f41af4072c573599c
