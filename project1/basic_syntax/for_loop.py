"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""

my_string = 'abcabc'

# for c in my_string:
#     print(c, end=' ')

for c in my_string:
     if c == 'a':
         print('A', end=' ')
     else:
         print(c, end=' ')


print('*' * 20)

cars = ['bmw', 'benz', 'honda']
print(cars)

for car in cars:
    print(car)

nums = [1, 2, 3]
for n in nums:
    print(n * 10, end=' ')
    if n == 3:
        print()

print('*' * 20)

dict1 = {'one': 1, 'two': 2, 'three': 3}
for k in dict1:
    print(k + ' ' + str(dict1[k]))

print('*' * 20)

# If you want to use multiple variables from Dictionary you have to loop in "dictionary.items()"
for k, v in dict1.items():
    print(k)
    print(v)

print('*' * 20)

# ITERATING MULTIPLE LISTS

list1 = [1,5,87,554,553,1,7,995,488]
list2 = [4,8,15,18,48,58,789,987]
list3 = [2, 6, 9, 25, 87, 35, 78]

for a, b, c in zip(list1, list2, list3):
    if a > b and c:
        print(a)
    elif b > a and c:
        print(b)
    else:
        print(c)

