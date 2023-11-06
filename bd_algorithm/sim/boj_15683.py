def monitor(k):
    global monit_prev, monit

    # Base Condition : 모든 cctv 체크
        # 사각지대 카운트 결과 저장
        # return

    if k == len(cctv_type):
        cnt = 0
        for i in monit:
            cnt += i.count(False)
        blind.append(cnt)
        return

    # n번째 cctv
        #1번 방향
            # 체크 전 결과 저장
            # 방향과 cctv 종류에 따라 감시 체크
            # monitor(n+1)
            # 체크 전 결과로 되돌림
        #2번 방향
        #...

    t = cctv_type[k]
    f_name = "cctv_" + str(t)
    call_cctv = globals()[f_name]

    if t == 2 :
        dir = [[0, 1], [1, 0]]
    else:
        dir = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    
    
    for i in dir:
        monit_prev = monit
        call_cctv(i, k)
        monitor(k+1)
        monit = monit_prev

    #up, down, right, left
    
def cctv_1(dir, k):

    while True:
        move_r = cctv_index[k][0] + dir[0]
        move_c = cctv_index[k][1] + dir[1]
        if move_r < 0 or move_r >= n: break
        if move_c < 0 or move_c >= m: break
        if monit[move_r][move_c] == 6: break
        monit[move_r][move_c] = True

    return

def cctv_2(dir, k):

    while True:
        move_r = cctv_index[k][0] + dir[0]
        move_c = cctv_index[k][1] + dir[1]
        if move_r < 0 or move_r >= n: break
        if move_c < 0 or move_c >= m: break
        if monit[move_r][move_c] == 6: break
        monit[move_r][move_c] = True
    while True:
        move_r = cctv_index[k][0] - dir[0]
        move_c = cctv_index[k][1] - dir[1]
        if move_r < 0 or move_r >= n: break
        if move_c < 0 or move_c >= m: break
        if monit[move_r][move_c] == 6: break
        monit[move_r][move_c] = True
    return

def cctv_3(dir, k):

    while True:
        move_r = cctv_index[k][0] + dir[0]
        move_c = cctv_index[k][1] + dir[1]
        if move_r < 0 or move_r >= n: break
        if move_c < 0 or move_c >= m: break
        if monit[move_r][move_c] == 6: break
        monit[move_r][move_c] = True

    if dir[0] == 0 and dir[1] == -1: dir = [-1, 0]
    elif dir[0] == -1 and dir[1] == 0: dir = [0, 1]
    elif dir[0] == 0 and dir[1] == 1: dir = [1, 0]
    elif dir[0] == 1 and dir[1] == 0: dir = [0, -1]

    while True:
        move_r = cctv_index[k][0] + dir[0]
        move_c = cctv_index[k][1] + dir[1]
        if move_r < 0 or move_r >= n: break
        if move_c < 0 or move_c >= m: break
        if monit[move_r][move_c] == 6: break
        monit[move_r][move_c] = True

def cctv_4(dir, k):
    dir_list = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    for i in dir_list:
        if i[0] == dir[0] and i[1] == dir[1]: continue
        while True:
            move_r = cctv_index[k][0] + i[0]
            move_c = cctv_index[k][1] + i[1]
            if move_r < 0 or move_r >= n: break
            if move_c < 0 or move_c >= m: break
            if monit[move_r][move_c] == 6: break
            monit[move_r][move_c] = True

def cctv_5(dir, k):
    dir_list = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    for i in dir_list:
        
        while True:
            move_r = cctv_index[k][0] + i[0]
            move_c = cctv_index[k][1] + i[1]
            if move_r < 0 or move_r >= n: break
            if move_c < 0 or move_c >= m: break
            if monit[move_r][move_c] == 6: break
            monit[move_r][move_c] = True


n, m = map(int, input().split())
office = [list(map(int, input().split())) for i in range(n)]
monit_prev = [[False for j in range(m)] for i in range(n)]
monit = [[False for j in range(m)] for i in range(n)]

cctv_index = []
cctv_type = []
blind = []

for i, row in enumerate(office):
    for j, val in enumerate(row):
        if val >= 1 and val <= 5:
            cctv_type.append(val)
            cctv_index.append([i, j])

monitor(0)
min = n*m
for i in blind:
    if i < min: min = i

print(min)