import math

BASE = '0123456789ABCDEF'
def tong(s):    
    res = 0
    for i in range(len(s)):
        res += int(s[i]) * (2 ** i) 
    return BASE[res]

def solve(s, b):
    k = int(math.log(b, 2))
    s = s[::-1]
    res = ""
    for i in range(0, len(s), k):
        res += str(tong(s[i:i+k]))
    return res[::-1]

t = int(input())
while t > 0:
    b = int(input())
    s = input()
    res = solve(s, b)
    print(res)
    t -= 0