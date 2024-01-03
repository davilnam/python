class NhanVien:
    def __init__(self, ma, ten, d1, d2):
        self.ma = f"TS0{ma}" 
        self.ten = ten
        self.d1 = d1
        self.d2 = d2
    
    def tinhTb(self):
        return (self.d1 + self.d2) / 2
    
    def getTrangThai(self):
        tb = self.tinhTb()
        if tb < 5:
            return "TRUOT"
        elif tb < 8:
            return "CAN NHAC"
        elif tb < 9.5:
            return "DAT"
        else:
            return "XUAT SAC"   

    def __str__(self):
        return f"{self.ma} {self.ten} {self.tinhTb():.2f} {self.getTrangThai()}"

t = int(input()) 
my_list = []
for i in range(1, t + 1):
    ten = input()
    d1 = float(input())
    if d1 > 10:
        d1 = d1 / 10
    d2 = float(input())
    if d2 > 10:
        d2 = d2 / 10
    nv = NhanVien(i, ten, d1, d2)
    my_list.append(nv)

def custom(nv):
    return -nv.tinhTb()

my_list.sort(key = custom)
for i in my_list:
    print(i)