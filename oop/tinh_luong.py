he_so_luong = {
    'A': {
        '1-3': 10,
        '4-8': 12,
        '9-15': 14,
        '16-100': 20
    },
    'B': {
        '1-3': 10,
        '4-8': 11,
        '9-15': 13,
        '16-100': 16
    },
    'C': {
        '1-3': 9,
        '4-8': 10,
        '9-15': 12,
        '16-100': 14
    },
    'D': {
        '1-3': 8,
        '4-8': 9,
        '9-15': 11,
        '16-100': 13
    }
}

class NhanVien:
    def __init__(self, ma, ten, luongCoBan, soNgayCong, tenPhongBan):
        self.ma = ma
        self.ten = ten
        self.luongCoBan = luongCoBan
        self.soNgayCong = soNgayCong
        self.tenPhongBan = tenPhongBan

    def tinhTienLuong(self):
        nhom = self.ma[0]
        kinhNgiem = int(self.ma[1:3])
        tmp = ""
        if kinhNgiem <= 3:
            tmp = '1-3'
        elif kinhNgiem <= 8:
            tmp = '4-8'
        elif kinhNgiem <= 15:
            tmp = '9-15'
        else:
            tmp = '16-100'
        heSo = he_so_luong[nhom][tmp]
        return heSo * self.luongCoBan * self.soNgayCong * 1000
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.tenPhongBan} {self.tinhTienLuong()}"

n = int(input())
my_dict = dict()
for i in range(n):
    a = input().split()
    tenPhongBan = ""
    for j in range(1, len(a)):
        tenPhongBan += a[j] + " "        
    tenPhongBan = tenPhongBan[:len(tenPhongBan) - 1]
    my_dict[a[0]] = tenPhongBan

m = int(input())
my_list = []
for i in range(m):
    ma = input()
    ten = input()
    luongCoBan = int(input())
    soNgayCong = int(input())
    maPhongBan = ma[-2:]
    tenPhongBan = my_dict[maPhongBan]
    nv = NhanVien(ma, ten, luongCoBan, soNgayCong, tenPhongBan)
    my_list.append(nv)

for i in my_list:
    print(i)