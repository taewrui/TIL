def rec(n, a, b):
    if n==1: 
        stars[a][b] = '*'
        return

    size = int(n/3)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1: continue
            rec(size, a+size*i, b+size*j)

n = int(input())
stars = [[' ' for j in range(n)] for i in range(n)]
rec(n, 0, 0)

print('\n'.join([''.join(i) for i in stars]))
