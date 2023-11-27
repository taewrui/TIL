def binary_search(n):
    st = 0
    en = len(n_list) - 1
    while st <= en:
        mid = (st + en) // 2
        if n_list[mid] == n:
            return True
        elif n_list[mid] > n:
            en = mid - 1
        else:
            st = mid + 1
    return False

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()
for i in m_list:
    if binary_search(i): print(1, end=' ')
    else: print(0, end=' ')

