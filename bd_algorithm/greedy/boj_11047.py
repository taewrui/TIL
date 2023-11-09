n, k = map(int, input().split())
val = []
for i in range(n): val.append(int(input()))

cnt = [0 for i in range(n)]

for idx, coin in enumerate(reversed(val)):
    cnt[idx] += k // coin
    k = k - coin * cnt[idx]

print(sum(cnt))
        
