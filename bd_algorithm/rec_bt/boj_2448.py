from math import log2
def rec(n, a, b): #a는 시작 행, b는 시작 열(중앙)

    if n==3: 
        draw_tri(a, b)
        return

    size = int(n/2)
    
    rec(n/2, a, b)
    rec(n/2, a+size, b-size)
    rec(n/2, a+size, b+size)

def draw_tri(a, b):
    stars[a][b] = '*'
    stars[a+1][b-1], stars[a+1][b+1] = "*", "*"
    for i in range(5):
       stars[a+2][b-2+i] = "*"
        

n = int(input())
k = int(log2(n/3))
size_x = (n//3*5) + n//3 - 1


stars = [[' ' for j in range(size_x)] for i in range(n)]
rec(n, 0, int(size_x / 2))

print('\n'.join([''.join(i) for i in stars]))
