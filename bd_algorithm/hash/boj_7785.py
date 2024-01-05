def custom_hash(a):
    return hash(a) % 1000000

n = int(input())
ht = [False for i in range(1000000)]
names = [None for i in range(n)]

for i in range(n):
    names[i], ent = map(str, input().split())
    if ent == "enter":
        ht[custom_hash(names[i])] = True
    else:
        ht[custom_hash(names[i])] = False

names.sort(reverse=True)
for name in names:
    if ht[custom_hash(name)]: print(name)

