def answer():
    for i in range(4):
        list = [1,2,3,4]
        a = list[i]
        for j in range(4):
            b = list[j]
            for k in range(4):
                c = list[k]
                if a!=b and a!=c and b!=c:
                    print(a,b,c)

answer()

def answer2():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i!=j and i!=k and j!=k:
                    print(i,j,k)


def answer_special():
    for i in range(4):
        list = [1,2,3,4]
        a = list[i]
        list.pop(i)
        for j in range(3):
            b = list[j]
            list.pop(j)
            for k in range(2):
                c = list[k]
                print(a,b,c)
            list.insert(j,b)
        list.insert(i,a)
