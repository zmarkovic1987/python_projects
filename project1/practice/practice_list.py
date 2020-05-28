#
# menu = []
#
# menu.extend(['pizza', 'beer', 'fries', 'wings', 'salad'])
#
# menu.pop(1)
# menu.append(menu[0])
# menu[0] = menu[len(menu) - 2]
# menu.pop(len(menu) - 2)
#
# menu[1] = 'quinoa'
# menu[2] = 'steak'
# menu.pop()
# print(menu)

######################
s = [1,2,3,3,4,5,1,2,1]

def unique(l):
    unique_l = []
    for e in l:
        if e not in unique_l:
            unique_l.append(e)
    return unique_l

# print(unique(s))
# print(s)

######################
list_1 = [1,2,3,1,2,3,4,5,6,4,3,6,2,4,5,2,3,4,2,3]
list_2 = [2,3,4,1,5,2,3,1,2,1,5,6,6]

def common(l1, l2):
    unique_list_1 = unique(l1)
    unique_list_2 = unique(l2)

    a = 0
    b = 0

    for e in unique_list_1:
        if e not in unique_list_2:
            a += 1
        else:
            a += 0

    for e in unique_list_2:
        if e not in unique_list_1:
            b += 1
        else:
            b += 0

    if a + b == 0:
        return True
    else:
        return False


print(common([1,2,3,3], [2,3,1]))

###################

cities = 'san francisco, boston, chicago,indianapolis'
cities = cities.split(',')
cities.sort()
print(cities)


###############################

def permutation(l1, l2):
    a = 0
    b = 0

    for e in l1:
        if e not in l2:
            a += 1
        else:
            a += 0

    for e in l2:
        if e not in l1:
            b += 1
        else:
            b += 0

    if a + b == 0 and len(l1) == len(l2):
        return True
    else:
        return False


print(permutation([1,2,2,3], [2,3,1]))

