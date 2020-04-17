"""
Classes Inheritance
"""


class Car(object):

    def __init__(self):
        print('You just created the Car instance')

    def drive(self):
        print('Car just started')

    def stop(self):
        print('Car stopped')

class BMW(Car):

    def __init__(self):
        super().__init__() # you can do it without this
        # Car.__init__(self) # this is other way to call this super class
        print('You just created BMW instance')


# c = Car()
# c.drive()
# c.stop()

b = BMW()
b.drive()
b.stop()

