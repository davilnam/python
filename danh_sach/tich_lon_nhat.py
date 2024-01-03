n = int(input())
l = [int(i) for i in input().split()]
l.sort()
m = max(l[0] * l[1], max(l[0] * l[1] * l[-1], max(l[-1] * l[-2], l[-1] * l[-2] * l[-3])))
print(m)