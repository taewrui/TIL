def count(n, r, c):
    h = n/2
    if n == 0:
        return 0
    
    if r < h and c < h: return count(n-1, r, c)
    elif r < h and c >= h: return h*h + count(n-1, r, c-h)
    elif r >= h and c < h: return 2*h*h + count(n-1, r-h, c)
    elif r >= h and c >= h: return 3*h*h + count(n-1, r-h, c-h)

n, r, c = map(int, input().split())
