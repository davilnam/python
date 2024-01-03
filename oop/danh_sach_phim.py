from datetime import datetime
class Phim:
    def __init__(self, maPhim, maTheLoai, ngayKhoiChieu, tenPhim, soTap, theLoai):
        self.maPhim = f"P{maPhim:03d}"
        self.maTheLoai = maTheLoai
        self.ngayKhoiChieu = ngayKhoiChieu
        self.tenPhim = tenPhim
        self.soTap = soTap
        self.theLoai = theLoai

    def getNgay(self):
        return datetime.strptime(self.ngayKhoiChieu, "%d/%m/%Y")
    
    def __str__(self):
        return f"{self.maPhim} {self.theLoai} {self.ngayKhoiChieu} {self.tenPhim} {self.soTap}"
    
n, m = [int(i) for i in input().split()]
my_dict = dict()
for i in range(1, n + 1):
    ma = f"TL{i:03d}"
    my_dict[ma] = input()


my_list = []
for i in range(1, m + 1):
    maTheLoai = input()
    ngayKhoiChieu = input()
    tenPhim = input()
    soTap = int(input())
    p = Phim(i, maTheLoai, ngayKhoiChieu, tenPhim, soTap, my_dict[maTheLoai])
    my_list.append(p)

def custom(p):
    return (p.getNgay(), p.tenPhim, -p.soTap)

my_list.sort(key=custom)

for i in my_list:
    print(i)

    

