class HoaDon:
    def __init__(self, ma, ten, chiSoCu, chiSoMoi):
        self.ma = f"KH{ma:02d}"
        self.ten = ten
        self.chiSoCu = chiSoCu
        self.chiSoMoi = chiSoMoi

    def tinhTongTien(self):
        soKhoi = self.chiSoMoi - self.chiSoCu                
        if soKhoi > 100:            
            return (50 * 100 + 50 * 150 + (soKhoi - 100) * 200) * 1.05
        elif soKhoi >= 51:
            return (50 * 100 + (soKhoi - 50) * 150) * 1.03            
        elif soKhoi >= 0:        
            return soKhoi * 100 * 1.02
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.tinhTongTien():.0f}"
    
t = int(input())
my_list = []
for i in range(1, t + 1):
    ten = input()
    chiSoCu = int(input())
    chiSoMoi = int(input())
    hd = HoaDon(i, ten, chiSoCu, chiSoMoi)
    my_list.append(hd)

def custom(hd):
    return -hd.tinhTongTien()

my_list.sort(key = custom)

for i in my_list:
    print(i)

