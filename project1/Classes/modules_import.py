"""
Importing modules
"""

# import modules_external.car as car # not good way
# from modules_external import car  # same as above but better way
from modules_external.car import info # best practice, importing only function that you need from a class

class ModulesDemo():

    def car_description(self):
        make = 'BMW'
        model = '550i'
        # car.info(make, model)
        info(make, model) # best practice


m = ModulesDemo()
m.car_description()
