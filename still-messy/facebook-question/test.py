
# functions that i learn in this challenge
# 1. max(someList) returns the max number in the list
# 2. someList.index(anElement) returns the index of the given number in the list
#    someList = [3,6,8,1],  someList.index(max(someList)) --> 2

input = [6,1,7,2]

# simple case: 6172

# thought process / algorithm:
# pick the max number
# if the max number is the first number:
#    do nothing
# else 
#     swap max with the first number

bigNo = max(input)

print (bigNo)

bigNoIndex = input.index(bigNo)
print(bigNoIndex)

no1 = input[0]
print(no1)
if bigNo > no1:
    tempBigNo = bigNo
    bigNo = no1
    no1 = tempBigNo
    print(bigNo,no1)
    print(input)



# testcases

# case 1: 7162
# max = 7
# no swap needed

# case 2: 6172
# max = 7
# swap 6 with 7 => 7162

# case 3: 6577
# -> 7567     X
# -> 7576     O