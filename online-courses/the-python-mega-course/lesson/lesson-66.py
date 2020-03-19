
def area(a,b):
    return a * b

# positional arguments, based on position, cannot be swapped in some cases
print(area(4,5))

# keyword arguments, position does not matter
print(area(a = 4, b = 5))
print(area(b = 5, a = 4))


# # default argument
# def area2(a, b = 5)
# non-default arguments cannot come after default arguments
# positional argument cannot come after keyword argument