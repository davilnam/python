mySet = set()
def Try(j, s, str):
    for i in range(1, n + 1):
        s += chr(96 + i)
        if(j == n):
            mySet.add(s + str)
            mySet.add(str + s)
        else:
            Try(j + 1, s, str)



for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    s = input()
    k = n - len(s)
    Try(1, "", s)
    res = len(mySet) % m
    print(res)
    mySet.clear()
    