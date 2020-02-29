# problem statement:
# print the entire times table

def my_slow_answer():
    for i in range (1,10):
        for j in range(1,10):
            a = str(i)
            b = str(j)
            c = str(i*j)
            if b <= a:
                print(a+'*'+b+'='+c+' ', end='')
    print('\n',end='')


def my_faster_answer():
    for i in range (1,10):
        print() # newline
        for j in range(1,i+1):
            print("%d*%d=%d"%(i,j,i*j),end=' ')

my_faster_answer()





