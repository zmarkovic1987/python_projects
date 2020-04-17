"""
File manipulating:
'w' -> Write-Only Mode
'r' -> Read-Only Mode
'r+' -> Read and Write Mode
'a' -> Append mode
"""

my_list = [1, 2, 3]

my_file = open('firstfile.txt', 'w') # open file or create new if not existing - 'w' means tha we want to write

my_file.write('Hello' + '\n')

for item in my_list:
    my_file.write(str(item) + '\n') # n is for new row

my_file.close() #close file after manipulating