"""
Built in methods for manipulating the list
"""


cars = ['bmw', 'honda', 'audi']
print(cars)

length = len(cars)
print(length)

cars.append('Jeep')
print(cars)
print('*#' * 20)

x = cars.pop(-3)
print(x)
print(cars)

cars.insert(1, 'honda')
print(cars)

y = cars.index('honda')
print(y)
cars.remove('bmw')
print(cars)

cars.pop()
cars.insert(0, 'bmw')
print(cars)

slicing = cars[1:]
print(slicing)
slicing = cars[0:2]
print(slicing)

slicing = cars[0:len(cars)-1]
print(slicing)
print("*" * 20)
print(cars)

cars.sort()
sorted_list = ['c', 'f', 't', 'y', 'a']
sorted_list.sort()

print(cars)
print(sorted_list)









