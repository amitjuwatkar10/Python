
'''
In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.

There are two types of type conversion in Python.

Implicit Conversion - automatic type conversion
Explicit Conversion - manual type conversion

Python Implicit Type Conversion
In certain situations, Python automatically converts one data type to another. This is known as implicit type conversion.
'''
integer_number = 123
float_number = 1.23

#Example 1: Converting integer to float
new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

'''
Explicit Type Conversion
In Explicit Type Conversion, users convert the data type of an object to required data type.

We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.
'''

num_string = '12'
num_integer = 23


print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)


print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))


'''

Key Points to Remember
Type Conversion is the conversion of an object from one data type to another data type.
Implicit Type Conversion is automatically performed by the Python interpreter.
Python avoids the loss of data in Implicit Type Conversion.
Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
In Type Casting, loss of data may occur as we enforce the object to a specific data type.

'''