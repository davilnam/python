import math
t = int(input())
while t > 0:
    n, x, m = input().split()
    n = float(n)
    x = float(x)
    m = float(m)
    ans = int(math.log(m / n, 1 + x / 100))
    if (ans ** (1 + x / 100)) * n == m:
        print(ans)
    else:
        print(ans + 1)
    t -= 1