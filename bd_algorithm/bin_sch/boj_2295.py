def binary_search(n):
    st = 0
    en = len(two_sum) - 1
    while st <= en:
        mid = (st + en) // 2
        if two_sum[mid] == n:
            return True
        elif two_sum[mid] > n:
            en = mid - 1
        else:
            st = mid + 1
    return False
     
n = int(input())
u = []
for i in range(n):
    u.append(int(input()))

u.sort()

k = []
two_sum = []
for i in u:
    for j in u:
        two_sum.append(i + j)

two_sum.sort()
for i in sorted(u, reverse=True):
    for j in u:
        if i - j >= 0 and binary_search(i - j):
            k.append(i)
print(max(k))
