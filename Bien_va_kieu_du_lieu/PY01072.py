n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a = sorted(list(set(a)))
n = len(a)

b = [0] * 1005

def xuat():
    for i in range(1, k + 1):
        print(a[b[i] - 1], end=" ")
    print()

def Try(i):
    for j in range(b[i - 1] + 1, n - k + i + 1):
        b[i] = j
        if i == k:
            xuat()
        else:
            Try(i + 1)

Try(1)


