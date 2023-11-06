n = int(input())
arr = []
for i in range(n + 1):
    prev_list = []
    if i == 0 or i == 1: 
        arr.append(0)
        continue
    if i % 2 == 0:
        prev_list.append(arr[i//2]+1)
    if i % 3 == 0:
        prev_list.append(arr[i//3]+1)
    prev_list.append(arr[i-1]+1)
    arr.append(min(prev_list))

print(arr[-1])
