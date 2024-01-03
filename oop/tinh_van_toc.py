class ThiSinh:
    def __init__(self, ten, donVi, tg):        
        self.ten = ten
        self.donVi = donVi
        self.tg = tg
        
    def getMa(self):
        a = str(self.ten).split()
        b = str(self.donVi).split()
        res = ""
        for i in b:
            res += i[0].upper()
        for i in a:
            res += i[0].upper()
        return res
    
    def tinhVanToc(self):
        time = [int(i) for i in str(self.tg).split(':')]
        gio = time[0] - 6 + time[1] / 60
        vanToc = 120 / gio
        return vanToc
    
    def __str__(self):
        return f"{self.getMa()} {self.ten} {self.donVi} {self.tinhVanToc():.0f} Km/h"
    
my_list = []
t = int(input())

for i in range(1, t + 1):
    ten = input().strip()
    donVi = input().strip()
    tg = input().strip()
    ts = ThiSinh(ten, donVi, tg)
    my_list.append(ts)    
    

def custom(ts):
    return -ts.tinhVanToc()

my_list.sort(key=custom)

for i in my_list:
    print(i)    
