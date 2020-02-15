
# 3m curtain,
# a, b,
# a = random say 0.4, b = 1.7
# a = 0.85, b = 1.925
# ....
# ??? a ~ 1, b ~ 2?
# 0.001

import random

def curtain_2():
    precision = 0.000001
    a = random.uniform(0,1.5)
    while True:
        b = (3 + a) / 2
        a = (0 + b) / 2
        print(round(a,5),round(b,5))
        if abs(a - 1) < precision and abs(b - 2) < precision:
            return True


def curtain_5():
    precision = 0.0001
    a = random.uniform(0,1)
    b = (5 - a) / 4 + a
    c = (5 - b) / 3 + b
    d = (5 - c) / 2 + c
    while True:
        a = (0 + b) / 2
        b = (a + c) / 2
        c = (b + d) / 2
        d = (c + 5) / 2
        print(round(a,3), round(b,3), round(c,3), round(d,3))
        if abs(a-1) < precision and abs(b-2) < precision and abs(c-3) < precision and abs(d-4) < precision:
            return True


def curtain_generalized(length = 10, portion = 3, precision = 5):

    # initialization
    var = [0] * portion
    var[1] = random.uniform(0,length/portion)
    for i in range(2,len(var)):
        var[i] = (length - var[i-1]) / (portion - i + 1) + var[i-1]

    while True:
        for i in range(1,len(var)-1):
            var[i] = (var[i-1]+var[i+1]) / 2
        var[len(var)-1] = (var[len(var)-2] + length ) / 2

        for i in range(0,len(var)):
            print(round(var[i],precision+1))

        end_flag = True
        for i in range(0,len(var)):
            # we set end_flag to false if we found any violation
            if abs(var[i]-i*length/portion) > pow(10,-1*precision):
                end_flag = False

        if end_flag:
            return True



print(curtain_2())
# print(curtain_5())

# print(curtain_generalized())
# print(curtain_generalized(5000, 10))
# print(curtain_generalized(length=5000, precision=3))
# print(curtain_generalized(5000, 5, 6))

