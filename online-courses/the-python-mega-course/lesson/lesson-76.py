
print(help(open))
with open("Hey_", "w") as file_1:
    file_1.write("Hey!")

# creates new file
# if file exists, overwrites file

with open("Hey", "w") as file:
    file.write("======\nHello world!\n======\n~~~~~~\nUsed in lesson 76\n~~~~~~")