import random

# code: 1 -> times
#       2 -> divide
#       3 -> times/divide + add/minus

def math(n):
    if n == 1:
        file = open("multiplication-print", "w")
    elif n == 2:
        file = open("division-print", "w")
    else:
        file
    for i in range(5):
        for j in range(8):
            for k in range(6):
                to_write = my_math(n)
                file.write(to_write)
            file.write("\n\n")
        file.write("\n\n\n")

def my_math(n):
    a = random.randint(2,9)
    b = random.randint(2,9)
    c = a * b
    if c < 10:
        return my_math(n)
    a = str(a)
    b = str(b)
    c = str(c)
    if n == 1:
        write = a+'*'+b+'=       '
    else:
        write = c+'/'+a+'=       '
    return write

test = input("What subject?")
if test == "math":
    math(1)
    math(2)
    math(3)




