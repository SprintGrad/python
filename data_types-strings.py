# Chat application

# Get user names
friend1 = input("Friend1's name: ")
friend2 = input("Friend2's name: ")


print(f"Let us start the conversation between {friend1} and {friend2}")

# Loop for chat conversation
while True:
    
    friend1_message = input(f"\n{friend1}: ")
    if "bye" in friend1_message.lower():
        print("\nChat session ended.")
        break
    

    
    friend2_message = input(f"\n{friend2}: ")
    if "bye" in friend2_message.lower():
        print("\nChat session ended.")
        break




# Page 2

# Using single quotes
s1 = 'Hello, World!'
print(s1)
# Using double quotes
s2 = "Python is awesome"
print(s2)


# Page 3

# Using empty quotes.
strr1 = ""
# Using the str() constructor.
strr2 = str()

'''Both of these approaches create an empty string object 
named empty_str with no characters.'''




s = "Hello World"
print(s[0])
print(s[6])


# Page 4

s = "Hello, World!"

for char in s:
    print(char)


'''Combining two or more strings together using the + 
operator or the str.join() method.'''
s1 = "Sprint"
s2 = "Grad"
result = s1 + s2
print(result)

words = ["Sprint", 'Grad']
result = "".join(words)
print(result)


# Page 5

# You can extract substrings from a string using slicing.
# Specify the start index and the end index, separated 
# by a colon, to return a part of the string.'''
s = "Hello, World!"
substring1 = s[0:5] # Get the characters from position 0 to 5(not included)
substring2 = s[:4]  # Get the characters from the start to position 5 (not included)
substring3 = s[2:]  # Get the characters from position 2, and all the way to the end

# '''Get the characters from 'o' in "World!"(position -5)
# to but not included "d" in "World!"(position -2)'''
substring4 = s[-5:-2]

# Extracting a substring with a step size of 2
substring5 = s[0:5:2]

print("Characters from position 0 to 5(not included) :",substring1)
print("Characters from the start to position 5 (not included) :",substring2)
print("Characters from position 2, and all the way to the end :",substring3)
print("Characters from position -5 to -2 (not included) :",substring4)
print("Characters from position 0 to 2 (exclusive) with a step size of 2 :",substring5)


# Page 6

name = "John"
age = 25
outp = "My name is {} and I am {} years old.".format(name,age)
print(outp)


name = "John"
age = 25
outp = f"My name is {name} and I am {age} years old."
print(outp)

# Page 7

ans = "Rohan is the new "leader" now."
print(ans)

ans = "Rohan is the new \"leader\" now."
print(ans)

# Page 8

# ''' The newline ('\n') escape character represents a line break in a string.'''
print("NEWLINE")
inp1 = "Hello\nWorld!"
print(inp1)

# ''' The tab ('\t') escape character represents a horizontal tab.'''
print("TAB")
inp2 = "Name:\tJohn\nAge:\t25"
print(inp2)

# ''' The backslash ('\\') escape character itself can be used to include a 
# literal backslash within a string.'''
print("BACKSLASH")
path = "C:\\Users\\John\\Documents"
print(path)

# '''The single quote ('\') and double quote('\"') escape characters are used to 
# include literal single or double quotes within a string, respectively.'''
print("SINGLE AND DOUBLE QUOTE")
inp3_1 = 'I\'m happy'
inp3_2 = "She said, \"Hello!\""
print(inp3_1)
print(inp3_2)

# '''The backspace ('\b') escape character is when encountered within a string, it moves 
# the cursor back one position, effectively erasing the character before the backspace.'''
print("BACKSPACE")
outp4 = "Hello\bWorld!"
print(outp4)


# Page 9

s = "Hello, World!"
ans = len(s)
print(ans)
''' You could have also written print(len(ans)) 
instead of line 2 and 3 '''

s1 = "John_Wick"
ans1 = s1 * 3
print(ans1)

'''The resulting string ans1 is then printed, 
showing "John_WickJohn_WickJohn_Wick".'''

s2 = "abcd"
ans2 = s2 * 0
print(ans2)

'''In this case, since the multiplier is zero, 
the resulting string ans2 is empty.'''


# page 10

s1 = "hey , let's meet"
print(s1.upper())

s2 = "ARE YOU THERE?"
print(s2.lower())

''' You can store the output of a 
string method in a variable and then 
print the value of that variable.'''

'''s1 = "hey , let's meet"
upper_ = s1.upper()
print(upper_)'''

#This will also give the same output.



s = "here we go for the first time"
print(s.capitalize())

# Page 11

s = "hello, Hello, Hello"
print(s.count("Hello")) #counts "Hello" substring in s
print(s.count("1"))     #counts "1" character in s


s = "Hello, World!"
print(s.startswith("hel"))
print(s.endswith("World"))


# Page 12

s = "Hello, World!"
print(s.replace("Hello","Hi"))


txt = "hello, my name is John, I am 25 years old"
x = print(txt.split(","))

'''The split() method is used on the txt 
string to split it into multiple substrings wherever a comma
(",") is found.'''




txt = "pineapple#apple#banana#orange"
print(txt.split('#',1))
'''
'#'specifies that the delimiter to split the string is the '#' character.
1 limits the split to only one occurrence of the delimiter.
'''

# Page 13

s = "     Hello people!      "
print(s.strip())
print(s.lstrip())
print(s.rstrip())


txt = "hello people!"
x = txt.islower()
print(x)


txt1 = "23244"
txt2 = "34r46"
x1 = txt1.isdigit()
x2 = txt2.isdigit()
print(x1)
print(x2)


# Page 14


strng = "Welcome to the world of python."
x = strng.find("world")
print(x)
