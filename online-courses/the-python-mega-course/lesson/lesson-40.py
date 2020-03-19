
# not a good practice
if      3 > 1:
    print('a')

print('aa')
print('aaa')

# not a good practice
if 3>1:
    print('b')

print('bb')
print('bbb')

# GOOD!!!
if 3 > 1:
    print('c')
                        # <- break line for logic and readability
print('cc')
print('ccc')