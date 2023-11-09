t = int(input())
cases = []

for i in range(t): cases.append(int(input()))


cnt = [[None, None] for i in range(max(cases)+1)]
cnt[0] = [1, 0]
if max(cases) > 0: cnt[1] = [0, 1]

if max(cases) > 1:
    for i in range(2, max(cases)+1):
        cnt[i][0] = cnt[i-1][0] + cnt[i-2][0]
        cnt[i][1] = cnt[i-1][1] + cnt[i-2][1]

for i in cases:
    print(f"{cnt[i][0]} {cnt[i][1]}")
