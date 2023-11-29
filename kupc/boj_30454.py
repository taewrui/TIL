n, l = map(int, input().split())
hairs = []
for i in range(n):
    line = input()
    hairs.append(line)


total = 0
max_black = 0
max_cnt = 0
isBlack = False

for i in range(n):
    for j in hairs[i]:
        color = int(j)
        if color == 1:
            isBlack = True
        elif color == 0 and isBlack:
            total += 1
            isBlack = False
    if isBlack:
        total += 1
        
    if total > max_black:
        max_black = total
        max_cnt = 1
    elif total == max_black:
        max_cnt += 1
    
    total = 0
    isBlack = False
    
print(f"{max_black} {max_cnt}")
    

    
        
        