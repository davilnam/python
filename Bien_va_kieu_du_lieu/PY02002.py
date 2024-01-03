t = int(input())
fibo = [0, 1, 1]

for i in range(3, 93):
    fibo.append(fibo[i - 1] + fibo[i - 2])

while t > 0:
    a, b = [int(i) for i in input().split()]
    for i in range(a, b + 1):
        print(fibo[i], end=" ")
    print()
    t -= 1