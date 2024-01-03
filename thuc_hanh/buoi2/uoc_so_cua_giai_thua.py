def degree(n, p):
    ans = 0
    i = p
    while i <= n:
        tmp = i
        while tmp % p == 0:
            ans += 1
            tmp //= p
        i += p 
    return ans   

t = int(input())
while t > 0:
    n, p = [int(i) for i in input().split()]
    ans = degree(n, p)
    print(ans)
    t -= 1