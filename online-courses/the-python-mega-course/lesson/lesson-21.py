
monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures)

monday_temperatures.append(8.1)
monday_temperatures.append(8.7)
monday_temperatures.append(8.9)
monday_temperatures.append(8.8)
print(monday_temperatures)

print(monday_temperatures.index(8.8))
print(help(list.index))
print(monday_temperatures.index(8.8,2,7))

monday_temperatures.clear()
print(monday_temperatures)

print(help(list.remove))