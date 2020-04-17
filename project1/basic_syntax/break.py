"""
Break: To break out of the loop
Continue: Go to the start od the loop
"""
x = 0
while x < 10:
    print('Value of x is: ' + str(x))
    x += 1

    if x == 8:
        break
    print('This example is awesome')
    print('*' * 20)
# in case that break is executed the else will not execute (print)
else:
    print('Just broke out of the loop')

# x = 0
# while x < 10:
#     print('Value of x is: ' + str(x))
#     x += 1
#
#     if x == 8:
#         continue
#     print('This example is awesome')
#     print('*' * 20)
# # Continue means stop this iteration (do not print 'this example is awesome'),
# # but continue with the next loop
# print('Just broke out of the loop')
#


