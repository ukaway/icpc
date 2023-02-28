import math
import sympy as sp


# a^2 + b^2 = c^2
# PPT: Primitive Pythagorean Triple if a, b, c have no common factors
def is_ppt(a, b, c):
    if math.gcd(math.gcd(a, b), c) == 1:
        return True
    return False


# find the number of PPT and non-PPT when c is specified
def find_a(c):
    c_pt = 0                # c_pt: count the number of Pythagorean Triple
    c_ppt = 0               # c_ppt: count the number of PPT
    for a in range(1, math.ceil(c/math.sqrt(2)+1)):
        # assume a < b
        # 2a^2 ≤ a^2 + b^2 = c^2
        # (√2a - c)(√2a + c) ≤ 0 <=> 1 ≤ a ≤ c/√2
        b = math.sqrt(c**2 - a**2)
        if b == int(b):     # if b is integer
            c_pt += 1
            if is_ppt(a, int(b), c):
                c_ppt += 1
    print(c_ppt, c_pt - c_ppt, end=' ')
    return


# find the number of PPT and non-PPT when a is specified
def find_bc(a):
    c_pt = 0
    c_ppt = 0
    div = sp.divisors(a**2)
    for i in range(round(len(div)/2+1)):
        # assume a^2 = m * n where m, n are divisors of a and m < n
        # a^2 = c^2 - b^2 = (c - b)(c + b)
        # thus c - b = m, c + b = n
        # c = (m + n)/2, b = (n - m)/2
        b = (div[-1-i]-div[i])/2
        c = (div[i]+div[-1-i])/2
        if b <= 0 or c <= 0:
            continue
        if b == int(b) and c == int(c):
            c_pt += 1
            if is_ppt(a, int(b), int(c)):
                c_ppt += 1
    print(c_ppt, c_pt - c_ppt)
    return


# main
n = int(input())
find_a(n)
find_bc(n)

