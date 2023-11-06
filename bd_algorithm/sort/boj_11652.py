n = int(input())
cards = []
for i in range(n):
    cards.append(int(input()))
                 
cards.sort()

cnt = 0
max_val = None
max_cnt = 0
prev_val = None

for i in cards:
    if prev_val != i:
        if cnt > max_cnt:
            max_cnt = cnt
            max_val = prev_val
        cnt = 0
    cnt += 1
    prev_val = i

if cnt > max_cnt:
    max_cnt = cnt
    max_val = prev_val
print(max_val)