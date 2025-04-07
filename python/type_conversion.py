# Type Conversion
# You can convert from one type to another with int(), float() and complex() methods

#Example
x = 1 # int
y = 2.8 # float
z = 1j # comlex

# Type before conversion
print(f"Type of {x} before conversion is: {type(x)}")
print(f"Type of {y} before conversion is: {type(y)}")
print(f"Type of {z} before conversion is: {type(z)}")

print()
print()

# Conversion
# Converting int to float
a = float(x) # x is an integer and this converts it to float and saved in variable a

# Converting float to int
b = int(y) # y is a floating point number, and this line converts it to int and saves it in variable b, this will result in truncating the number 2.8 to 2

# Converting from int to complex
c = complex(x) # x  is an integer, and this line converts it to complex number type

# Converting from float to complex
d = complex(y) # y is a floating point number, and this line converts it to a complex type

# Conversion from complex to any type is not allowed, as complex type cannot be converted into any other type.

# Conversion from str to int
age = "32"
int_age = int(age) # converts a string type "32" to integer 32

# Conversion from int to str
str_age = str(int_age) # converts int_age back to str

# After Conversion
print(f"Type of {x} after conversion is: {a}")
print(f"Type of {y} after conversion is: {b}")
print(f"Type of {z} after conversion is: {c}")

# Conversion from complex to any other type is not allowed.
#end
