"""
Variable Scope

"""

a = 10


def test_method(a):
    print('Value of local is: ' + str(a))
    a = 2
    print('Value of local is: ' + str(a))


print('Value of Global is: ' + str(a))
test_method(a)
print('Did the value of global changed? ' + str(a))

print('*' * 20)

b = 20


def test_method2():
    global b
    print('Value of local is: ' + str(b))
    b = 2
    print('New value of "b" inside the code changed to: ' + str(b))


print('Value of Global is: ' + str(b))
test_method2()
print('Did the value of global changed? ' + str(b))


