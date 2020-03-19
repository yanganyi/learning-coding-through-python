
def sentence(string):
    interrogatives = ("how", "what", "why", "where", "when", "who")
    caps = string.capitalize()
    question = string.startswith(interrogatives)
    if question:
        return "{}?".format(caps)
    else:
        return "{}.".format(caps)

output = []

while True:
    string = input("Say something: ")
    if string == "\end":
        break
    else:
        string = sentence(string)
        output.append(string)

### 2 output methods

#output method 1
answer = " ".join(output)
print(answer)

#output method 2
for i in output:
    print(i, end=" ")