
# Requirement:
# part 1:
# write a function gcd(...) such that
# given two positive integers,
# compute and return the highest common factor
# the caller will print the returned hcf out on the console
# input: 24, 60 output: 12
# input: 12, 23 output: 1
# input: 27, 81 output: 27

# part 2:
# write a verify() function, which takes in the needed parameters for hcf,
# as well as the expected output, the verify() function output "right" or "wrong" for each call
# e.g. verify(15,5,5)

def hcf_v1 (a,b):
    repeat = True
    while repeat:
        if a % b == 0:
            ans = b
            repeat = False
        elif b % a == 0:
            ans = a
            repeat = False
        elif a > b:
            a = a % b
        elif b > a:
            b = b % a
    return ans

# main changes
# - simplify the logics
def hcf_v2 (a,b):
    while True:
        if a % b == 0:
            return b
        elif b % a == 0:
            return a
        elif a > b:
            a = a % b
        elif b > a:
            b = b % a

# main changes
# - enforce a>=b
def hcf_v3 (a,b):
    if a < b:
        hcf_v3(b,a)
    while True:
        if a % b == 0:
            return b
        else:
            c = b
            b = a % b
            a = c


def hcf_recur(a,b):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif a > b:
        a = a % b
        return hcf_recur(a,b)
    elif b > a:
        b = b % a
        return hcf_recur(a,b)


def verify_hcf(a, b, expected):
    actual = hcf_recur(a,b)
    if actual == expected:
        print("Right!")
    else:
        print("Wrong! Input:",a,b,"Output:",actual,"Expected:",expected)

def run_testcases():
    verify_hcf(15, 5, 5)
    verify_hcf(4, 9, 1)
    verify_hcf(1, 1, 1)
    verify_hcf(3500, 3000, 500)
    verify_hcf(5, 15, 5)
    verify_hcf(1, 5, 1)
    verify_hcf(10, 10, 10)
    verify_hcf(1000, 100, 100)

run_testcases()
