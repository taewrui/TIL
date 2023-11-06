a, b, m = map(int, input().split())
pow(a, b, m)
# a^b를 m으로 나눈 나머지를 구해라.

def pow(a, b, m):

    if b == 1: return a % m
    val = pow(a, b/2, m)
    val = (val ** 2) % m
    if b%2 == 0: return val
    else: return (val * a) % b