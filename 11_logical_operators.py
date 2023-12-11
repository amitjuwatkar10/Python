'''
Python Logical Operators
Logical operators are used to check whether an expression is True or False. They are used in decision-making. For example,

Operator	Example	Meaning
and	a and b	Logical AND:

					True only if both the operands are True
or	a or b	Logical OR:

					True if at least one of the operands is True
not	not a	Logical NOT:

					True if the operand is False and vice-versa.
     
     
'''

a = 5
b = 6

print((a > 2) and (b >= 6))    # True

# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False