
#Python Literals
#Python Numeric Literals
#Numeric Literals are immutable (unchangeable).
#Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.
#Type	Example	Remarks
#Decimal	5, 10, -68	Regular numbers.
#Binary	0b101, 0b11	Start with 0b.
#Octal	0o13	Start with 0o.
#Hexadecimal	0x13	Start with 0x.
#Floating-point Literal	10.5, 3.14	Containing floating decimal points.
#Complex Literal	6 + 9j	Numerals in the form a + bj, where a is real and b is imaginary part

#Python Boolean Literals
#There are two boolean literals: True and False.
result1 = True  
print(result1)

#String and Character Literals in Python
some_character = 'S'
print(some_character)


#Special Literal in Python
#Python contains one special literal None. We use it to specify a null variable. For example,
value = None
print(value)

## list literal
fruits = ["Mango","Grapes","Apples",1]
print(fruits) #prints array 
print(fruits[0]) #print first in order
print(fruits[1]) #print second  in order
print(fruits[2])#print third in order
print(fruits[3])#print third in order
print(fruits[2][1]) #print second charater in last value order

# tuple literal
numbers1 = 1, 2, 3,"Amit",  # whit or whithout bracket 
print(numbers1) #prints array 
print(numbers1[0]) #print first in order
print(numbers1[1]) #print second  in order
print(numbers1[2])#print third in order
print(numbers1[3][1]) #print second charater in last value order

# dictionary literal - comes in key and value pair 
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
print(alphabets) #prints array 
print(alphabets['a']) #print first in order - accessed by only key name 


#set literal - returns uiquer list 
vowels = {'a', 'e', 'i' , 'o', 'u','e','i'} 
print(vowels)