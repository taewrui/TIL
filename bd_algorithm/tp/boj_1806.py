n, s = map(int, input().split())
arr = list(map(int, input().split()))

length = []
en = 0
sub_sum = arr[0]
for st in range(n):
    while en < n and sub_sum < s:
        en += 1
        if en != n: sub_sum += arr[en]
    if en == n: break
    length.append(en-st+1)
    sub_sum -= arr[st]

if len(length) == 0: print(0)
else: print(min(length))