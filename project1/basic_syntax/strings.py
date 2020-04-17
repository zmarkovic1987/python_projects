"""
Strings are Sequence od characters
Contains a-z, 0-9, @
"""

a = 'This is a simple string'
b = "using double quotes"
print(a)
print(b)

# Accessing characters in  a string
first = 'nyc'[2]
city = 'sfo'
print(first)

ft = city[0]
print(ft)

"""
STRING METHODS
len() - length of a string
lower() - lowercase
upper() - uppercase
str() - convert to string
"""

stri = 'This Is a Mixed Case'
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + str(2))


"""
STRING METHODS
"""

# Replace Method
a = '1abc2abc3abc4abc'
print(a.replace('abc', 'ABC', 2))
# replace first two occurencies

# Sub-strings
# Starting index is inclusive - it starts with this
# Ending index is exclusive - it stops at this (and do not include it) - 1-6 = 1,2,3,4,5
# Step means which step in a string. If you put 2 it will print every 2nd.
sub = a[1:6]
step2 = a[1:6:2]
comb = a[1:len(a):3]
print('***************')
print(sub)
print(step2)
print(len(a))
print(comb)



