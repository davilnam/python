import math

def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

t = int(input())
while t > 0:
    x, y = input().split()
    ucln = math.gcd(int(x), int(y))
    sum = 0
    for i in str(ucln):
        sum += int(i)
    if nt(sum):
        print("YES")
    else:
        print("NO")
    t -= 1
