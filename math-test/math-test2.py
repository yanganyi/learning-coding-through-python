import random
import time

print('What is your name?')
name = input()
print('What is your age?')
age = input()
if age.isdigit():
    age = int(age)
    qcountmultiply = int(age)
    qcountaddition = int(age)
    qcountsubtraction = int(age)
    qcount = qcountmultiply + qcountaddition + qcountsubtraction
    # alton's results
    qcorrect = 0
    qwrong = 0

    def newline():
        print()
        print()

    def add(a,b):
        return a+b

    def subtract(a,b):
        return a-b

    def multiply(a, b):
        return a*b


    print('Hey',name,'nice to meet you! I know your age is',age,'.')
    print('I am your new toy created by YAY that is designed to challenge you everyday using Math problems.')
    print('Please have fun answering these',qcount,' questions.')
    print('How long do you think you will take in total (seconds)?')
    altonGuess = int(input())

    startingtime = time.time()

    # multiplication and addition
    # testscope can be: + * -
    # testqcount
    def calculation(testscope, testqcount):
        global qcorrect, qwrong
        for i in range(1,testqcount + 1):
            # Change numbers if needed
            n1 = random.randint(3,9)
            n2 = random.randint(3,9)
            tempn = n1
            if n1<n2:
                n1=n2
                n2=tempn
            print('Question No.',i,' Please answer this question:',n1,testscope,n2,'=')
            tempinput = input()
            while (not tempinput):
                tempinput = input()
            # mul, add, sub, div
            altonAnswer = int(tempinput)

            if (testscope == '+'):
                correctAnswer = add(n1,n2)
            elif (testscope == '-'):
                correctAnswer = subtract(n1,n2)
            else:
                correctAnswer = multiply(n1,n2)
            correct = altonAnswer==correctAnswer
            if (correct):
                qcorrect = qcorrect + 1
            else:
                qwrong = qwrong + 1

            # how we are going to use this function

    calculation("+",qcountmultiply)
    calculation("*",qcountaddition)
    calculation("-",qcountsubtraction)
    endingtime = time.time()
    timeElapsed = endingtime-startingtime

    penaltyPerQuestion = 30
    totalPenalty = penaltyPerQuestion * qwrong

    finalTime = timeElapsed + totalPenalty

    newline()
    print('Alton, in','{:03.1f}'.format(timeElapsed),'seconds, you have answered',qcorrect, 'questions right and',qwrong,'questions wrong.')
    newline()
    print('The penalty is',totalPenalty,'seconds so the final time recorded is','{:03.1f}'.format(finalTime),'seconds')
    newline()
    print('Your average time per question is','{:02.1f}'.format(finalTime / qcount),'seconds')
    newline()

    if(finalTime / qcount) < 10:
        print('Congragulations, you used less than 10 seconds per question. Good Job!')
    elif(10 < (finalTime / qcount) < 20):
        print('Nice work! You used 10-20 seconds per question. Way to go!')
    else:
        print('You did not use less then 20 seconds per question. Try again next time!')

    metGoal = finalTime < altonGuess
    newline()

    if (metGoal):
        print('You met your own goal! You can set a higher goal next time!')
    else:
        print('You did not meet your goal. Try harder next time!')

else:
    print("Smart of you to test my code. Sorry to inform you I have thought of this.")