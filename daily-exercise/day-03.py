# problem statement:
# print the nth element of the fibonacci sequence,
# assuming the 1st,2nd,3rd element is 0,1,1



# time complexity: O(n)
# space complexity: O(n)
def fib(n):
    fib = [0,1,1]
    for i in range(n):
        new = fib[-1] + fib[-2]
        fib.append(new)
    return fib[n-1]

# time complexity: O(n)
# space complexity: constant, O(1)
def fibox(n):
    fib_1 = 0
    fib_2 = 1

    if n == 1:
        return 0
    else:
        for i in range(n-2):
            temp = fib_1
            fib_1 = fib_2
            fib_2 = temp + fib_2
    return fib_2


# time complexity: O(n)
# space complexity: constant, O(1)
def fibo(n):

    if n<=2:
        return n-1

    fib_1 = 0
    fib_2 = 1
    for i in range(n-2):
        fib_3 = fib_1+fib_2
        fib_1 = fib_2
        fib_2 = fib_3

    return fib_3


# time complexity: ...something big...
def fibonnaci(n):
    if n == 1:
        return 0
    elif n == 3 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)




# 0 1 1 2 3 5 8 13 21 34


# print(fib(1))   #0
# print(fib(2))   #1
# print(fib(3))   #1
# print(fib(4))   #2
# print(fib(5))   #3
# print(fib(6))   #5
# print(fib(7))   #8
# print(fib(8))   #13
# print(fib(9))   #21
# print(fib(10))  #34

print(fib(30))
print(fib(50))
#
# print(fibonnaci(1))   #0
# print(fibonnaci(2))   #1
# print(fibonnaci(3))   #1
# print(fibonnaci(4))   #2
# print(fibonnaci(5))   #3
# print(fibonnaci(6))   #5
# print(fibonnaci(7))   #8
# print(fibonnaci(8))   #13
# print(fibonnaci(9))   #21
# print(fibonnaci(10))  #34

# print(fibonnaci(30))
# print(fibonnaci(50))
#
# print(fibo(1))   #0
# print(fibo(2))   #1
# print(fibo(3))   #1
# print(fibo(4))   #2
# print(fibo(5))   #3
# print(fibo(6))   #5
# print(fibo(7))   #8
# print(fibo(8))   #13
# print(fibo(9))   #21
# print(fibo(10))  #34
#
# print(fibo(30))
# print(fibo(50))