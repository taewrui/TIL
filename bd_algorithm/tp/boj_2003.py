n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
total = arr[0] #첫째 값을 합에 먼저 넣음
j = 0

if arr[0] == m: #첫째 값이 부분합과 같을 때 예외처리
    cnt += 1
    
for i in range(n):
    while j < n and total < m: #포인터 범위, 부분합 조건
        j += 1 #먼저 포인터를 증가시키고 부분합 계산
        if j != n:
            total += arr[j]
        if total == m:
            cnt += 1
            break
    total -= arr[i]
    if total == m: # i가 다음으로 넘어가면서 부분합을 만족할 수도 있으므로
        cnt += 1
        continue
    
print(cnt)