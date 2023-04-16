numDays = int(input("Enter the number of days : "))
total = 0

for i in range(1, numDays+1):
    nextDay = int(input("Day " + str(i) + "'s high temperature : "))
    total += nextDay

avg = round(total/numDays, 2)

print("Average = " + str(avg))