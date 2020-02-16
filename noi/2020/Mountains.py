import random
from datetime import datetime

def mountains_v1():
    cases = 0
    number = int(input())
    list = input().split()
    nums = []

    for i in range(number):
        nums.append(int(list[i]))

    for j in range(number):
        before = 0
        after = 0
        if 0 < j < (number-1):
            for k in range(j):
                if nums[j-k-1] < nums[j]:
                    before += 1
            for l in range(number - j - 1):
                if nums[j+l+1] < nums[j]:
                    after += 1
            increment = before * after
            # print("i am at ", j, increment)
            cases += increment

    print(cases)


# add with some optimizations on top of v1
# which did not earn additional marks in the contest
def mountains_v2(nums):

    cases = 0
    data_size = len(nums)

    before_min, before_max = prepare_before(nums)
    after_min, after_max = prepare_after(nums)
    for j in range(1, data_size - 1):
        before = 0
        after = 0

        if nums[j] < before_min[j]:
            continue

        if nums[j] < after_min[j]:
            continue

        if nums[j] > before_max[j]:
            before = j
        else:
            for k in range(j):
                if nums[j - k - 1] < nums[j]:
                    before += 1

        if nums[j] > after_max[j]:
            after = data_size - j - 1
        else:
            for l in range(data_size - j - 1):
                if nums[j + l + 1] < nums[j]:
                    after += 1

        increment = before * after
        # print("i am at ", j, increment)
        cases += increment
    return cases


def prepare_before(nums):
    data_size = len(nums)
    before_max = [-1]
    before_min = [10**18+1]
    for i in range(data_size - 1):
        if nums[i] > before_max[i]:
            before_max.append(nums[i])
        else:
            before_max.append(before_max[i])
        if nums[i] < before_min[i]:
            before_min.append(nums[i])
        else:
            before_min.append(before_min[i])
    # print("before min",before_min)
    # print("before max",before_max)
    return before_min, before_max


def prepare_after(nums):
    data_size = len(nums)
    after_max = [-1]
    after_min = [10**18+1]
    for i in range(data_size-1,0,-1):
        if nums[i] > after_max[0]:
            after_max.insert(0,nums[i])
        else:
            after_max.insert(0,after_max[0])
        if nums[i] < after_min[0]:
            after_min.insert(0,nums[i])
        else:
            after_min.insert(0,after_min[0])
    # print("after min",after_min)
    # print("after max",after_max)
    return after_min,after_max


# ===== entry methods =====

def manual_testcases():

    data_size = int(input())
    raw_data = input().split()
    nums = []
    for i in range(data_size):
        nums.append(int(raw_data[i]))

    cases = mountains_v2(nums)

    print(cases)


def automated_testcases():
    timed_mountains(1000, 100)
    timed_mountains(2000, 100)
    timed_mountains(3000, 100)
    # timed_mountains(4000, 100)
    # timed_mountains(5000, 100)
    # timed_mountains(10 ** 4, 100)

def timed_mountains(n, k):
    nums = auto_generate_mountains(n, k)
    a = datetime.now()
    cases = mountains_v2(nums)
    b = datetime.now()
    time_taken = b - a
    print("size:",n,"time:",time_taken.seconds)

def auto_generate_mountains(n, k):
    mountain = []
    for i in range(n):
        a = random.randint(1,k)
        mountain.append(a)
    return mountain


automated_testcases()
# timed_mountains(100,10)
# manual_testcases()
