"""Explicit Type Conversion"""

#variables declarations
NUM_STRING = "15" # number of type str
NUM_INTEGER = 12 # number of type int

print(f"Data type of '{NUM_STRING}' before type conversion: {type(NUM_STRING)}")

# explicit type conversion
NUM_STRING = int(NUM_STRING)

print(f"Data type of '{NUM_STRING}' after type conversion: {type(NUM_STRING)}")

NUM_SUM = NUM_INTEGER + NUM_STRING

print("Sum: ", NUM_SUM)
print(f"Data type of {NUM_SUM}: {type(NUM_SUM)}")

#END
