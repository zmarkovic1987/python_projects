"""
Built-in Function
Creates a sequence of numbers, but does not save them in memory
Useful for generating numbers
"""

# print(range(0, 10))
# print(list(range(0, 10)))
#
# a = range(0, 10)
# b = range(0, 20, 2)
# c = range(0, 20, 3)
#
# print(a)
# print(type(a))
#
# print(b)
# print(list(b))
# print(list(c))
#
# print(list(a))
# print('*' * 20)
#
#
# for num in range(3):
#     print(num)
#
# print('*' * 20)
#
# for num in range(0, 3):
#     print(num)
#
# print('*' * 20)
#
# for num in range(1, 10, 2):
#     print(num)

name_list = ['Petar', 'Dusan', 'Milos', 'Milan', 'Marko']
m_name_liste = []
x = 0
print(name_list[x][0])

for n in name_list:
    if n[0] == 'M':
        print(n)
        m_name_liste.append(n)
    else:
        continue
print(m_name_liste)

print(name_list)

