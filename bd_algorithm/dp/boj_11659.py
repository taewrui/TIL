n, m = map(int, input().split())
num = list(map(int, input().split()))
scopes = []

for i in range(m): scopes.append(list(map(int, input().split())))

if n == 1:
    print(num[0])
    exit()
    
cuml = [0, num[0]]
for i in range(2, n+1):
    cuml.append(cuml[i-1] + num[i-1])

for scope in scopes:
    i, j = scope[0], scope[1]
    print(cuml[j] - cuml[i-1])


