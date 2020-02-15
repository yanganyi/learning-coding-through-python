import itertools

listA = [1,3,5,6,7,10,13,16]

def verifySolution(a,b,c,d,e,f,g,h):
    return f+d==h and g+c==a and f+b==e and c+a==d and a+h==e

def printSolution(a,b,c,d,e,f,g,h):
    print('Hooray, I found the correct solution! A =',solCandidate[0],'B =',solCandidate[1],'C =',solCandidate[2]
        ,'D =',solCandidate[3],'E =',solCandidate[4],'F =',solCandidate[5],'G =',solCandidate[6],'H =',solCandidate[7])

# a python way to generate all possibilities with brute force
allperm = list(itertools.permutations(listA))

for row in allperm:
    solCandidate = list(row)
    #print('i am verifying this solution',solCandidate)
    a = solCandidate[0]
    b = solCandidate[1]
    c = solCandidate[2]
    d = solCandidate[3]
    e = solCandidate[4]
    f = solCandidate[5]
    g = solCandidate[6]
    h = solCandidate[7]
    if verifySolution(a,b,c,d,e,f,g,h):
        printSolution(a,b,c,d,e,f,g,h)
        break
    
