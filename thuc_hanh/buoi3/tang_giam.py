def xl():
    T = int(input())
    for _ in range(T):
        n = int(input())

        a = []
        b = []
        for k in range(n):
            A= [float(x) for x in input().split()]
            a.append(A[0])
            b.append(A[1])
        f = [1] * n

        for i in range(n):
            for j in range(i):
                if a[i] > a[j] and b[i] < b[j]:
                    f[i] = max(f[i], f[j] + 1)

        print(max(f))

xl()