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
    cnt = 0
    for i in range(2, n - 5):
        if prime[i] == 1 and prime[i + 6]:
            if prime[i + 2] == 1 or prime[i + 4] == 1:
                cnt += 1
    print(cnt)
    t -= 1

