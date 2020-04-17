"""
Built in modules
https://docs.python.org/3/library/
"""

import math


class ModulesDemo():

    def built_in_modules(self):
        print(math.sqrt(100))


m = ModulesDemo()
m.built_in_modules()


from math import sqrt
# Importing only sqrt function from math Module

class ModulesDemo2():
    def built_in_modules(self):
        print(sqrt(36))


m2 = ModulesDemo2()
m2.built_in_modules()
