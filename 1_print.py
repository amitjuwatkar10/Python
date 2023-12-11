#Print statement
print("Hello, world!")

'''
  object - value(s) to be printed
sep (optional) - allows us to separate multiple objects inside print().
end (optional) - allows us to add add specific values like new line "\n", tab "\t"
file (optional) - where the values are printed. It's default value is sys.stdout (screen)
flush (optional) - boolean specifying if the output is flushed or buffered. Default: False
'''

#Example 2: Python print() with end Parameter
# print with end whitespace
print('Good Morning!', end= '. ')

print('It is rainy today')

#Example 3: Python print() with sep parameter

print('New Year', 2023, 'See you soon!', sep= '. ')

#Example: Print Concatenated Strings

print('Programiz is ' + 'awesome.')

'''
Output formatting
Sometimes we would like to format our output to make it look attractive. This can be done by using the str.format() method. For example,

'''

x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))