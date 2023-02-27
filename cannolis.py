import math

# D: cone base diameter
# S: slant height
# r: radius of the dough disk
# O: the desired overlap
# B: the distance from the bottom of the cone to the bottom of the dough to achieve the desired overlap
[D, S, r, O] = [float(x) for x in input().split()]

# Dπ = Sø  <=>  ø = (D/S)*π
phi = (D/S) * math.pi
halfphi = phi / 2
# x = S - (r + B)
x = (r-O/2)/math.sin(halfphi)
B = S - x - r

# if O is not possible because r is too large
if B < 0:
    print(-1.0)
    exit()
# if O is not possible because r is too small
if B > S - 2*r:
    print(-2.0)
    exit()
print(round(float(B), 1))

