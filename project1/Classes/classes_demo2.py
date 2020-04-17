"""
Object Orientated Programming
"""


class Car(object):

    wheels = 4

    def __init__(self, make, model, color):
        self.s_make = make
        self.s_model = model
        self.s_color = color

    def info(self):
        print(self.s_make)
        print(self.s_model)

c1 = Car('bmw', '550i', "green")
print(c1.s_make + ' ' + c1.s_color)
# c1.wheels = 3 #This is wrong
# print(c1.wheels) # This is wrong
c1.info()

c2 = Car('Benz', 'E350', 'gray')
c2.info()
# print(c2.make_car)
# print(c2.wheels)

print(Car.wheels) # This is correct
