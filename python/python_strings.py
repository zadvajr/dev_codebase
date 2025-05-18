"""Python Strings"""
# Strings in python are either surrounded by single quotation marks or
# double quotation marks. "hello" and 'hello' are the same in python.
# You can display a string literal with the print() function

#Example
print("Hello")
print('Hello')

#Quotes inside a string
# You can use a quote inside a string as long as it did not match the one surrounding it.
# Example
print("It's alright!")
print("He is called 'Zadva'")
print('He loves "Reading"')

#Assign string to a variable
# Assigning a string to a variable is done with the variable name
# followed by an equal sign and the string literal
# Example
a = "Hello"
print(a)

# Multiline string
# You can assign multiline string to a variable by using triple quotes
# Example
a = """This is a multiline string assigned to a variable
it is going to appear as it is in the code."""
print(a)

# You can also use three single quotes
# Note, line breaks are inserted in the same position they appear in the code.

# Looping through a string
# Since strings are arrays we can loop through them with a for loop
# Example: loop through the word 'banana'
for x in "banana":
    print(x)

# String leng
# To get the length of a string we can use the len() function
a = "Hello world"
print(len(a))

# Check string
# To check if a certain character or string exist in a particular string
# we make use of in keyword
txt = "The best things in life are free"
print("free" in txt)

if "free" in txt:
    print("Yes free is in the txt")
#end
