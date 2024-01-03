import math

BASE = '0123456789ABCDEF'

def solve(substr):
    sum = 0
    for i in range(0, len(substr)):
        sum = sum + (2 ** i) * int(substr[i])
    return BASE[sum]
        

s = list(input())
s.reverse()
k = 3
ans = ''
for i in range(0, len(s), k):
    ans = solve(s[i: i + k]) + ans

print(ans)


