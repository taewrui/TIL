def move(a, b, n):
    
    if n == 1:
        print(a, b, sep=' ')
        return
    move(a, 6-a-b, n-1)
    move(a, b, 1)
    move(6-a-b, b, n-1)

n = int(input())

print(2**n - 1)
move(1, 3, n)

