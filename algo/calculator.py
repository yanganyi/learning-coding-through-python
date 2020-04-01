
# === Iterative Mode ===
# while True:
#     expression = input("Calculate (type 'exit' to exit): ")
#     if expression == 'exit':
#         break
#     else:
#         print(calculate(expression))

operators = ['+', '-', '*', '/']



def _precedence_level(op):
    lvl3 = ['^']
    lvl2 = ['*','/']
    lvl1 = ['+','-']
    if op in lvl1:
        return 1
    elif op in lvl2:
        return 2
    elif op in lvl3:
        return 3
    else:
        return -1

def _precedence(op1, op2):
    op1_lvl = _precedence_level(op1)
    op2_lvl = _precedence_level(op2)
    if op1_lvl > op2_lvl:
        return 1
    elif op1_lvl == op2_lvl:
        return 0
    elif op1_lvl < op2_lvl:
        return -1

# this function returns True when we need to pop
def _check_pop(op, stack):
    return len(stack) > 0 and _precedence(op, stack[-1]) != 1

# split an expression (string) to a infix expression (list)
def preprocess(exp_str):
    # TODO: to split by all supported operators
    infix = exp_str.split(' ')
    return infix

# convert a infix expression (list) to a postfix expression (list)
# it is a simplified version of the shunting yard algorithm
def convert_infix_to_postfix(infix):
    operator_stack = []
    postfix = []
    for i in infix:
        if i not in operators:  # if i is an operand (number)
            postfix.append(i)
        else:
            while _check_pop(i, operator_stack):
                postfix.append(operator_stack.pop())
            operator_stack.append(i)

    while len(operator_stack) > 0:
        postfix.append(operator_stack.pop())

    # print(' '.join(postfix))
    return postfix

# evaluate the postfix expression to a int/float number
# postfix is also called reversed polish notation (RPN)
def evaluate_postfix(exp):
    stack = []
    for i in exp:
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


def evaluate_infix(exp_str):
    infix_e = preprocess(exp_str)
    postfix_e = convert_infix_to_postfix(infix_e)
    result = evaluate_postfix(postfix_e)
    return result

# print(convert_infix_to_postfix("1 + 2"))
# print(convert_infix_to_postfix("1 + 2 + 3"))
# print(convert_infix_to_postfix("1 + 2 * 3 + 4"))
# print(convert_infix_to_postfix("1 * 2 + 3 * 4"))
# print(convert_infix_to_postfix("1 + 2 + 3 * 4"))
# print(convert_infix_to_postfix("1 * 2 * 3 + 4"))

print(evaluate_infix("1 + 2"))
print(evaluate_infix("1 + 2 * 3 + 4"))
print(evaluate_infix("1 * 2 + 3 * 4"))
print(evaluate_infix("1 + 2 + 3 * 4"))
print(evaluate_infix("1 * 2 * 3 + 4"))

print(evaluate_infix("1+2+3"))









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


# print(evaluate_postfix('1 2 + 3 * 4 +'))
# print(evaluate_postfix('1 2 3 * + 4 +'))
# print(evaluate_postfix('1 2 + 3 * 4 *'))
# print(evaluate_postfix('1 2 + 3 + 4 *'))
# print(evaluate_postfix('1 2 + 3 / 4 *'))
# print(evaluate_postfix('3 1 2 + * 4 * 6 / 7 + 8 9 * -'))

# print(precedence('+','-'))
# print(precedence('-','+'))
# print(precedence('+','*'))
# print(precedence('/','-'))
# print(precedence('*','/'))

# print(precedence('+','^'))
# print(precedence('^','+'))
# print(precedence('^','/'))
# print(precedence('-','^'))


# a = precedence(op,stack[-1]) != 1

