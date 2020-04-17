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
        super().__init__()  # you can do it without this
        print('You just created BMW instance')

    def drive(self):
        super().drive()  # drive is inharitated from Car class
        print('You are driving BMW')  # I inharitated the Car.drive and changed it

    @staticmethod # This is something that python offered me
    def parking_sensor():
        print('This is the unique feature')


# c = Car()
# c.drive()
# c.stop()

b = BMW()
b.drive()
b.stop()
b.parking_sensor()
