n = int(input())
s = input()

if n % 2 == 1:
    s = s[:n//2] + s[n//2 + 1:]
#print(s)

cnt = [0 for i in range(26)]
for i in s:
    cnt[ord(i)-97] += 1

for i in cnt:
    if i % 2 == 1:
        print("No")
        exit()

print("Yes")