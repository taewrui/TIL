n = int(input())
score = [[None, None] for i in range(n)]
stairs = []
for i in range(n): stairs.append(int(input()))

if n == 1: 
    print(stairs[0])
    exit()

score[0][0] = stairs[0]
score[0][1] = 0

score[1][0] = stairs[1]
score[1][1] = stairs[1] + stairs[0]

if n == 2:
    print(max(score[1][0], score[1][1]))
    exit()


for i in range(2, n):
    score[i][0] = max(score[i-2][0], score[i-2][1]) + stairs[i]
    score[i][1] = score[i-1][0] + stairs[i]

print(max(score[-1][0], score[-1][1]))