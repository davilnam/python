def min_sum_seq(a):
    n = len(a)
    b = [0] * n
    b[0] = 1
    for i in range(1, n):
        b[i] = (a[i] * b[i - 1]) // a[i - 1]

    min_sum = sum(b)
    return min_sum
n = int(input())
a = [int(i) for i in input().split()]
rs = min_sum_seq(a)
print(rs)