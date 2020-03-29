
# while True:
#     expression = input("Calculate (type 'exit' to exit): ")
#     if expression == 'exit':
#         break
#     else:
#         print(calculate(expression))

operators = ['+', '-', '*', '/']

def verify(exp,ans):
    a = float(calculator(exp))
    if a != ans:
        print('Something went wrong! The answer given was',a,'but the correct answer is',ans,'.')

def calculate(exp):
    x = exp.split(' ')
    n = []
    n.append(int(x[0]))
    n.append(x[1])
    n.append(int(x[2]))
    if n[1] == '+':
        return str(n[0]+n[2])
    elif n[1] == '-':
        return str(n[0]-n[2])
    elif n[1] == '*':
        return str(n[0]*n[2])
    elif n[1] == '/':
        return str(n[0]/n[2])

def calculator(exp):
    x = exp.split(' ')
    length = len(x)
    if length%2 == 0:
        print("Some error occurred in the calculator function.")
    else:
        noOfOperations = int((length-1) / 2)
        result = x[0]
        cursor = 1
        for i in range(noOfOperations):
            string = result + ' ' + x[cursor] + ' ' + x[cursor+1]
            result = calculate(string)
            cursor += 2

        return result


##### ====== serious business

# also called reversed polish notation (RPN) or postfix notation
def evaluate_postfix(exp):
    x = exp.split(' ')
    stack = []
    for i in x:
        if i in operators:
            operand1 = int(stack.pop())
            operand2 = int(stack.pop())
            if i == operators[0]:
                temp = operand2 + operand1
            elif i == operators[1]:
                temp = operand2 - operand1
            elif i == operators[2]:
                temp = operand2 * operand1
            else:
                temp = operand2 / operand1
        else:
            temp = i

        stack.append(temp)

    return stack[0]


def op_stack(obj,stack,output):
    length = len(stack)
    if length > 0:
        a = precedence(obj,stack[-1])
        if a == 1:
            stack.append(obj)
        else:
            # TODO (ron): while true: loop until ...
            for i in range(0,length,-1):
                a = precedence(obj,stack[i])
                if a < 1:
                    output += stack[i]  # TODO (ron): change it to append instead
                    stack.pop(i)
            stack.append(obj)
    else:
        stack.append(obj)
    return stack,output


# shunting yard algorithm
def convert_infix_to_postfix(exp):
    x = exp.split(' ')
    operator_stack = []
    output = '' # TODO (ron): change it to a list
    for i in x:
        if i in operators:
            operator_stack,output = op_stack(i,operator_stack,output)
        else:
            output = output + i # TODO (ron): append to a list instead
    # TODO (ron): process the remaining elements in stack here
    return output

print(convert_infix_to_postfix("1 + 2"))






def evaluate_infix(e):
    postfix_e = convert_infix_to_postfix(e)
    result = evaluate_postfix(postfix_e)
    return result


def precedence(op1,op2):
    op1_lvl = lvl_precedence(op1)
    op2_lvl = lvl_precedence(op2)
    if op1_lvl > op2_lvl:
        return 1
    elif op1_lvl == op2_lvl:
        return 0
    elif op1_lvl < op2_lvl:
        return -1

def lvl_precedence(op):
    lvl3 = ['^']
    lvl2 = ['*','/']
    lvl1 = ['+','-']
    if op in lvl1:
        return 1
    elif op in lvl2:
        return 2
    elif op in lvl3:
        return 3

# print("expected wrong answers")
# verify("2 + 1",0)
# verify("2 / 1",2.1)

# print("simple expression")
# verify("2 + 1",3)
# verify("2 - 1",1)
# verify("2 * 1",2)
# verify("2 / 1",2.0)

# print("complex expression")
# verify("2 * 3 + 4",10)

# print(calculator('1 + 2 + 1'))
# print(calculator('1 + 2 * 3'))
# print(calculator('1 - 2 + 1'))
# print(calculator('2 - 1 / 1'))
# print(calculator('5 - 1 / 2'))

# verify('1 + 2 + 1',4)
# verify('1 + 2 * 3',9)
# verify('1 - 2 + 1',0)
# verify('2 - 1 / 1',1.0)
# verify('5 - 1 / 2',2.0)
# verify('1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10',55)
# verify('1 * 2 * 3 * 4 * 5',120)

# exp = 'hello + bye'
# x = exp.split(' ')
# print(x[1])
# print(type(1+2))

# print(evaluate_postfix('1 2 + 3 * 4 +'))
# print(evaluate_postfix('1 2 3 * + 4 +'))
# print(evaluate_postfix('1 2 + 3 * 4 *'))
# print(evaluate_postfix('1 2 + 3 + 4 *'))
# print(evaluate_postfix('1 2 + 3 / 4 *'))
# print(evaluate_postfix('3 1 2 + * 4 * 6 / 7 + 8 9 * -'))

# print(precedence('+','+'))
# print(precedence('+','-'))
# print(precedence('+','*'))
# print(precedence('+','/'))
# print(precedence('-','+'))
# print(precedence('-','-'))
# print(precedence('-','*'))
# print(precedence('-','/'))
# print(precedence('*','+'))
# print(precedence('*','-'))
# print(precedence('*','*'))
# print(precedence('*','/'))
# print(precedence('/','+'))
# print(precedence('/','-'))
# print(precedence('/','*'))
# print(precedence('/','/'))
#
# print(precedence('+','^'))
# print(precedence('^','+'))
# print(precedence('^','/'))
# print(precedence('-','^'))

# 0 0 -1 -1 0 0 -1 -1 1 1 0 0 1 1 0 0
# -1 1 1 -1
