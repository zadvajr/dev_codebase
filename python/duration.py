hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
total_mins = dura + mins
add_hour = total_mins // 60
end_hour = hour + add_hour
end_mins = (total_mins % 60)

print(end_hour)
print(end_mins)
print(add_hour)