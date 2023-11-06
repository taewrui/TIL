def fill(k, prev):
    global n, m
    if k == m:
        st = [str(i) for i in arr]
        print(' '.join(st))
        return
    
    for i in range(n):
        if i+1 <= prev: continue
        if not used[i]:
            arr[k] = i+1
            prev = arr[k]
            used[i] = True
            fill(k + 1, prev)
            used[i] = False

n, m = map(int, input().split())
arr = [None for i in range(m)]
used = [None for i in range(n)]
fill(0, 0)

