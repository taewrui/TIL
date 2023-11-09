t, w = map(int, input().split())
trees = []
for i in range(t): trees.append(int(input()))
print(trees)
max_plum = []

if trees[0] == 1:
    max_plum.append(1)
else:
    max_plum.append(0)
trees = trees[1:]

trees_interval = []
prev_tree = None
trees_cnt = 0
for n, i in enumerate(trees):
    if prev_tree != i and n != 0:
        trees_interval.append(trees_cnt)
        prev_tree = i
        trees_cnt = 1
        continue
    trees_cnt += 1
    prev_tree = i
trees_interval.append(trees_cnt)
#print(trees_interval)

trees_interval.sort(reverse=True)

for i in range(w+1):
    
