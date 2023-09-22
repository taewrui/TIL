from collections import deque
board = [[]]
dist = [[]]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque([])
cnt = 0
max = 0

n, m = map(int, input().split())

board = [[None for j in range(m)] for i in range(n)]
for i in range(n):
    line = input()
    for j in range(len(line)):
        board[i][j] = int(line[j])

dist = [[-1 for j in range(m)] for i in range(n)]


q.append([0, 0]) # 초기값을 큐에 추가
dist[0][0] = 1 # 거리, -1은 미방문
while len(q) != 0: # 영역 구하기 시작
    cur = q[0]
    q.popleft()                           
    #print("({0}, {1}) ->".format(cur[0], cur[1])) #방문한 칸 출력
    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]
        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
        if dist[nx][ny] != -1 or board[nx][ny] == 0: continue
        dist[nx][ny] = dist[cur[0]][cur[1]] + 1
        q.append([nx, ny])
print(dist[n-1][m-1])
        