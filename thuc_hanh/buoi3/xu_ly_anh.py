import math

t = int(input())
while t > 0:
    n , m , l = map(int, input().split())
    save = []
    save.append([[0] * (m + 1)])
    pos = [[0] * (m + 1)]
    for i in range(0, n):
        res = list(map(int,input().split()))
        save.append([0] + res)
        pos.append([0] + res)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pos[i][j] = save[i][j] + pos[i - 1][j] + pos[i][j - 1] - pos[i - 1][j - 1]

    for i in range(1, n - l + 2):
        for j in range(1, m - l + 2):
            print(math.floor((pos[i + l - 1][j + l - 1] - pos[i + l - 1][j - 1] - pos[i - 1][j + l- 1] + pos[i - 1][j - 1]) / (l *l)), end=" ")
        print()

    t -= 1


