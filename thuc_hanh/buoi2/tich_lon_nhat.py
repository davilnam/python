n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
a = arr[0] * arr[1] * arr[-1]
b = arr[-1] * arr[-2] * arr[-3]
c = arr[-1] * arr[-2]
d = arr[0] * arr[1]
res = max(a, b, c, d)
print(res)