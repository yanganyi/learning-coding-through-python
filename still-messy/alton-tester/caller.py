import time
import callee

print('What is your name?')
name = input()
print('What is your age?')
age = int(input())

qcountmultiply = int(age * 1.5)
qcountaddition = int(age * 1.5)
qcount = qcountmultiply + qcountaddition

# alton's results
qcorrect = 0
qwrong = 0

def newline():
    print()
    print()


print('Hey',name,'nice to meet you! I know your age is',age,'.')
print('I am your new toy created by YAY that is designed to challenge you everyday using Math multiplication problems.')
print('Please have fun answering these',qcount,' questions.')
print('How long do you think you will take in total?')
altonGuess = int(input())

startingtime = time.time()

callee.calculation("+",qcountmultiply)
callee.calculation("*",qcountaddition)

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

newline()
print('By the way, we are going to add more problems using different signs like subtraction.')
