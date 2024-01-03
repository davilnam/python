from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(int(i) for i in input().split())
    x = Counter(l)
    for i in x.items():
        if i[1] % 2 == 1:
            print(i[0])

