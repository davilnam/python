def degree(n, p):
    ans = 0
    i = p 
    while i <= n:
        ans += (n // i)
        i *= p
    return ans

t = int(input())
while t > 0:
    n, p = [int(i) for i in input().split()]
    res = degree(n, p)
    print(res)
    t -= 1