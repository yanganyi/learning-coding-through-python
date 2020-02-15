import random

def add(a,b):
    return a+b

def multiply(a, b):
    return a*b

# multiplication and addition
# testscope can be: + *
# testqcount 
def calculation(testscope, testqcount):
    global qcorrect, qwrong
    for i in range(1,testqcount + 1):
        # Change numbers if needed
        n1 = random.randint(3,9)
        n2 = random.randint(3,9)
        print('Question No.',i,' Please answer this question:',n1,testscope,n2,'=')
        tempinput = input()
        while (not tempinput):
            tempinput = input()
        # mul, add, sub, div
        altonAnswer = int(tempinput)

        if (testscope=='+'):
            correctAnswer = add(n1,n2)
        else:
            correctAnswer = multiply(n1,n2)
        correct = altonAnswer==correctAnswer
        if (correct):
            qcorrect = qcorrect + 1 
        else: 
            qwrong = qwrong + 1 
