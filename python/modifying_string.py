"""Modifying Strings in Python"""
# Python has set of built-in methods that you can apply on strings.

# Examples
# You can convert strings to upper case using the method upper()
# The upper() method returns the string in uppercase it does not change the original string
txt = "Hello I am Daniel Zadva Jnr"
print(txt) # Prints: Hello I am Daniel Zadva Jnr
print(txt.upper()) # Prints: HELLO I AM DANIEL ZADVA JNR
print(txt) # Still prints: Hello I am Daniel Zadva Jnr

print()
# Lower case: lower() method returns the string all in lowercase
# It also does not change the original string but rather returns a new string
name = "DANIEL ZADVA JNR"
print("Before conversion: ", name)
print("After Conversion: ", name.lower())
print("Original Text: ", name)

