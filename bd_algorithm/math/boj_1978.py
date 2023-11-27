n = int(input())
num = list(map(int, input().split()))
cnt = n


for i in num:
    if i == 1:
        cnt -= 1
        continue
    j = 2
    while j*j <= i:
        if i % j == 0: 
            cnt -= 1
            break
        j += 1
    
print(cnt)
