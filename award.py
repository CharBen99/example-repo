time_swimming = int(input("Enter the time (in minutes) you completed the swimming challenge : "))
time_cycling = int(input("Enter the time (in minutes) you completed the cycling challenge : "))
time_running = int(input("Enter the time (in minutes) you completed the running challenge : "))
total_time = time_swimming + time_cycling + time_running
print(total_time)
if total_time >= 0 and total_time <= 100 :
    print("Award : Provincial colours ")
elif total_time >= 101 and total_time <= 105 :
    print("Award : Provincial half colours ")
elif total_time >= 106 and total_time <= 110 :
    print("Award : Provincial scroll ")
else:
    print("No award ")


