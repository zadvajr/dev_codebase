x = float(input("Enter value for x: "))

# Write your code here.
c = x + (1 / x)
y = 1 / ((x + (1 / (x + (1 / c)))))

print("y =", y)
