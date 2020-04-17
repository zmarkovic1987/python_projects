"""
Practices
Loops and FUnctions
"""

"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate
"""

# q = input('How long should be your Fibonnaci sequence? ')
# seq_num = int(q)
#
# fib = [1, 1]
#
# while len(fib) != seq_num:
#     if seq_num == 1:
#         print(1)
#         break
#     # x = fib[-1]
#     # y = fib[-2]
#     fib.append(fib[-1] + fib[-2])
#     if len(fib) == seq_num:
#         print(fib)
#         break

"""
Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.
"""

# l = [1, 2, 2, 1, 3, 4, 3,4]
# n = []
# def dup(x):
#     s = set(x)
#     print(s)

# def dup(x):
#     for num in l:
#         if num not in n:
#             n.append(num)
#     print(n)
#
# dup(l)

"""
Checking prime numbers
"""
# q = int(input('Number to check:'))
#
#
# def prime(num):
#     for x in list(range(2, num - 1)):
#         if num % x == 0:
#             print("not Prime")
#             break
#         else:
#             print("Prime number")
#             break
# prime(q)

"""
reverse the string
"""
# q = input('Type a sentance ')
#
# def rev():
#     print(list(q.split())[::-1])
# rev()

"""
Search for number in the list
"""
# l = [1,2, 4, 6, 12, 15, 17, 21, 25]
# def search(lis, number):
#     for x in l:
#         if number in lis:
#             print('True')
#             return True
#         else:
#             print('False')
#             return False
# search(l, 21)

"""
Ask User how many cubes he wants and draw it
"""
# q = input('How many cubes do you want?')
#
# root = int(q) ** 0.5
#
# l = range(0, int(root))
# def draw():
#     for x in l:
#         print(' --- ' * int(root))
#         print('|   |' * int(root))
#         print(' --- ' * int(root))
# draw()

"""
Password generator
"""
import random

# low = 'zxcvbnmasdfghjklqwertyu'
# up = low.upper()
# num = range(1, 10)
# spec = '!@#$%^&*()-=+_?><'
# weak = ['dog', 'cat', 'shit', 'weak']
#
# strength = input("Do you want a weak, medium, or strong, password?: ")
# def password():
#     # ran_low = random.choice(low)
#     # ran_up = random.choice(up)
#     # ran_num = str(int(random.random() * 10))
#     # ran_spec = random.choice(spec)
#     if strength == 'weak':
#         print(random.choice(weak))
#     elif strength == 'medium':
#         print(str(random.choice(low) + str(int(random.random() * 10)) + str(random.choice(low) + str(int(random.random() * 10)) + str(random.choice(low) + str(int(random.random() * 10))))))
#     else:
#         print(str(random.choice(low) + str(int(random.random() * 10)) + random.choice(spec) + random.choice(up) + random.choice(low) + str(int(random.random() * 10)) + random.choice(spec) + random.choice(up)))
#
# password()


"""
Random
Cows and Bulls
"""

ran_num = str(int(random.random() * 10000))
cow = 0
def cows_bulls(q_a):
    cows = 0
    bulls = 0
    # while q_a != ran_num:
    #     q_a = input('Guess a number:')

    for n in range(len(ran_num)):
        if q_a[n] == ran_num[n]:
            cows += 1
        elif q_a[n] in ran_num and q_a[n] != ran_num[n]:
            bulls += 1
    return cows, bulls


if __name__ == '__main__':
    while cow < 4:
        q_a = input('Guess a number:')
        cow, bulls = cows_bulls(q_a)
        print('cows: ' + str(cow))
        print('bulls: ' + str(bulls))
        if cow == 4:
            print("Congratulations!")

    # playing = True
    # q_a = input('Guess a number:')
    # ran_num = str(int(random.random() * 10000))

    # while q_a != ran_num:
    #     if q_a[x] == ran_num[x]:
    #         print('Cows')
    #         x =+ 1

    # print(ran_num)
    # print(q_a[0])
    # print(q_a[0])
    # if q_a[1] ==
