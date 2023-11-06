n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
aidx, bidx = 0, 0

for i in range(len(a) + len(b)):

    if aidx >= len(a):
        for j in b[bidx:]: c.append(j)
        break

    if bidx >= len(b):
        for j in a[aidx:]: c.append(j)
        break

    if a[aidx] <= b[bidx]:
        c.append(a[aidx])
        aidx += 1
        continue
    elif a[aidx] > b[bidx]:
        c.append(b[bidx])
        bidx += 1
        
print(' '.join([str(i) for i in c]))