n, m = map(int, input().split())
l1 = set(int(i) for i in input().split())
l2 = set(int(i) for i in input().split())
l3 = list(l1 & l2)
l3.sort()
print(*l3)
l3 = list(l1 - l2)
l3.sort()
print(*l3)
l3 = list(l2 - l1)
l3.sort()
print(*l3)


