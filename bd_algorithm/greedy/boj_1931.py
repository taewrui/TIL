n = int(input())
time = []
for i in range(n): time.append(list(map(int, input().split())))

time.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for i in time:
    if end_time <= i[0]:
        cnt += 1
        end_time = i[1]
print(cnt)