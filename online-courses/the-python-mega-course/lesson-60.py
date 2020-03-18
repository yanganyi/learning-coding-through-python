
temps = [221, 234, 340, 230]

### 2 methods

# method 1
new_temps = []
for temp in temps:
    new_temp = temp / 10
    new_temps.append(new_temp)
print(new_temps)

#method 2
temperature = [temp / 10 for temp in temps]
print(temperature)