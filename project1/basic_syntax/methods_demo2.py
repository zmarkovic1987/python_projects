"""
Positional Parameters
They are like optional parameters
Anc can be assigned a default value, if no value is provided from outside
"""


def num_sum(x=2, y=3):
    """
    Get sum of 2 numbers
    :param x:
    :param y:
    :return:
    """
    return x + y


sum1 = num_sum()
sum2 = num_sum(y=5)
sum3 = num_sum(x=10)
sum4 = num_sum(x=20, y=10)

sum5 = num_sum(1, y=3)
sum6 = num_sum(1, 2)

print(sum1)
print(sum2)
print(sum3)
print(sum4)
print(sum5)
print(sum6)
