#In python if you try to add a number and a string you will generate an error.
#for example
age = 36
greeting = "Welcome, you are "
print(greeting + age) #this will generate an errror TypeError

#To overcome the error, convert any of the variable type to match the other.
# in this case I will convert age into str and join them with + operator
print(greeting + str(age)) #this wont generate an erro. comment line 5 to run this.