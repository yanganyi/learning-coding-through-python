import math

def mysqrt(x):
    guess = x / 2
    x = int(x)
    while True:
        delta = ( guess * guess - x ) / ( 2 * guess )
        guess = guess - delta
        if abs(delta) < 0.000001:
            break
    return guess


def verify_sqrt(x):
    expected = math.sqrt(x)
    actual = mysqrt(x)
    if abs(expected - actual) < 0.000001:
        print("Correct!")
    else:
        print("Wrong.")

def test_cases():
    verify_sqrt(2)     #1.414
    verify_sqrt(3)     #1.732
    verify_sqrt(4)     #2
    verify_sqrt(5)     #2.236
    verify_sqrt(9)     #3
    verify_sqrt(10)    #3.162
    verify_sqrt(100)   #10

test_cases()


