"""
Excercisse from Udemy course
"""

class Fruit(object):

    def __init__(self):
        print('This is the Fruit class')

    def nutrition(self):
        print('The nutriton of this Fruit is:')

    def fruit_shape(self):
        print('The fruit shape')

class Orange(Fruit):

    def __init__(self):
        super().__init__()
        print('The Oranges')

    def nutrition(self):
        super().nutrition()
        print('Grade B')

    def color(self):
        print('The Color of Oranges is Orange')



c = Fruit()
c.nutrition()
c.fruit_shape()

b = Orange()
b.nutrition()
b.color()
b.fruit_shape()