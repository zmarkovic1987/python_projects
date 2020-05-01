"""
napravi string reci
napravi  string slova
napravi praznu listu
podeli string u reci
napravi listu reci
u for petlji za svako slovo u reci uporedi sa datim slovima
    ako su sva slova iz reci u datim slovima, dodaj rec u listu
"""
# words = "art\nhue\nink\noil\npen\nwax\nclay\ndraw\nfilm"
words = """art
hue
ink
oil
pen
wax
clay
draw
film"""
matched_words = []
names_list = []
start = 0
names = ''
delimiter = "\n"

for e in words:
    if e != delimiter:
        names += e
    else:
        names_list.append(names)
        names = ''
last_name = words[words.rfind(delimiter) + 1:]
names_list.append(last_name)
print(names_list)

given_letters = "fhijklmnop"
for name in names_list:
    new_name = ''
    for e in name:
        if e in given_letters:
            new_name += e
            # if len(new_name) == len(name):
            if new_name in names_list:
                matched_words.append(name)
                new_name = ''

print(matched_words)


# number_to_guess = '5'
# question = 'yes'
#
# while question == "yes" or question == "y":
#     question = input('Do you wanna play a game?')
#     if question != 'yes' and question != 'y':
#         print('You are boring')
#         break
#     else:
#         guess = input('Guess a number from 1 to 10')
#     while guess != number_to_guess:
#         guess = input('Guess again')
#     if guess == number_to_guess:
#         print('you nailed it')
#     continue

# # for ch in "Python is fun so far!":
# #     print('the character is ', ch)
# even = []
# by_six = []
# for e in range(0,100):
#
#     if e % 2 == 0:
#         # print(e)
#         even.append(e)
#     if e % 6 == 0:
#         by_six.append(e)
#
# print("Even number: " + str(len(even)))
# print("Divisible by 6: " + str(len(by_six)))


# secret = "code"
# guess = input('Guess the word: ')
# counter = 1
#
# while secret != guess:
#     print('You tried to guess ' + str(counter) + ' times.')
#     guess = input('Guess again: ')
#     counter += 1
#     if counter == 3:
#         print("No more guesses")
#         break
# if secret == guess:
#     print('You nailed it')
