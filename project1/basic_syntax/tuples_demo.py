"""
Tuple
Like a list but immutable
It means you cant change them
"""

my_list = [1, 2, 3]
print(my_list)

my_list[0] = 3
print(my_list)

my_tuple = (1, 2, 3,2,2,3,3,1,2,3,2,1,2)
print(my_tuple)


print(my_tuple[0])

print(my_tuple[1:])

print(my_tuple.index(1))

print(my_tuple.count(3))
