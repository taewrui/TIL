n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
total = arr[0]
j = 0
for i in range(n):
    
    while j < n and total <= m:
        j += 1
        if j == n: break
        
        if total == m:
            cnt += 1
            break
        
        total += arr[j]
    total -= arr[i]
    
    
print(cnt)