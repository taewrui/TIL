def move(a, b, n): #a: 시작 지점 b: 목표 지점 6-a-b: 남은 한 곳
    if n==1: #base cond.
        print(a, b, sep=' ')
        return

    move(a, 6-a-b, n-1) #a에서 남은 자리로 n-1개까지 이동
    print(a, b, sep=' ')#a에서 b로 n을 이동
    move(6-a-b, b, n-1) #남은 자리에 있던 n-1개를 b로 이동

n = int(input())
print(2**n - 1)
move(1, 3, n)