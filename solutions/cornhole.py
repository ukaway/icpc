# h: the number of bags a player got through the hole (3 pts)
# b: the number of bags a player got on the board (1 pt)
[h1, b1] = [int(x) for x in input().split()]
[h2, b2] = [int(x) for x in input().split()]
score1 = h1*3 + b1*1
score2 = h2*3 + b2*1
if score1 == score2:
    print("NO SCORE")
    exit()
print(1 if score1 > score2 else 2, abs(score1-score2))
