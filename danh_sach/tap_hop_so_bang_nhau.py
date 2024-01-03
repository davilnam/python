n, m = map(int, input().split())
l1 = set(int(i) for i in input().split())
l2 = set(int(i) for i in input().split())
if len(l1) != len(l2):
    print('NO')
else:
    l3 = l1 - l2
    if len(l3) != 0:
        print('NO')
    else:
        print('YES')


