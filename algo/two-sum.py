# write a function two_sum(list,sum) to find out if there are two numbers with different indices
# in the given list whose sum equals the given target.
# if found, return the indices of two numbers; if not found, return -1, -1

def list_generator(n):
    my_long_list = [1,5]
    for i in range(n):
        my_long_list.append(10)
    my_long_list.append(99)
    my_long_list.append(101)
    return my_long_list

# method 1: nested loops
# time complexity: O(n^2)
def two_sum_v0(list, sum):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == sum:
                return i, j
    return -1, -1

# method 2: fast searching using dictionary
# time complexity: O(n)
def two_sum_v1(list, sum):
    values_dict = {}
    for i in range(len(list)):
        if list[i] in values_dict:
            return values_dict[list[i]], i
        elif sum - list[i] not in values_dict:
            values_dict[sum - list[i]] = i
    return -1, -1


# method 3: fast searching using dictionary
# time complexity: O(n)
# only slight variation from method 2, what is the subtle diff here?!
def two_sum_v2(list, sum):
    values_dict = {}
    for i in range(len(list)):
        if list[i] in values_dict:
            return values_dict[list[i]], i
        else:
            values_dict[sum - list[i]] = i
    return -1, -1


# functional test
print("\n=== functional test ===\n")
print(two_sum_v1([1, 3, 5, 10, 20], 1))
print(two_sum_v1([1, 3, 5, 10, 20], 4)) 
print(two_sum_v1([1, 3, 5, 10, 20], 5)) 
print(two_sum_v1([1, 3, 5, 10, 20], 6)) 
print(two_sum_v1([1, 3, 5, 10, 20], 7)) 
print(two_sum_v1([1, 3, 5, 10, 20], 23)) 

# stress test
print("\n=== stress test ===\n")
print(two_sum_v1(list_generator(10), 200)) 
print(two_sum_v1(list_generator(1000), 200)) 
print(two_sum_v1(list_generator(10000), 200)) 
print(two_sum_v1(list_generator(100000), 200)) 
print(two_sum_v1(list_generator(1000000), 200)) 
print(two_sum_v1(list_generator(10000000), 200)) 

# note the result difference between method 2 & 3
print(two_sum_v1([1, 3, 3, 5, 10, 20], 8)) 
print(two_sum_v2([1, 3, 3, 5, 10, 20], 8)) 

