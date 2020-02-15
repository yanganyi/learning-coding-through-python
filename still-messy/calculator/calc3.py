#Addition
def add(a,b):
    return a+b
#Subtraction
def minus(a,b):
    return a-b
#Multiply
def times(a,b):
    return a*b
#Division
def divide(a,b):
    return a/b
#Remainder
def remainder(a,b):
    return a%b
#Square
def square(a):
    return a*a
#Cube
def cube(a):
    return a*a*a
#Power(easier to type)
def power(a,b):
    return a**b
#Power(using for loop)
def power2(a,b):
    result=1
    for count in range(1,b+1):
        result = result * a
    return result
#Factorial
def factorial(a):
    result=1
    for count in range(1,a+1):
        result = result * count
    return result
#Fibonacci(harder to type but faster in caculating)
def fibonacci(a):
    memo = [0] * (a+1)
    memo[0] = 1
    memo[1] = 1
    for count in range(2,a+1):
        memo[count] = memo[count-1] + memo[count-2]
    return memo[a]
#Fibonacci(easier to type but slower in caculating)
def fibonacciRecursive(a):
    if a==0: return 1
    if a==1: return 1
    return fibonacciRecursive(a-1)+fibonacciRecursive(a-2)

def waysOfJumpingStaircase(a):
    return fibonacci(a)


name=input(('What is your name?'))
print('Hello, my name is',name,'2.0. Same name as you!')
a=int(input('Please provide one number that is smaller than 30.'))
b=int(input('Please provide another number that is smaller than the previous one.'))
print(a,'+',b,'=',add(a,b))
print(a,'-',b,'=',minus(a,b))
print(a,'*',b,'=',times(a,b))
print(a,'/',b,'=',divide(a,b))
print('The remainder of',a,'divided by',b,'is',remainder(a,b))
print('The square of ',a,'is',square(a),',while the square of',b,'is',square(b),'.')
print('The cube of ',a,'is',cube(a),',while the cube of',b,'is',cube(b),'.')
print(a,'to the power of',b,'is',power(a,b),'while',b,'to the power of',a,'is',power(b,a))
print('The factorial of ',a,'is',factorial(a),',while the factorial of',b,'is',factorial(b),'.')
print('The fibonacci of ',a,'is',fibonacci(a),',while the fibonacci of',b,'is',fibonacci(b),'.')






#print(add(10,5))
#print(minus(10,5))
#print(times(10,5))
#print(divide(10,5))
#print(divide(10,3))
#print((int)(divide(10,3)))
#print((int)(divide(11,3)))
#print(remainder(10,3))
#print(remainder(11,3))
#print(square(5))
#print(cube(5))
#print(power(5,3))
#print(power2(5,3))
#print(factorial(3))
#print(factorial(6))
#print(fibonacci(100))
#print(waysOfJumpingStaircase(50))
# print(fibonacci(6))

# print(fibonacci(40))