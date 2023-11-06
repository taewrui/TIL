n = int(input())
costs = []
for i in range(n): costs.append(list(map(int, input().split())))

houses = [[None, None, None] for i in range(n)]
houses[0][0] = costs[0][0]
houses[0][1] = costs[0][1]
houses[0][2] = costs[0][2]

for i in range(1, n):
    houses[i][0] = min(houses[i-1][1], houses[i-1][2])+ costs[i][0]
    houses[i][1] = min(houses[i-1][2], houses[i-1][0])+ costs[i][1]
    houses[i][2] = min(houses[i-1][0], houses[i-1][1])+ costs[i][2]

print(min(houses[-1]))