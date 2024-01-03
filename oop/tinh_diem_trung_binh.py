import math

def chuanHoaTen(s):
    res = str(s).strip().lower().split()
    ans = ""
    for i in res:
        ans += i.title() + " "

    return ans[:len(ans) - 1]


class ThiSinh:
    def __init__(self, ma, ten, d1, d2, d3, thuHang=1):
        self.ma = f"SV{ma:02d}"
        self.ten = chuanHoaTen(ten)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.thuHang = thuHang

    def tinhDiemTb(self):
        tb = (self.d1 * 3 + self.d2 * 3 + self.d3 * 2) / 8  
        return tb    
    
    def setThuHang(self, value):
        self.thuHang = value

    def __str__(self):
        return f"{self.ma} {self.ten} {(math.ceil(self.tinhDiemTb() * 100) / 100):.2f} {self.thuHang}"



t = int(input())
my_list = []
for i in range(1, t + 1):
    ten = input()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    ts = ThiSinh(i, ten, d1, d2, d3)
    my_list.append(ts)


def custom(ts):
    return (-ts.tinhDiemTb(), ts.ma)

my_list.sort(key=custom)
cnt = 0
tmp = 1
diem = my_list[0].tinhDiemTb()
for i in my_list:
    if i.tinhDiemTb() == diem:
        cnt += 1
    else:
        tmp += cnt
        diem = i.tinhDiemTb()
        cnt = 1
    i.setThuHang(tmp)

for i in my_list:
    print(i)