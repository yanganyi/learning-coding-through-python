
### notice the arrangement of the conditional ( if ) and the for loop

# lesson-61
temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)

# lesson-62
temps = [221, 234, 340, -9999, 230]
new_temp = [temp / 10 if temp != -9999 else 0 for temp in temps]
