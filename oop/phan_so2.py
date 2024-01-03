import math
class PhanSo:
    def __init__(self, tu, mau):
        uc = math.gcd(tu, mau)
        self.tu = tu // uc
        self.mau = mau // uc

    def __str__(self):
        return f'{self.tu}/{self.mau}'
    
    def tong(self, other):
        tmp1 = self.tu * other.mau + self.mau * other.tu
        tmp2 = self.mau * other.mau
        return PhanSo(tmp1, tmp2)
    
arr = [int(i) for i in input().split()]
ps1 = PhanSo(arr[0], arr[1])
ps2 = PhanSo(arr[2], arr[3])
ps3 = ps1.tong(ps2)
print(ps3)

