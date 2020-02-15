def name():
    username = input()
    if username.isalpha():
        if len(username) <= 10:
            print("Hello "+username+"!")

name()