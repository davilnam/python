class HoaDon:
    def __init__(self, ma, ten, soLuong, donGia, tienChietKhau):
        self.ma = ma
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.tienChietKhau = tienChietKhau

    def tinhTongTien(self):
        return self.soLuong * self.donGia - self.tienChietKhau
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.soLuong} {self.donGia} {self.tienChietKhau} {self.tinhTongTien()}"
    
t = int(input())
my_list = []
while t > 0:
    ma = input()
    ten = input()
    soLuong = int(input())
    donGia = int(input())
    tienChietKhau = int(input())
    hd = HoaDon(ma, ten, soLuong, donGia, tienChietKhau)
    my_list.append(hd)
    t -= 1

def custom(hd):
    return -hd.tinhTongTien()

my_list.sort(key=custom)

for i in my_list:
    print(i) 
