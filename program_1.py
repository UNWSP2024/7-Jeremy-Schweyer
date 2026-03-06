rainfall = []

for i in range(1,13):
    rainfal = int(input("Enter the rainfall for every month: "))
    rainfall.append(rainfal)

total = sum(rainfall)
average = total/12
print("The average rainfall is: ", average)
print("The total rainfall is: ", total)
print("The Maximum rainfall is: ", max(rainfall))
print("The Minimum rainfall is: ", min(rainfall))
