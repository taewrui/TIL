n = int(input())
ropes = []
for i in range(n): ropes.append(int(input()))

ropes.sort(reverse=True)
max_w = []
for n, rope in enumerate(ropes):
    max_w.append((n+1) * rope)

print(max(max_w))
