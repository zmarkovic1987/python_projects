"""
Nested Dictionary
x = {'k1': {'nestkey1' : 'nestval1', 'nestkey2' : 'nestval2'}}
x['k1']['nestkey1']

"""

cars = {'bmw': {'model': '550i', 'year': 2016 }}
print(cars)
print(cars['bmw'])
print(cars['bmw']['model'])

cars['benz'] = {'model': 'E350', 'year': 2015}
print(cars)
print(cars['benz'])
benz_year = cars['benz']['year']
print(cars['benz']['year'])
print(benz_year)


