"""
Dictionary stores more than one variable name, in key:value pairs
x = {'k1':'v1', 'k2','v2'}
No indexing just Mapping
"""

car = {'make':'bmw', 'model':'550i', 'year':2016}
print(car)

x = car['make']
print(x)
print(car['make'])

car['fuel'] = 'diesel'
print(car)

y = car['fuel']
print(y)

print('*#' * 20)

d = {}
print(d)

d['one'] = 1
d['two'] = 2
print(d)

sum1 = d['two'] + 8
print(sum1)

sum1 = sum1 + d['one']
print(sum1)

sum1 = (sum1 - d['one']) / d['two']
print(sum1)
print(d)

d['two'] = d['two'] + 8
print(d)

