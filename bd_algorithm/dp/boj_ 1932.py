n = int(input())
tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

total = [[None for j in range(i+1)] for i in range(n)]

if n == 1:
    print(tri[0][0])
    exit()

total[0][0] = tri[0][0]
total[1][0] = tri[0][0] + tri[1][0]
total[1][1] = tri[0][0] + tri[1][1]

if n == 2:
    print(max(total[1]))
    exit()

for i in range(2, n):
    for j in range(i+1):
        a = total[i-1][j-1] if j != 0 else 0
        b = total[i-1][j] if j != i else 0
        total[i][j] = max(a, b) + tri[i][j]

print(max(total[-1]))
