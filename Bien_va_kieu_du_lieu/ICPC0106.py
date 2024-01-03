import math

BASE = '0123456789ABCDEF'

def solve(substr):
    sum = 0
    for i in range(0, len(substr)):
        sum = sum + (2 ** i) * int(substr[i])
    return BASE[sum]
        
t = int(input())
while t > 0:
    n = int(input())
    k = int(math.log2(n))
    s = list(input())
    s.reverse()
    ans = ''
    for i in range(0, len(s), k):
        ans = solve(s[i: i + k]) + ans

    print(ans)
    t -= 1

