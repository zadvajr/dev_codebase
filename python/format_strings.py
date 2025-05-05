"""Python Format Strings"""
# As you may know now, you cannot combine or add a string and a number in python
# age = 37
# txt = "Hello my name is Daniel and I am" + age # This line will result in error
# print(txt)

# But with string format this is very much possible
# we can combine strings and numbers by making use of f-string and format() method

# f-strings
age = 28
txt = f"I am Daniel and I am {age} year old."
print(txt)

# format() method
name = "Daniel"
height = 2.5
txt = "{} is {} in height".format(name, height)
print(txt)

# end