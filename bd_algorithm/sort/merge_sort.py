def merge(a, b):
    mid = (a + b) / 2
    aidx = a
    bidx = mid
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

def merge_sort(a, b):
    if b - a == 1: return
    mid = (a + b) // 2
    merge_sort(a, mid)
    merge_sort(mid, b)
    merge(a, b)

n = 10
arr = list(map(int, input().split()))
c = [None for i in range(len(arr))]

merge_sort(0, len(arr))       
print(' '.join([str(i) for i in c]))
