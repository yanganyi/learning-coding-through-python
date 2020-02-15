import calc

print('This is another one of the machine made by YCM and YAY to just caculate the factorial, combination and permutation of two numbers.')
print('Enter the n and r (n>r) (type n first then r) for me to calculate the factorial, combination and permutation for you.')
n = int(input())    # the n
r = int(input())    # the r

#addition
print(n,'+',r,'=',calc.addition(n,r))    

#subtraction
print(n,'-',r,'=',calc.subtraction(n,r))

#multiplication
print(n,'*',r,'=',calc.multiplication(n,r))

#division
#todo: move the rounding part to the calc module as well

print(n,'/',r,'rounds off to',calc.division(n,r))

#power
print(n,'to the power of',r,'is',calc.power(n,r),'.')


#factorial
print('The factorial of',n,'is',calc.factorial(n),'.')
print('The factorial of',r,'is',calc.factorial(r),'.')

# combination of n, 2
# C 5 2 => 20/2! = 10
# P 5 2 => 5!/3! = 20

#combination
print('All possibilities of selecting',r,'out of',n,'is',calc.combination(n,r),'.')

#permutation
print('All possibilities of selecting',r,'out of',n,'and making the order matter is',calc.permutation(n,r),'.')

print('Now you know how to use this program to caculate factorial, combination, permutation and power.')