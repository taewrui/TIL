from bisect import bisect_left, bisect_right
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()
for i in m_list:
    print(bisect_right(n_list, i) - bisect_left(n_list, i), end=' ')