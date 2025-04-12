# Specify a variable type in python
# There may be time you want to explicitly specify a type of a variable
# That could be achieved using casting.
# Python is an OOP it is uses classes to define its data type even its own primitive type.
# It uses classes to define types

# Casting in python is therefore achieved using constructor functions such as
# int(), float(), str(), complex()

# int()
# int() - constructs an integer from integer literal, from float literal by removing the decimal parts
# from string literal by removing the quotes provided that it is an integer
age = "25"
height = 1.75
weight = "68.50"
print(f"Type of age[{age}], [{height}], and [{weight}] before conversion:\
      \n {type(age)}, {type(height)}, and {type(weight)}")
