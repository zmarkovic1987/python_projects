"""
Exceptions are errors.
We should handle exceptions in our code
"""


def exception_handling2():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)
    except:
        print('This is the exception block. Error occured')
        # raise Exception # To see all errors in exception
    else:
        print('There was no exception, so the ELSE is executed')
    finally:
        print('Finally is always executed, no matter what')


exception_handling2()


# def exception_handling():
#     try:
#         a = 10
#         b = 20
#         c = 0
#
#         d = (a + b) / c
#         print(d)
#     # except ZeroDivisionError:
#     #     print('Cant divide by Zero')
#     # except TypeError:
#     #     print('Cant add string to integer')
#     except:
#         print('This is the exception block. Error occured')
#
#
# exception_handling()
