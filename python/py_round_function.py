# Python round() function
# The round() function returns a floating point number that is a rounded version
# of the specified number with the speciifed number of decimals.
# the default number of decimal is 0 - meaning that the function will return the nearest integer.

# syntax - round(number, digits)
# number - is a required argument, it specifies the number to be rounded
# digits - is an optional argument - it defaults to 0, it specifies the number of decimal digits to round the number to

#Example
num = 5.76543
print("Rounded to Nearest Integer: ", round(num)) # No second argument specified so the function will return the nearest integer which will be 6

print("Rounded to 2 Decimal Places: ", round(num, 2))