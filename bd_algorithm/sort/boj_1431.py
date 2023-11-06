def sort_condition(num):
    total = 0
    num = str(num)
    for i in num:
        if i.isdigit(): total += int(i)

    return len(num), total, num

n = int(input())
serial = []
for i in range(n):
    serial.append(input())

serial.sort(key=sort_condition)

for i in serial: print(i)