n, l = map(int, input().split())
p = 0

if n == 0:
    p = 10**(l-1)
    
elif n == 1:
    for i in range(l):
        p += (10**i)
    
else:
    p = n
    for i in range(1, l):
        p += (10**i)


    
print(p)
