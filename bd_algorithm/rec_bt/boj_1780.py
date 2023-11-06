def cut(paper):
    global cnt
    if isSame(paper) or len(paper[0]) == 1: 
        cnt[paper[0][0]+1] += 1 #Base Condition
        return
    
    size = int(len(paper[0]) / 3)
    
    for i in range(3):
        for j in range(3):
            x_start, x_end = size*i, size*(i+1)
            y_start, y_end = size*j, size*(j+1)
            

            new_paper = paper[x_start:x_end]
            new_paper = [row[y_start:y_end] for row in new_paper]
            cut(new_paper)


def isSame(paper):
    num = paper[0][0]
    for i in paper:
        for j in i:
            if j != num: return False
    return True
    
n = int(input())
cnt = [0, 0, 0]
paper = [[None for j in range(n)] for i in range(n)]
for i in range(n):
    paper[i] = list(map(int, input().split()))

cut(paper)

for i in cnt: print(i)