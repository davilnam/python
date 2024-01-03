import math
def nt(n):

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
while t > 0:
    n = int(input())
    cnt = 0
    for i in range(1,n):
        if math.gcd(i, n) == 1:
            cnt += 1
    if nt(cnt):
        print("YES")
    else:
        print("NO")
    t -= 1
