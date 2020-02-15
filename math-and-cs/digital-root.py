# Requirements:
# input: a positive integer
# output: its digital root

def digital_root_hmmmm(num):
    return num % 9

def digital_root_slowest(num):
    while True:
        if num < 9:
            return num
        else:
            num = num - 9

# 1 level loop with recursion
def digital_root_faster(num):
    digital_sum = 0
    while num > 0:
        processing_num = num % 10
        num = int(num - processing_num / 10)
        digital_sum = digital_sum + processing_num

    if digital_sum < 9:
        return digital_sum
    elif digital_sum == 9:
        return 0
    else:
        return digital_root_faster(digital_sum)

# 2 level loops
def digital_root_faster_v2(num):
    while True:
        if num == 9:
            return 0
        elif num < 9:
            return num
        else:
            temp_num = num
            digital_sum = 0
            # inner loop takes out every digit and sum it up
            while temp_num > 0:
                processing_num = temp_num % 10
                digital_sum = digital_sum + processing_num
                temp_num = int((temp_num - processing_num) / 10)
            # overwrite num to prepare for the next iteration, if necessary
            num = digital_sum


print(digital_root_faster(3))    # 3
print(digital_root_faster(9))    # 0
print(digital_root_faster(22))   # 4
print(digital_root_faster(27))   # 0
print(digital_root_faster(28))   # 1
print(digital_root_faster(100))  # 1

print(digital_root_faster(57619351234))  # 1

