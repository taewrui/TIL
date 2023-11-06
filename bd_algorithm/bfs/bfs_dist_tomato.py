from collections import deque
board = []
dist = [[]]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque([])


m, n = map(int, input().split())

for i in range(n):
    board.append(list(map(int, input().split())))

dist = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append([i, j])
        if board[i][j] == 0:
            dist[i][j] = -1


while len(q) != 0: # 영역 구하기 시작
    cur = q[0]
    q.popleft()
    #print("({0}, {1}) ->".format(cur[0], cur[1])) #방문한 칸 출력
    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]
        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
        if dist[nx][ny] >= 0: continue
        dist[nx][ny] = dist[cur[0]][cur[1]] + 1
        q.append([nx, ny])

ans = 0
isans = True
for i in range(n):
    for j in range(m):
        if dist[i][j] == -1:
            isans = False
            
            break
        if dist[i][j] > ans:
            ans = dist[i][j]
if isans: print(ans)
else: print(-1)


        