"""
Object Orientated Programming
"""

class Car(object):

    def __init__(self, make, model='124'):
        self.make_car = make
        self.model = model

c1 = Car('bmw', '550i')
print(c1.make_car)
print(c1.model)

c2 = Car('Benz')
print(c2.make_car)
print(c2.model)


