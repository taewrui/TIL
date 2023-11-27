def binary_search(n):
    st = 0
    en = len(b_list) - 1
    while st <= en:
        mid = (st + en) // 2
        if b_list[mid] == n:
            return True
        elif b_list[mid] > n:
            en = mid - 1
        else:
            st = mid + 1
    return False

a, b = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

ab = []
b_list.sort()
for i in a_list:
    if not binary_search(i): ab.append(i)

if len(ab) == 0: print(0)
else:
    print(len(ab))
    ab.sort()
    for i in ab: print(i, end=' ')