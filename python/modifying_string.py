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

print()
# Remove whitespace
# whitespace is the space before and/or after the actual text
# and most likely you may want to remove these spaces
# the strip() method removes whitespaces at the begining or end of text
a = "   Hello I have space before and after       "
print("Text before striping: ", a)
print("Text Length befor strip: ", len(a))
print("Text after striping: ", a.strip())
print("Text length after strip: ", len(a.strip()))

print()


