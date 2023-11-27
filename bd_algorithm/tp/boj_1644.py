n = int(input())
if n == 1:
    print(0)
    exit()
    
prime_num = []
for i in range(2, n+1):
    isPrime = True
    for j in range(1, i):
        if j != 1 and i % j == 0:
            isPrime = False
    if isPrime:
        prime_num.append(i)


cnt = 0
length = len(prime_num)
for i_idx, i in enumerate(prime_num):
    subtotal = 0
    j = i_idx
    while j < length and subtotal <= n:
        subtotal += prime_num[j]
        if n == subtotal:
            cnt += 1
            break
        j += 1
    
        
            
print(cnt)