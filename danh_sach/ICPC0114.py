def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1
t = int(input())
a = [2, 3, 5, 7]
while t > 0:
    s = input()
    s_rv = s[::-1]
    tmp = [int(i) for i in s]
    tmp1 = [i for i in tmp if i in a]
    tong = sum(tmp)
    if nt(int(s)) and nt(int(s_rv)) and nt(tong) and len(tmp1) == len(tmp):
        print("Yes")
    else:
        print("No")
    t -= 1