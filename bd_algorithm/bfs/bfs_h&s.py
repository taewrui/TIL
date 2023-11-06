from collections import deque
q = deque([])
board = [None for i in range(100001)]
dist = [-1 for i in range(100001)]
n, k = map(int, input().split())
catched = False

if n == k: 
    catched = True
    print(0)
if not catched:
    q.append(n)
    dist[n] = 0

for i in range(10):
    if catched: break
    cur = q[0]
    q.popleft()
    move = [cur+1, cur-1, 2*cur]
    print(move[0], move[1], move[2])
    for j in move:
        if j < 0 or j > 100000: continue
        if dist[j] >= 0: continue
        dist[j] = dist[cur] + 1
        q.append(j)
        #print(j)
        if board[j] == k:
            print(dist[j])
            catched = True
            break