import random

def generate():
    a = random.randint(2,9)
    b = random.randint(2,9)
    c = a * b
    if c < 10:
        return generate()
    a = str(a)
    b = str(b)
    write = a+'*'+b+'=       '
    return write

for i in range(5):
    for j in range(8):
        for k in range(6):
            to_write = generate()
            with open("multiplication-print", "a") as file:
                file.write(to_write)
        with open("multiplication-print", "a") as file:
            file.write("\n\n")
    with open("multiplication-print", "a") as file:
        file.write("\n\n\n")


