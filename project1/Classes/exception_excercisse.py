"""
Exception exercise from udemy course
"""

car = {'make': 'bmw', 'model': 'E350i', 'year': '2018'}

try:
    print(car['color'])
except:
    print('This is the exception block')
finally:
    print('Finally is always executed')

