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

for i in a_interval:
    if i / 2 > r: break
    for j in b:
        if j / 2 > r: break
        area = i * j * 0.5
        if area <= r and area > max_area: max_area = area
print(round(max_area, 1))