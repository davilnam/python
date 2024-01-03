from collections import Counter
for _ in range(int(input())):
    n, p, k = map(int, input().split())
    l1 = list(int(i) for i in input().split())
    l2 = list(int(i) for i in input().split())
    l3 = list(int(i) for i in input().split())
    i1, i2, i3, ok = 0, 0, 0, 0
    while i1 < n and i2 < p and i3 < k:
        # neu bang nhau thi in ra xong dong thoi tang len
        if l1[i1] == l2[i2] and l2[i2] == l3[i3]:
            print(l1[i1], end = " ")
            i1 += 1
            i2 += 1
            i3 += 1
            ok = 1
        elif l1[i1] < l2[i2]: i1 += 1
        elif l2[i2] < l3[i3]:
            i2 += 1
        elif l3[i3] < l1[i1]:
            i3 += 1
    if ok == 0:
        print('NO')
    else:
        print()