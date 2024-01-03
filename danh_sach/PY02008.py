n, x = [int(i) for i in input().split()]
prime = [1] * 10000
prime[0] = prime[1] = 0
def sang():
    for i in range(2, 101):
        if prime[i]:
            j = i * i
            while j < 10000:
                prime[j] = 0
                j += i
sang()
print(x, end=" ")
cnt = 0
for i in range(2, 10000):
    if prime[i]:
        cnt += 1
        x += i
        print(x, end=" ")
        if cnt == n:
            break
