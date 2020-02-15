
### Requirement
# write a function, taking an list as input, print the index of the biggest number as well as its value
# it is safe to assume that the input numbers fall in the range of [-10k,10k]
# in case the list is empty, print "no such number found"
# in case the list is not an integer list, print "no integer list found"
def biggestNumberInList(numbers):
    biggestNumInList = -10001
    indexOfBiggestNumInList = 0

    if len(numbers)==0 :
        print("no such number found")
        return

    if type(numbers[0]) is not int:
        print("no integer list found")
        return

    for i in range(len(numbers)):
        if numbers[i] > biggestNumInList:
            biggestNumInList = numbers[i]
            indexOfBiggestNumInList = i
    print("index:",indexOfBiggestNumInList,"biggest number:",biggestNumInList)

testcase1 = [3, 6, 10, 7, 5, 9, 1, 8, 4, 2]
biggestNumberInList(testcase1) # expecting 10
testcase2 = [3, 6, -10, 7, 5, 9, 1, 8, 4, 2]
biggestNumberInList(testcase2) # expecting 9
testcase3 = [-1, -2, -100, -10]
biggestNumberInList(testcase3) # expecting 0
testcase4 = [0, 0, 0, 0]
biggestNumberInList(testcase4) # expecting 0
testcase5 = []
biggestNumberInList(testcase5) # expecting "no such number found"
testcase6 = ['a', 'b', 'c']
biggestNumberInList(testcase6) # expecting "no integer List found"

