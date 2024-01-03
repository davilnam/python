tmp = []
cnt = 10
while cnt != 0:
    a = [int(i) % 42 for i in input().split()]
    cnt -= len(a)
    tmp += a
tmp = list(set(tmp))
print(len(tmp))
