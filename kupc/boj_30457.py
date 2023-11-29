n = int(input())
a = list(map(int, input().split()))

a.sort()
total = 0
cnt = 0
for idx, i in enumerate(a):
    if idx != 0:
        if a[idx-1] == i:
            cnt += 1
        else:
            total += min(cnt, 2)
            cnt = 1
    else:
        cnt = 1
        
total += min(cnt, 2)
print(total) 

        