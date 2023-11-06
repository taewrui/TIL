n, c = map(int, input().split())
arr = list(map(int, input().split()))

arr_sorted = sorted(arr)

freq = dict() 
order = dict()
cnt = 0
prev_val = None
for i in arr_sorted: # 빈도 수 계산
    if prev_val != i and prev_val is not None:
        freq[prev_val] = cnt
        order[prev_val] = arr.index(prev_val)
        cnt = 0
    cnt += 1
    prev_val = i
freq[prev_val] = cnt
order[prev_val] = arr.index(prev_val)

arr.sort(key=lambda x: (freq[x], -order[x]), reverse=True) # 오름차순, 내림차순을 달리 적용할 때 
for i in arr: print(i, sep=' ')