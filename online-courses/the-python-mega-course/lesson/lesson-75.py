
# note that the file "hello" is not in the same directory as this file,
# so we have to do it as follows:
with open("file/hello") as file:
    content = file.read()

print(content)
