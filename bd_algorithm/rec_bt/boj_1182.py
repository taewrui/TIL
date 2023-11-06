def sum(k, tot):

    global cnt, n, s

    if k == n:
        if tot == s: 
            cnt += 1
        return 

    sum(k + 1, tot)
    sum(k + 1, tot + arr[k])
    

cnt = 0
n, s = map(int, input().split())
arr = list(map(int, input().split()))
sum(0, 0)
if s == 0: cnt -= 1
print(cnt)