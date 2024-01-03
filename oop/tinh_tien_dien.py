bang_he_so = {
    'A': 100,
    'B': 500,
    'C': 200
}

def chuanHoaTen(s):
    res = str(s).strip().lower().split()
    ans = ""
    for i in res:
        ans += i.title() + " "

    return ans[:len(ans) - 1]

class HoaDonDien:
    def __init__(self, ma, ten, maHoGd, chiSoDau, chiSoCuoi):
        self.ma = f"KH{ma:02d}"
        self.ten = chuanHoaTen(ten)
        self.maHoGd = maHoGd
        self.chiSoDau = chiSoDau
        self.chiSoCuoi = chiSoCuoi

    def tinhTienVuotDinhMuc(self):
        soDien = self.chiSoCuoi - self.chiSoDau
        dinhMuc = bang_he_so[self.maHoGd]
        if soDien >= dinhMuc:
            return (soDien - dinhMuc) * 1000
        else:
            return 0
    
    def tinhTienTrongDinhMuc(self):
        soDien = self.chiSoCuoi - self.chiSoDau
        dinhMuc = bang_he_so[self.maHoGd]
        if soDien >= dinhMuc:
            return dinhMuc * 450
        else:
            return soDien * 450
    
    def tinhThueVat(self):
        return self.tinhTienVuotDinhMuc() * 5 // 100

    def tinhTienPhaiNop(self):
        return self.tinhThueVat() + self.tinhTienTrongDinhMuc() + self.tinhTienVuotDinhMuc()
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.tinhTienTrongDinhMuc()} {self.tinhTienVuotDinhMuc()} {self.tinhThueVat()} {self.tinhTienPhaiNop()}"



t = int(input())
my_list = []
for i in range(1, t + 1):
    ten = input()
    a = input().split()
    maHoGd, chiSoDau, chiSoCuoi = a[0], int(a[1]), int(a[2])
    hdd = HoaDonDien(i, ten, maHoGd, chiSoDau, chiSoCuoi)
    my_list.append(hdd)

def custom(hdd):
    return -hdd.tinhTienPhaiNop()

my_list.sort(key=custom)
for i in my_list:
    print(i)