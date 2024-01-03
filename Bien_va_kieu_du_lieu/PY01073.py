check = [0] * 1000
a = [0] * 1000

s = input()
n = len(s)

def xuat():
    for i in range(1, n + 1):
        print(s[a[i] - 1], end="")
    print()

def Try(i):
    for j in range(1, n + 1):
        if check[j] == 0:
            check[j] = 1
            a[i] = j 
            if i == n:
                xuat()
            else:
                Try(i + 1)
            check[j] = 0
        
Try(1)