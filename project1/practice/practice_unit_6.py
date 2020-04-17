# # print('some_String'.find('ing'))
# # print('variables have no spaces'.replace(' ', '_'))
# # a = 'python 4 ever&EVER'
#
# x = input('Whats your name? ')
#
# print((x + ' \n') * 3)
# # print(a.count(' '))
# # print(a.count(' 4 '))
# # print(a.count('eVer'))
# # print("on" in a)
# # print(" " in a)
# # print("2 8 2 " in a)
# #
# # print(a.find('E'))
# # print(a.find('eve'))
# # print(a.rfind('rev'))
# # print(a.rfind('VER'))
# # print(a.find(' '))
# # print(a.rfind(' '))


"""
input first last name
input2 first last name
cut the first and last name - i will find the " "
cut the first and last name 2
cut the halfs of all names - find len, then cut in half
mash up
print
Zar ko Te st
Te st Zar ko
Zar st Te rko
Ter ko Za st

"""

name1 = input('Enter your First and Last name: ')
name2 = input('Enter your First and Last name: ')
# name1 = "Zarko Test"
# name2 = "Test Zarko"

first_1 = name1.find(" ")
first_name_1 = name1[0:first_1]
last_name_1 = name1[first_1+1:]

first_2 = name2.find(" ")
first_name_2 = name2[0:first_2]
last_name_2 = name2[first_2+1:]

middle_first_1 = int(len(first_name_1)/2)
middle_last_1 = int(len(last_name_2)/2)
middle_first_2 = int(len(first_name_1)/2)
middle_last_2 = int(len(last_name_2)/2)

first_mash_1_first_part = first_name_1[0:middle_first_1]
first_mash_1_second_part = first_name_1[middle_first_1:]
last_mash_1_first_part = last_name_1[0:middle_last_1]
last_mash_1_second_part = last_name_1[middle_last_1:]
first_mash_2_first_part = first_name_2[0:middle_first_2]
first_mash_2_second_part = first_name_2[middle_first_2:]
last_mash_2_first_part = last_name_2[0:middle_last_2]
last_mash_2_second_part = last_name_2[middle_last_2:]

new_name_1 = first_mash_1_first_part + first_mash_2_second_part + " " + last_mash_1_first_part + last_mash_2_second_part
new_name_2 = first_mash_2_first_part + first_mash_1_second_part + " " + last_mash_2_first_part + last_mash_1_second_part

print(new_name_1)
print(new_name_2)











