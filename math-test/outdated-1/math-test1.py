import random
import math

name = input("What is your name?")
age = input("What is your age?")
if age.isdigit() == True:
    age = int(age)
    if age <= 5:
        print("Oh so you are still a baby! Hello baby",name,".")
    elif age > 5 and age < 12:
        print("Oh so you are still a child! Hello master",name,".")
    elif age >= 12 and age < 18:
        print("Wow you are a teenager! Hello teenager",name,".")
    elif age >= 18 and age < 80:
        print("You are still young! Hello Ms/Miss/Mrs/Mdm/Mr/Sir/Dr",name,".")
    elif age >= 80 and age <= 122 :
        print("Hello old man/woman!")
    else:
        print("...")
        print("Seriously?")
        print("Don't tell me you broke the world record for oldest person ever who is Jeanne Louis Calment who lived for 122 years and 164 days.")


    for i in range(4):
        a = random.randint(100,500)
        b = random.randint(100,500)
        print("What is",a,"plus",b,"?")
        h1 = input()
        c1 = a + b
        if int(h1) == c1:
            print("You are correct!")
        else:
            print("You are wrong")
        print("What is",a,"minus",b,"?")
        h2 = input()
        c2 = a - b
        if int(h2) == c2:
            print("You are correct!")
        else:
            print("You are wrong")
        print("What is",b,"minus",a,"?")
        h3 = input()
        c3 = b - a
        if int(h3) == c3:
            print("You are correct!")
        else:
            print("You are wrong")



elif age.isdigit() == False:
    print("Congrats!!! I never knew that",age,"was an age!")















