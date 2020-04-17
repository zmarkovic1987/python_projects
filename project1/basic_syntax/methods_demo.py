def num_sum(x, y):
    """
    Get sum of 2 numbers
    :param x:
    :param y:
    :return:
    """
    return x + y


sum1 = num_sum(4, 5)
sum2 = num_sum(5, 10)

print(sum1)
print(sum1 + sum2)

string_add = num_sum('one', 'two')
print(string_add)

print('*' * 20)

def isMetro(city):
    l = ['sfo', 'nyc', 'la']

    if city in l:
        print(city)
        return True
    else:
        print('No metro in ' + city)
        return False


x = isMetro('sfo')
print(x)

y = isMetro('Miami')
print(y)



l1 = [1, 2, 3]
print(l1)

l1.append(4)
print(l1)

print(len(l1))
