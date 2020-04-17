"""
Reading a file -> read()
Reading line by line -> readline()
"""

my_file = open('firstfile.txt', 'r')

print(my_file.read())

my_file.close() # must close

print('*' * 20)

my_file_line = open('firstfile.txt', 'r')

# print(my_file_line.readline()) # reading first line
# print(my_file_line.readline()) # reading second line
# print(my_file_line.readline()) # reading third line

for item in my_file_line:
    print(str(item))

my_file_line.close()
