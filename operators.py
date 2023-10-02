# Page 2

price_of_pineapple = 25.50
price_of_apple = 18.60
price_of_tomato = 7.80


quantity_of_pineapple = 5
quantity_of_apple = 3
quantity_of_tomato = 2


total_cost = (price_of_pineapple * quantity_of_pineapple)  
+ (price_of_apple * quantity_of_apple)
+ (price_of_tomato * quantity_of_tomato)


print("Total cost of purchase:", total_cost)


# Page 3

a1 = 3
b1 = 5
print("Here is your required sum of a1 and b1",a1+b1)  # Addition Operator
print("Here is your required difference of a1 and b1",a1-b1)  # Subtraction Operator
print("Here is your required product of a1 and b1",a1*b1)  # Multiplication Operator
print("Here is your required division of a1 and b1",a1/b1) # Division Operator
print("a1 to the power b1",a1**b1)  # Exponential Operator
print("Remainder when b1 is divided by a1 is",b1%a1)  # Remainder/Modulus Operator
# floor division operator
print("floor division operator",b1//a1)
'''after division it returns the largest integer
that is less than or equal to the quotient'''

# Page 4

'''Equality Operator returns True if both operands are equal,
otherwise returns False.'''
print(5==5)
print('sprintgrad'=='sprintgrad')




'''Inequality returns True if the operands are not equal otherwise,
returns False.'''
print(5!='5')
print(2!=2)


# Page 5

'''Greater than returns True if the left operand is greater than the right operand,
otherwise returns False.'''
print(9.63>9.6)
print(1>2)


'''Less than returns True if the left operand is less than the right operand,
otherwise returns False.'''
print(10<7)
print(12<15)

# Page 6



'''Greater Than or Equal To returns True if the left operand is
 greater than or equal to the right operand otherwise, returns False.'''
print(20>=20)
print(35>=55)


'''Less Than or Equal To returns True if the left operand is less than or 
equal to the right operand otherwise, returns False.'''
print(10<=3)
print(77<=100)


# Page 7


# LOGICAL OPERATORS
x = 25
y = 15

# Using logical AND and logical OR operators
result1 = (x > 15) and (y < 80)  # True and True => True
result2 = (x > 15) or (y < 3)  # True or False => True
result3 = not (x == y)         # not False => True

print(result1)
print(result2)
print(result3)


# Page 8

# IDENTITY OPERATORS
x = [1, 2, 3]   # x is a list
y = x
# y = x is used to create a new reference to the same object that x is referring to.

print(y is x)     # Output: True
print(y is not x)  # Output: False


# Page 9


# ASSIGNMENT OPERATORS

x = 10 
# Assigns the value on the right-hand side to the variable on the left-hand side.
x += 5 
''' Adds the value on the right-hand side to the variable 
on the left-hand side and assigns the result to the variable.'''
x -= 3
'''Subtracts the value on the right-hand side 
from the variable on the left-hand side and assigns the result to the variable.'''
x *= 2
'''Multiplies the variable on the left-hand side 
by the value on the right-hand side and assigns the result to the variable.'''
x /= 4
'''Divides the variable on the left-hand side by the value on the 
right-hand side and assigns the result to the variable.'''
x %= 3
'''Performs the modulus operation on the variable on the left-hand side with the 
value on the right-hand side and assigns the result to the variable.'''
x **= 2
'''Raises the variable on the left-hand side to the power of the 
value on the right-hand side and assigns the result to the variable.'''
x //= 5
'''Performs the floor division operation on the variable on the left-hand side 
with the value on the right-hand side and assigns the result to the variable.'''

print(x)



# Page 10

# MEMBERSHIP OPERATORS

# Using in operator
fruits = ['apple', 'banana', 'orange', 'grape']  # fruits is a list
print('apple' in fruits)  
print('kiwi' in fruits)   



# Using in operator with a string
text = "Hello, World!"
print('Hello' in text)  
print('Python' in text)


# Page 11

# BITWISE OPERATOR

# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
a = 3
b = 2
print(a & b)

'''
3 = 0000000000000011
2 = 0000000000000010
--------------------
2 = 0000000000000010

'''

# The | operator compares each bit and set it to 1 if 1 or both is 1 , otherwise it is set to be 0

a = 4
b = 5
print(a | b)


'''
4 = 0000000000000100
5 = 0000000000000101
----------------------
5 = 0000000000000101
'''


# Page 12

a = 6
b = 3
print(a ^ b)

'''
The ^ operator compares each bit and set it to 1 if only one is 1, 
otherwise (if both are 1 or both are 0) it is set to 0
6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
'''



a = 3
print(~3)
'''
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
 --------------------
-4 = 1111111111111100
'''



# Page 13

a = 3
b = 2
print(a << b)

'''
The << operator inserts the specified number of 0's (in this case 2) 
from the right and let the same amount of leftmost bits fall off
If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100
'''



a = 4
b = 2
print(a >> b)

'''
The >> operator moves each bit the specified number of times to the right. 
Empty holes at the left are filled with 0's.
If you move each bit 2 times to the right, 4 becomes 1
4 = 0000000000000100
becomes
1 = 0000000000000001
'''


















































































# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# a = 3
# b = 2
# print(a & b)

'''
3 = 0000000000000011
2 = 0000000000000010
--------------------
2 = 0000000000000010

'''


"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""












































































