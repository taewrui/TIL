n = int(input())
index = []
for i in range(n):
    index.append(list(map(int, input().split())))
                 
index.sort(key= lambda x: (x[0], x[1]))
#lambda 함수의 결과값을 튜플로 넘겨주면, 정렬 기준을 여러 개 부여 가능
for i in index:
    print(f"{i[0]} {i[1]}")