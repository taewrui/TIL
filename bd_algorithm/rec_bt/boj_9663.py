def queen(k):
    global n, cnt
    if k == n:
        cnt += 1
        return
    
    for i in range(n):
        if used_1[i] or used_2[i+k] or used_3[k-i+n-1]: continue
        
        used_1[i] = True
        used_2[i+k] = True
        used_3[k-i+n-1] = True
        queen(k + 1)
        used_1[i] = False
        used_2[i+k] = False
        used_3[k-i+n-1] = False

n = int(input())
cnt = 0
arr = [[None for j in range(n)] for i in range(n)]
used_1 = [False for i in range(n)]
used_2 = [False for i in range(2*n-1)]
used_3 = [False for i in range(2*n-1)]
#열 방향, 양방향 대각선, 음방향 대각선

queen(0)
print(cnt)

