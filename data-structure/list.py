
# basic functions of list

num_list = [1,2,9,8,5]
print(num_list)

# list initialization
v = [1] * 5
for i in range(len(v)):
    print(i,v[i])

# range and enumeration
for i in range(len(num_list)):
    print(str(i) + "  "+ str(num_list[i]))

for i,v in enumerate(num_list):
    print(str(i) + "  "+ str(v))

# take a slice
print(num_list[1:3])
print(num_list[2:])
print(num_list[:3])
print(num_list[-1])


# manipulations

num_list.append(10)
print(num_list)

num_list.insert(1,15)
print(num_list)
num_list.insert(1,16)
print(num_list)

print(num_list.index(16))
print(num_list.index(15))

print(20 in num_list)

num_list.pop(5)     # remove the value at the given index
print(num_list)

num_list.remove(5)  # remove the given value, a slow operation
print(num_list)

