"""
1. not
2. and
3. or
"""

bool_output = True or not False and False
# This is how you break it down
# 1. not False -> True
# 2. True and False -> False
# 3. True or False -> True
print(bool_output)

bool_output_2 = 10 == 10 or not 10 > 10 and 10 > 10
print(bool_output_2)

bool_output_3 = (10 == 10 or not 10 > 10) and 10 > 10
print(bool_output_3)


