"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
# name = input('Whats your name?')
# age = input('Thats your age')
# def hundred(name, age):
#     year = 2020
#     x = (100 - age) + year
#     print('Hello ' + name + ', it will be year ' + str(x) + ' when you turn 100')
#     # print()
#
# hundred('Zarko', 33)
#
# odd_or_even = 1231
# if odd_or_even % 2 == 0:
#     print('even')
# else:
#     print('odd')

"""
Take a list, 
and write a program that prints out all the elements of the list that are less than 5.
"""
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
#
# for x in a:
#     if x < 5:
#         b.append(x)
#     else:
#         None
# print(b)
#
# # one line code
# print([x for x in a if x < 5])

"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number
"""

# num = 100
# l = []
#
# for x in range(1, num+1):
#     if num % x == 0:
#         l.append(x)
#
# print(l)

"""
Lists overlap
"""

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# x = 0
# # y = b[x]
#
# # while x != b[0]:
# for same in b:
#     if same in a:
#         c.append(same)
#         continue
#
# print(c)


# wrd = '1234321'
# rvs = wrd[::-1]
# print(rvs)
# if wrd == rvs:
#     print("This word is a palindrome")
# else:
#     print("This word is not a palindrome")

"""
even numbers
"""
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# # one line
# b = [x for x in a if x % 2 == 0]
#
#
# # for x in a:
# #     if x % 2 == 0:
# #         b.append(x)
# print(b)


# x = 'rock'
# y = 'paper'
# if x == 'rock' and y == 'scissors':
#     print('x wins')
# elif x == 'rock' and y == 'paper':
#     print('y wins')
# elif x == 'scissors' and y == 'paper':
#     print('x wins')
# elif x == 'scissors' and y == 'rock':
#     print('y wins')
# elif x == 'paper' and y == 'rock':
#     print('x wins')
# elif x == 'paper' and y == 'scissors':
#     print('y wins')
# else:
#     print('even')
#



# user1 = input("What's your name?")
# user2 = input("And your name?")
# user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
# user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)
#
# def compare(u1, u2):
#     if u1 == u2:
#         return("It's a tie!")
#     elif u1 == 'rock':
#         if u2 == 'scissors':
#             return("Rock wins!")
#         else:
#             return("Paper wins!")
#     elif u1 == 'scissors':
#         if u2 == 'paper':
#             return("Scissors win!")
#         else:
#             return("Rock wins!")
#     elif u1 == 'paper':
#         if u2 == 'rock':
#             return("Paper wins!")
#         else:
#             return("Scissors win!")
#     else:
#         return("Invalid input! You have not entered rock, paper or scissors, try again.")
#
# print(compare(user1_answer, user2_answer))


"""
Enter the number and compare to random number
"""
# import random
# q = 0
# c = 0
#
# while q != 'exit':
#
#     q = input('Whats your number')
#     if q == "exit":
#         break
#     user_number = int(q)
#     bot_num = random.choice(range(1, 9))
#     print('Bot number is: ' + str(bot_num))
#     c += 1
#     if user_number > bot_num:
#         print("you win")
#     elif user_number < bot_num:
#         print('bot won')
#     else:
#         print('tie')
#
# print('Games played: ' + str(c))


