#In Python, if you try to add a number and a string, you will generate an error.
#for example
AGE = 36
GREETING = "Welcome, you are "
print(GREETING + AGE) #this will generate an errror TypeError

#To overcome the error, convert any variable types to match the other.
# I will convert age into str and join them with the + operator
print(GREETING + str(AGE)) #this won't generate an error. Comment line 5 to run this.

#end
