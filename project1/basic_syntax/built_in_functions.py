"""
Some of the built-in-function

max()
min()
abs() -> absolute value of the number. Only single number
type() - > Returns the type of the data of the argument it receives
"""

l = [1, 2, 3, 4, 5, 6, -4]

print(max(l))
print(min(l))
print(abs(min(l)))

print('*' * 20)

def largest_num(*args):
    print(max(args))



largest_num(-9, 0, 4, 7, 12)


def smallest_num(*args):
    return min(args)

x = smallest_num(-9, 0, 4, 7, 12)
print(x)


def absolute(a):
    print(abs(a))

absolute(-13)
absolute(21)


def type1(a):
    print(type(a))

type1(1)
type1(1.11)
type1('1.1')
type1(l)

print('*' * 20)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
