#Example 5: Membership operators in Python


'''
In Python, in and not in are the membership operators. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

In a dictionary we can only test for presence of key, not the value.

Operator	Meaning	Example
in	True if value/variable is found in the sequence	5 in x
not in	True if value/variable is not found in the sequence	5 not in x

'''

x = 'Hello world'
y = {1:'a', 2:'b'}

#------------------------------------------#

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True

# check if 'hello' is present in x string
print('Hello' not in x)  # prints False

# check if 'hello' is present in x string
print('Hello' in x)  # prints True

#------------------------------------------#

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print('a' in y)  # prints False