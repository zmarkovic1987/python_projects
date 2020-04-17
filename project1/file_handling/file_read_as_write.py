"""
The Example for not using the file.close()
"""


with open('read_as.txt', 'w') as new_write:
    new_write.write('This is an example of with/as')
print()

with open('read_as.txt', 'r') as new_read:
    print(str(new_read.read()))


