t = int(input())
while t > 0:
    n = int(input())
    cnt = 0
    while n % 7 != 0 and cnt <= 1000:
        cnt += 1
        tmp = str(n)
        n = n + int(tmp[::-1])
    if cnt == 1000:
        print(-1)
    else:
        print(n)
    t -= 1