
def hcf(a,b):
    if b > a:
        a,b = b,a
    a = a % b
    if a == 0:
        return b
    return hcf(a,b)

def lcm(a,b):
    c = a * b
    h = hcf(a,b)
    return int(c / h)

def hcf_lcm(a,b):
    c = a * b
    h = hcf(a,b)
    l = int(c/h)
    return h,l

def helper(a,b):
    h, l = hcf_lcm(a,b)
    print("HCF:",h,"LCM",l)

def verify(a,b,h,l):
    x,y = hcf_lcm(a,b)
    if x == h and y == l:
        print("True")
    else:
        print("False")

# testcases verify
verify(1,1,1,1)
verify(1,2,1,2)
verify(3,6,3,6)
verify(6,3,3,6)
verify(8,12,4,24)
verify(12,8,4,24)
verify(24,64,8,192)
verify(11,13,1,143)
verify(11,121,11,121)
verify(120,45,15,360)

# # testcases helper
# helper(1,1)
# helper(1,2)
# helper(3,6)
# helper(6,3)
# helper(8,12)
# helper(12,8)
# helper(24,64)
# helper(11,13)
# helper(11,121)
# helper(120,45)