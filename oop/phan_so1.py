import math
class PhanSo:
    def __init__(self, tu, mau):
        uc = math.gcd(tu, mau)
        self.tu = tu // uc
        self.mau = mau // uc
    def __str__(self):
        return f'{self.tu}/{self.mau}'
    
arr = [int(i) for i in input().split()]
ps = PhanSo(arr[0], arr[1])
print(ps)
