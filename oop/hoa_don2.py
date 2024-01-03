from datetime import datetime

class KhachHang:
    def __init__(self, ma, ten, soPhong, ngayNhan, ngayTra, tienDichVu):        
        self.ma = f"KH{ma:02d}"
        self.ten = ten
        self.soPhong = soPhong
        self.ngayNhan = ngayNhan
        self.ngayTra = ngayTra
        self.tienDichVu = tienDichVu
        tang = soPhong // 100
        if tang == 1:
            self.gia = 25            
        elif tang == 2:
            self.gia = 34
        elif tang == 3:
            self.gia = 50
        elif tang == 4:
            self.gia = 80

    def tinhSoNgay(self):
        timeIn = datetime.strptime(self.ngayNhan, "%d/%m/%Y")
        timeOut = datetime.strptime(self.ngayTra, "%d/%m/%Y")
        return (timeOut - timeIn).days + 1
    
    def tinhTien(self):
        return self.gia * self.tinhSoNgay() + self.tienDichVu
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.soPhong} {self.tinhSoNgay()} {self.tinhTien()}"

my_list = []
t = int(input())

for i in range(1, t + 1):
    ten = input().strip()
    soPhong = int(input())
    ngayNhan = input().strip()
    ngayTra = input().strip()
    tienDichVu = int(input())
    kh = KhachHang(i, ten, soPhong, ngayNhan, ngayTra, tienDichVu)
    my_list.append(kh)    
    

def custom(kh):
    return -kh.tinhTien()

my_list.sort(key=custom)

for i in my_list:
    print(i)    
