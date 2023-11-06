n = int(input())
cases = [None for i in range(n)]

if n == 1:
    print(1)
    exit()
    
cases[0] = 1
cases[1] = 2

for i in range(2, n):
    cases[i] = (cases[i-1] + cases[i-2]) % 10007

print(cases[-1])