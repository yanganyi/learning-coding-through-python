# problem statement:
# there is an integer A. Adding 100 to A makes it a perfect square;
# on top of 100, adding another 168 makes it another perfect square.
# how many such integers exist in the range of [1,500]?

import math


def find_my_integer():
    number = 0
    for i in range(1,5001):
        a = i + 100
        b = int(math.sqrt(a))
        c = b**2
        d = a + 168
        e = int(math.sqrt(d))
        f = e**2
        if a == c and d == f:
            number += 1
    return number


print(find_my_integer())

