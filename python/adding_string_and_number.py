#In python if you try to add a number and a string you will generate an error.
#for example
AGE = 36
GREETING = "Welcome, you are "
print(GREETING + AGE) #this will generate an errror TypeError

#To overcome the error, convert any of the variable type to match the other.
# in this case I will convert age into str and join them with + operator
print(GREETING + str(AGE)) #this wont generate an erro. comment line 5 to run this.
