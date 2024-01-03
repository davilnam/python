def giaithua(n):
    if n == 1 or n == 0:
        return 1
    return n * giaithua(n - 1)

