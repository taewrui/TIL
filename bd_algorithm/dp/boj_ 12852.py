n = int(input())
arr = []
track = [0, 0, 1, 1]

if n == 1:
    print("1")
    exit()

if n == 2 or n == 3:
    print(f"{n} 1")
    exit()



for i in range(n):
    prev_list = []
    if i == 0 or i == 1: 
        arr.append(0)
        continue
    if i % 2 == 0:
        prev_list.append(arr[i//2]+1)
    if i % 3 == 0:
        prev_list.append(arr[i//3]+1)
    prev_list.append(arr[i-1]+1)
    
    if i > 2:
        if prev_list[0] < prev_list[1] and prev_list[0] < prev_list[1]:
            arr.append(prev_list[0])
            track.append(i//2)
        elif prev_list[1] < prev_list[0] and prev_list[1] < prev_list[2]:
            arr.append(prev_list[1])
            track.append(i//3)
        else:
            arr.append(prev_list[2])
            track.append(i-1)
        

print(arr[-1])
print(n, end='')
for i in track.reverse():
    if track[i] == 0: break
    print(f" {track[i]}", end='')
