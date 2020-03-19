from random import randint

# code: 1 -> times
#       2 -> divide
#       3 -> times/divide + add/minus

EQUAL_MSG = '=       '

def pretty(string):
    length = len(string)
    if length == 15:
        return string
    elif length == 14:
        return string + ' '


def math(n):

    if n == 1:
        file = open("multiplication-print.txt", "w")
        a = 6
    elif n == 2:
        file = open("division-print.txt", "w")
        a = 5
    else:
        file = open("mixed-print.txt", "w")
        a = 4
    for i in range(5):
        for j in range(8):
            for k in range(a):
                to_write = my_math(n)
                file.write(to_write)
            file.write("\n\n")
        file.write("\n\n\n")

def my_math(n):
    a = randint(2,9)
    b = randint(2,9)
    c = randint(2,9)
    d = a * b
    z = 3 * c
    if d < 10:
        return my_math(n)
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    z = str(z)
    if n == 1:
        write = a +'*' + b + EQUAL_MSG
    elif n == 2:
        write = d +'/' + a + EQUAL_MSG
    else:
        # x=1 means *, y=1 means +
        x = randint(1,2)
        y = randint(1,2)
        times =  x == 1
        add =  y == 1
        if times and add:
            write = pretty(d +'*' + a + '+' + z + EQUAL_MSG)
        elif times:
            write = pretty(d +'*' + a + '-' + c + EQUAL_MSG)
        elif add:
            write = pretty(d +'/' + a + '+' + z + EQUAL_MSG)
        else:
            write = pretty(d +'/' + a + '-' + c + EQUAL_MSG)
    return write

def final():
    n = 1
    file = open("final", "w")
    for i in range(3):
        for j in range(8):
            if n == 1:
                a = 6
            elif n == 2:
                a = 5
            else:
                a = 4
            for k in range(a):
                write = my_math(n)
                file.write(write)
            file.write("\n\n")
        file.write("\n\n\n")
        n += 1



# math(1)
# math(2)
# math(3)
final()