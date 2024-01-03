def first_pos(a, l, r, value):
    res = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == value:
            res = m
            r = m - 1
        elif a[m] > value:
            r = m - 1
        else:
            l = m + 1
    return res

def last_pos(a, l, r, value):
    res = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] == value:
            res = m
            l = m + 1
        elif a[m] > value:
            r = m - 1
        else:
            l = m + 1
    return res




t = int(input())
while t > 0:
    n = int(input())
    a = [int(i) for i in input().split()]
    res = 0
    a.sort()
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            tmp = a[i] + a[j]
            f_index = first_pos(a, j + 1, n - 1, 0 - tmp)
            l_index = last_pos(a, j + 1, n - 1, 0 - tmp)
            if f_index != -1:
                res = res + (l_index - f_index + 1)
    print(res)
    t -= 1