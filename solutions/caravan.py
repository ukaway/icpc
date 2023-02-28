import math

# n: number of oasis locations
# m: number of caravan trips
[n, m] = [int(x) for x in input().split()]
o = [int(x) for x in input().split()]
for i in range(m):
    # d: index of destination oasis in the list o
    # t: number of days to get there
    [d, t] = [int(x) for x in input().split()]
    # combination with repetition (n+r-1Cr)
    r = t - o[d-1]
    print(math.comb(len(o[:d])+r, r))


