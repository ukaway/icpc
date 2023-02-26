import itertools as it

# function to flip 0 <-> 1; 0:top; 1: bottom
def flip(i, j, k):
    return abs(i-1), abs(j-1), abs(k-1)

# 3 cards are SET if they all have the same property or the different properties
# x, y, z: one side of a card
# l: a property; count, color, fill, shape for each letters in a card
def is_set(x, y, z):
    for l in {0, 1, 2, 3}:
        if x[l] == y[l] == z[l]:
            return True
        if x[l] != y[l] != z[l]:
            return True
    return False

# 3 cards are PSET if the top cards (possibly after flipping) are SET AND the bottoms are SET
# a, b, c: one card
# combinations of 3 cards' sides are 000, 001, 010, 011, 100, 101, 110, 111
# when flipped, 100 -> 011, 101 -> 010, 110 -> 001, 111 -> 000, so these do not need to be gone through
# when is_PSET() found PSET, it ends for-loop and returns 1
# else, is_PSET() returns 0
def is_pset(a, b, c):
    comb = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1]]
    for [i, j, k] in comb:
        if is_set(a[i], b[j], c[k]):
            ni, nj, nk = flip(i, j, k)
            if is_set(a[ni], b[ni], c[ni]):
                return 1
    return 0

# n: number of cards
n = int(input())
# ans: number of PSET pairs
ans = 0
# cards: lists(top/bottom card) in list
cards = []
for i in range(n):
    cards.append(input().split())

for a, b, c in it.combinations(range(n), 3):
    ans += is_pset(cards[a], cards[b], cards[c])

print(ans)
