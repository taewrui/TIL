n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()
    
cont = [arr[0]]
i = 0
j = 0
cnt = 0

while i < n:
    if i == n-1:
        cnt += 1
        break
    
    while j < n:
        j += 1
        if j == n:
            l = j - i
            cnt += (l * (l+1)) // 2
            break
        
        if cont.count(arr[j]) == 0:
            cont.append(arr[j])
            
        else:
            j_idx = cont.index(arr[j])
            cont = cont[j_idx + 1:]
            cont.append(arr[j])
            
            l = j - i
            cnt += (l * (l+1)) // 2
            i = i + j_idx + 1
            break
    if j == n: break   
    
print(cnt)