import math

16
4 6 10 12 6 8 12 14 18 10
3 5 9 11 5 7
n = int(input())
sk = []
k = []
for i in range(math.ceil(n/10)):
    sk.extend([int(x) for x in input().split()])
m = sk[0]
for i in range(1, n+1):
    if i == 1:
        if m > sk[1]/2:
            k.extend([2] * (m - sk[1]/2))
print(k)
