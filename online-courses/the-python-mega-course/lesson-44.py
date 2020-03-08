
name_1 = input("Enter your name: ")
surname_1 = input("Enter your surname: ")
message_1 = "Hello {} {}!".format(name_1, surname_1)
print(message_1)

name_2 = input("Enter your name: ")
surname_2 = input("Enter your surname: ")
message_2 = f"Hello {name_2} {surname_2}!"
print(message_2)

name_3 = input("Enter your name: ")
surname_3 = input("Enter your surname: ")
message_3 = "Hello %s %s!" % (name_3, surname_3)
print(message_3)
