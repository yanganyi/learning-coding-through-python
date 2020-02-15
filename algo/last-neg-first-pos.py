### Requirement
# write a function named find_two_indices, taking an array as input, print the index of the last negative number and the index of the first positive number
# you may assume:
# 1. the array is fully sorted
# 2. all values are integers which fall within [-1000,1000] range
# sample input: [-10,-5,-1,1,3,5,100]
# sample printout: 2 3

# 25 lines, 1 for 7 if
# main changes:
# - first working version
def find_two_indices_v1(arr):
    indexSmallPosNum = 0
    smallPosNum = 1000
    indexBigNegNum = 0
    bigNegNum = -1000
    if len(arr)==0 :
        print(-1, -1)
        return
    for i in range(len(arr)):
        if arr[i] > 0:
            smallPosNum = arr[i]
            indexSmallPosNum = i
            break
        if arr[i] < 0:
            if i == 0:
                bigNegNum = arr[i]
                indexBigNegNum = i
            elif arr[i] >= bigNegNum:
                bigNegNum = arr[i]
                indexBigNegNum = i
    if arr[len(arr) - 1] <= 0:
        indexSmallPosNum = -1
    if arr[0] >=0:
        indexBigNegNum = -1
    print(indexBigNegNum, indexSmallPosNum)

# 29 lines, 1 for 9 if
# main changes:
# - add two circuit breakers
def find_two_indices_v2(arr):
    indexSmallPosNum = 0
    smallPosNum = 1000
    indexBigNegNum = 0
    bigNegNum = -1000
    if len(arr)==0 :
        print(-1, -1)
        return
    if arr[len(arr) - 1] <= 0:
        indexSmallPosNum = -1
        if arr[len(arr) - 1] < 0:
            indexBigNegNum = len(arr) - 1
            print(indexBigNegNum, indexSmallPosNum)
            return
    if arr[0] >= 0:
        indexBigNegNum = -1
        if arr[0] > 0:
            indexSmallPosNum = 0
            print(indexBigNegNum, indexSmallPosNum)
            return
    for i in range(len(arr)):
        if arr[i] > 0:
            smallPosNum = arr[i]
            indexSmallPosNum = i
            break
        if arr[i] < 0:
            if i == 0:
                bigNegNum = arr[i]
                indexBigNegNum = i
            elif arr[i] >= bigNegNum:
                bigNegNum = arr[i]
                indexBigNegNum = i
    print(indexBigNegNum, indexSmallPosNum)

# 18 lines, 1 for 4 if
# main changes:
# - assume -1 for both indices unless they are actually found
def find_two_indices_v3(arr):
    indexSmallPosNum = -1
    smallPosNum = 1000
    indexBigNegNum = -1
    bigNegNum = -1000
    for i in range(len(arr)):
        if arr[i] > 0:
            smallPosNum = arr[i]
            indexSmallPosNum = i
            break
        if arr[i] < 0:
            if i == 0:
                bigNegNum = arr[i]
                indexBigNegNum = i
            elif arr[i] >= bigNegNum:
                bigNegNum = arr[i]
                indexBigNegNum = i
    print(indexBigNegNum, indexSmallPosNum)

# 10 lines, 1 for 2 if
# main changes:
# - removed unused variables definitions
# - always update if negative number found
def find_two_indices(arr):
    indexSmallPosNum = -1
    indexBigNegNum = -1
    for i in range(len(arr)):
        if arr[i] > 0:
            indexSmallPosNum = i
            break
        if arr[i] < 0:
            indexBigNegNum = i
    print(indexBigNegNum, indexSmallPosNum)


find_two_indices([-10,-5,-1,0,1,3,5,100]) # 2 4
find_two_indices([-10,-5,-1,1,3,5,100])   # 2 3
find_two_indices([-1000,-100,-10,-1])     # 3 -1
find_two_indices([1,10,100,1000])         # -1 0
find_two_indices([0,0,0,0,0])             # -1 -1
find_two_indices([])                      # -1 -1

find_two_indices([-10,-5,-1,-1,-1,0,0,1,1,1,3,5,100]) # 4 7
find_two_indices([-10,-5,-1,0,0,1,3,5,100])           # 2 5
find_two_indices([0,0,1,3,5,100])                     # -1 2
find_two_indices([-10,-5,-1,0,0])                     # 2 -1
find_two_indices([-5,-5,5,5])                         # 1 2
find_two_indices([-5])                                # 0 -1
find_two_indices([5])                                 # -1 0

