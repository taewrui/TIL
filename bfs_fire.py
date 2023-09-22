from collections import deque
q = deque([])
r = deque([])
board = [[]]
dist_fire = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
fire_start = []
ji = [-1, -1]

n, m = map(int, input().split())
board = [[None for j in range(m)] for i in range(n)]
dist_fire = [[None for j in range(m)] for i in range(n)]
dist_ji = [[-1 for j in range(m)] for i in range(n)]

for i in range(n):
    s = input()
    for j in range(m):
        board[i][j] = s[j]
        if board[i][j] == 'F':
            q.append([i, j])
            dist_fire[i][j] = 1
        elif board[i][j] == 'J':
            r.append([i, j])
            dist_fire[i][j] = -1
            dist_ji[i][j] = 1
        elif board[i][j] == '.':
            dist_fire[i][j] = -1
        #elif board[i][j] == '#':

#print(board)
#1. 불의 확산
while len(q) != 0:
    cur = q.popleft()
    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
        if board[nx][ny] == '#' or dist_fire[nx][ny] > 0 : continue
        q.append([nx, ny])
        dist_fire[nx][ny] = dist_fire[cur[0]][cur[1]] + 1

#print(dist_fire)
#2. 사람의 이동
isEsc = False
while len(r) != 0:
    if isEsc: break
    cur = r.popleft()
    for i in range(4):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
            print(dist_ji[cur[0]][cur[1]])
            isEsc = True
            break
        if board[nx][ny] == '#' or dist_ji[nx][ny] > 0: continue
        if dist_fire[nx][ny] <= dist_ji[cur[0]][cur[1]] + 1 and dist_fire[nx][ny] != -1: continue
        r.append([nx, ny])
        dist_ji[nx][ny] = dist_ji[cur[0]][cur[1]] + 1
if not isEsc:
    print("IMPOSSIBLE")
