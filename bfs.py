from collections import deque
board = [[]]
vis = [[]]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque([])
cnt = 0
max = 0

n, m = map(int, input().split())
board = [None for i in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

vis = [[False for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 0  or vis[i][j]: continue
        q.append([i, j]) # 초기값을 큐에 추가
        vis[i][j] = True # 방문 여부도 표시
        cnt += 1 # 그림 개수 추가, 그림의 넓이를 세기 시작
        area = 0
        while len(q) != 0: # 영역 구하기 시작
            cur = q[0]
            q.popleft()                
            area += 1
            #print("({0}, {1}) ->".format(cur[0], cur[1])) #방문한 칸 출력
            for dir in range(4):
                nx = cur[0] + dx[dir]
                ny = cur[1] + dy[dir]
                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
                if vis[nx][ny] or board[nx][ny] == 0: continue
                vis[nx][ny] = True
                q.append([nx, ny])
        #print(area) #각 그림의 크기 출력
        if max < area: max = area
print(cnt)
print(max)