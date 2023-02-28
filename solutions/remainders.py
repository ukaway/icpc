import math

# Sk(n) = ∑(K in K | n mod K)
# N = range(1, n+1)
# find list K

# partial Sk(n)
def prt_sk(k, n):
    if k == []:
        return 0
    p_sk = 0
    for rem in k:
        p_sk += n % rem
    return p_sk


n = int(input())
sk = []
k = []
# input 10 values per line
for i in range(math.ceil(n/10)):
    sk.extend([int(x) for x in input().split()])
# m: length of the list K
m = sk[0]
for i in range(2, n+1):
    x = m - len(k) - (sk[i-1] - prt_sk(k, i))/i
    k.extend([i] * int(x if x > 0 else 0))
    if len(k) == m:
        break

print(m, *k, sep=' ')
