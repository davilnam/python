class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
    
    def tich(self):
        for i in range(self.n):            
            for j in range(self.n):
                tong = 0
                for k in range(self.m):
                    tong += self.a[i][k] * self.a[j][k]
                print(tong, end=" ")
            print()


t = int(input())
while t > 0:
    n, m = [int(i) for i in input().split()]
    a = []
    for i in range(n):
        tmp = [int(j) for j in input().split()]
        a.append(tmp)
    matrix = Matrix(n, m, a)
    matrix.tich()
    t -= 1
