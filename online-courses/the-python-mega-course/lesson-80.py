import time
import os

print(os.sys.prefix)

print(dir(os))

a = os.path.exists("___")
print(a)



while True:
    if os.path.exists("___"):
        with open("___") as file:
            print(file.read())
    else:
        print("No such file.")
    time.sleep(1)