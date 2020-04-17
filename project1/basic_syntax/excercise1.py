"""
state name and gross income that you make
federal Tax = 10%
state Tax = 5%
income 100000
x = 100000 * 0.1
x = x * 0.05
net = 100000 - x
"""

fed_tax = 0.1
states = {'ny': 0.08, 'ca': 0.075, 'fl': 0.05}

# MY WAY
# def net(state, gross):
#     for k,v in states.items():
#         if state == k:
#             x = gross * fed_tax
#             y = gross - x
#             w = y * v
#             z = gross - (x + w)
#             print('Your net income is: ' + str(z))
#             return z
#         # else:
#         #     print('State is not in the list')
#
#
# net('ny', 100000)

#CORRECT WAY

def net(state, gross):
    # find the income after fed tax
    x = gross - (gross * fed_tax)

    # find a net income after state tax
    if state in states:
        x = x - (x * states[state])
        print('Your net income is: ' + str(x))
        return x
    else:
        print('state ' + state + ' is not in the list')
        # return None

net('fl', 100000)





