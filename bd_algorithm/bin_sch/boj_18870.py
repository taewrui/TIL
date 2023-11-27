from bisect import bisect_left, bisect_right
n = int(input())
n_list = list(map(int, input().split()))

n_sorted = sorted(n_list)
uni = []

for i, n in enumerate(n_sorted):
    if i != 0:
        if n_sorted[i-1] != n:
            uni.append(n)
    else: uni.append(n)


zipped = []
for i in n_list:
    zipped.append(bisect_left(uni, i))
    
for i in zipped:
    print(i, end=' ')
