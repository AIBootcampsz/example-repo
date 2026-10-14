# Create variables for each activity time

# Time in minutes to swim
time_swim = int(input("Enter the time taken to swim (in minutes): "))
ts = time_swim  # Assign the input value to the variable ts

# Time in minutes to cycle
time_cycle = int(input("Enter the time taken to cycle (in minutes): "))
tc = time_cycle  # Assign the input value to the variable tc

# Time in minutes to run
time_run = int(input("Enter the time taken to run (in minutes): "))
tr = time_run  # Assign the input value to the variable tr

# Calculate the total time taken for all activities, and print the award based
# on the total time taken.
time_total = ts + tc + tr

if time_total >= 111:
    print("No award.")
elif time_total >= 106:
    print("Provincial scroll.")
elif time_total >= 101:
    print("Provincial half colours.")
else:
    print("Provincial colours.")
