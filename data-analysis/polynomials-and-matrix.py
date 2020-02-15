# this is an intro on Matrix Mathematics

# how to run it
# for now, we can't run it directly from IDEA
# we can only launch a anaconda prompt, and do a "python polynomials-and-matrix.py" in the right directory

import numpy as np

"""
a1*x + b1*y＋c1*z = n1
a2*x + b2*y＋c2*z = n2
a3*x + b3*y＋c3*z = n3

1x + 2y + 5z = 20
2x + 5y + 1z = 25
3x + 5y + 4z = 35

Solution: x=4,y=3,z=2

"""

a1 = 1
b1 = 2
c1 = 5
n1 = 20

a2 = 2
b2 = 5
c2 = 1
n2 = 25

a3 = 3
b3 = 5
c3 = 4
n3 = 35

m = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
n = np.array([n1, n2, n3])
solution = np.linalg.solve(m, n)

print(solution)