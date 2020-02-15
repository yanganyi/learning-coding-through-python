
# typical ways of debugging
# - using print() and print out key variables' values
# - using IDE's breakpoints + step over/into

def perfect_squares(size):
    v = [1] * size
    for i in range(len(v)):
        v[i] = i * i
    for i in range(len(v)):
        print(i, v[i])


perfect_squares(10)