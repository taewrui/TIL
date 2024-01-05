from bisect import bisect_left
n, m, r = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
a_interval = []
for l in range(1, n):
    for i in range(l, n):
        a_interval.append(a[i]-a[i-l])
#print(a_interval)

max_area = -1

a_interval.sort()
b.sort()

r_b = [2*r/i for i in b]

for idx, k in enumerate(r_b):
    bisect_left(k, a)
print(round(max_area, 1))