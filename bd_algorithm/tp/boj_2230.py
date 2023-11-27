n, m = map(int, input().split())
a = []
for i in range(n): a.append(int(input()))

a.sort()
diff = []
en = 0
for st in range(n):
    while en < n :
        if a[en] - a[st] >= m:
            diff.append(a[en] - a[st])
            break
        en += 1

print(min(diff))