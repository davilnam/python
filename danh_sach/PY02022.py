def nt(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return n > 1
n = int(input())
arr = [int(i) for i in input().split()]
myDict = {}
for i in arr:
    if nt(i):
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
for k, v in myDict.items():
    print(k, v)