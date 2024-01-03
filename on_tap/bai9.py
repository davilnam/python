n = int(1e6)
prime = [1] * n

def sang():
    i = 2
    while i * i <= n:
        if prime[i] == 1:
            for j in range(i ** 2, n, i):
                prime[j] = 0
        i += 1

sang()

t = int(input())

while t > 0:
    n = int(input())    
    check = []
    for i in range(13, n):
        tmp = str(i)
        dao = int(tmp[::-1])
        if dao < n:
            if prime[i] == 1 and prime[dao] == 1 and i != dao and (i not in check) and (dao not in check):
                check.append(i)
                check.append(dao)
                print(i, dao, end=" ")
    print()
    t -= 1

