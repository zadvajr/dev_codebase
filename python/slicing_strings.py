"""Python String Slicing"""
# You can return a range of characters from a string by using a slice syntax
# You achieve this by specifying the start index and the end index
# Separated by colon to return some part of the string
# Example: To get characters from position 2 to 5 (not included)
b = "Hello World"
print(b[2:5]) # Prints llo
# Note: The first character has an index 0

# Slice from start
# By ommiting the start index, the slice will begin at index 0
print(b[:5]) # Prints Hello

# Slice to the end
# By leaving out the end index, it slices up to the end
print(b[6:]) # Prints World

