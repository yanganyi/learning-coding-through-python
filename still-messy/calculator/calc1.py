def addition(n,r):
    return n+r

def subtraction(n,r):
    return n-r

def multiplication(n,r):
    return n*r

def division(n,r):
    a = round((n/r),1)
    return a


def power(n,r):
    l=n
    for x in range(1,r):
        l=l*n
    return l

def factorial(k):
    fac = 1
    for x in range(1,k+1):
        # print('i am going to * ',x)
        fac = fac * x
    return fac

def combination(n,r):
    # first we need to know n!
    a = factorial(n)
    # next, we want to know r! and (n-r)!
    b = factorial(r)
    c = factorial(n-r)
    # lastly we calculate using the combination formula NOT taught in primary school
    return a/b/c

def permutation(n,r):
    a = factorial(n)
    b = factorial(n-r)
    return a/b