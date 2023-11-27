def binarysearch(t):
    st = 0
    en = n-1
    
    while(st <= en):
        
        mid = (st + en) // 2
        if t == n_list[mid]:
            return 1
        elif t > n_list[mid]:
            st = mid + 1
        else:
            en = mid - 1
    return 0
     
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()
for i in m_list:
    print(binarysearch(i))