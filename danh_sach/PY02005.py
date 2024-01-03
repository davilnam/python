n = int(input())
a = [int(i) for i in input().split()]
cnt = 0
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            cnt += 1
print(cnt)