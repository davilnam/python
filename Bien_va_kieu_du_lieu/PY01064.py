t = int(input())
while t > 0:
    n, k = [int(i) for i in input().split()]
    while n != 1:
        if k == 2 ** (n - 1):
            break
        elif k < 2 ** (n - 1):
            n -= 1
        else:
            k = k - 2 ** (n - 1)
            n = n - 1
    print(chr(64 + n))
    t -= 1