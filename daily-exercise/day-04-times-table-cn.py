# problem statement:
# print the entire times table in chinese
# 一一得一
# 一二得二 二二得四
# 一三得三 二三得六 三三得九
# 一四得四 二四得八 三四十二 四四十六
# 一五得五 二五一十 三五十五 四五二十 五五二十五
# 一六得六 二六十二 三六十八 四六二十四 五六三十 六六三十六
# 一七得七 二七十四 三七二十一 四七二十八 五七三十五 六七四十二 七七四十九
# 一八得八 二八十六 三八二十四 四八三十二 五八四十 六八四十八 七八五十六 八八六十四
# 一九得九 二九十八 三九二十七 四九三十六 五九四十五 六九五十四 七九六十三 八九七十二 九九八十一

def times_table_chinese():
    for i in range(1,10):
        for j in range(1,i+1):
            multiply = i * j
            ch_multiply = times_table_translate(multiply)
            ch_i = translate(i)
            ch_j = translate(j)
            print('{}{}{}'.format(ch_j, ch_i,ch_multiply),end=' ')
        print()

def times_table_translate(n):
    special = ''
    if (n<10):
        special = '得'
    return special + translate(n)

def translate(n):
    n = int(n)
    vocab = ['零','一','二','三','四','五','六','七','八','九','十']
    ones = n % 10
    tens = int((n - ones) / 10)
    if ones == n:
        return vocab[n]
    else:
        if tens == 1 and ones == 0:
            return vocab[1] + vocab[10]
        elif ones == 0:
            return vocab[tens] + vocab[10]
        elif tens == 1:
            return vocab[10] + vocab[ones]
        else:
            return vocab[tens] + vocab[10] + vocab[ones]

times_table_chinese()


def ch_answer():
    for i in range(1,10):
        print()
        for j in range(1,i+1):
            multiply = i * j
            ch_multiply = digits(multiply)
            ch_i = ch(i)
            ch_j = ch(j)
            print('{}{}{}'.format(ch_j, ch_i,ch_multiply),end=' ')

def digits(n):
    ones = n % 10
    a = (n - ones) / 10
    ch_ones = ch(ones)
    if a > 0:
        tens = a % 10
        ch_tens = ch(tens)
        if ones == 0 and tens == 1:
            return "一十"
        elif ones == 0:
            return ch_tens + "十"
        elif tens == 1:
            return "十" + ch_ones
        else:
            return ch_tens + "十" + ch_ones
    else:
        return "得" + ch_ones

def ch(n):
    n = int(n)
    characters = ['十','一','二','三','四','五','六','七','八','九']
    return characters[n]
    # if n == 0:
    #     return "十"
    # elif n == 1:
    #     return "一"
    # elif n == 2:
    #     return "二"
    # elif n == 3:
    #     return "三"
    # elif n == 4:
    #     return "四"
    # elif n == 5:
    #     return "五"
    # elif n == 6:
    #     return "六"
    # elif n == 7:
    #     return "七"
    # elif n == 8:
    #     return "八"
    # else:
    #     return "九"

# ch_answer()