a=[0, 10, 10, 10, 12, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14, 14, 20]
b=[0, 10, 10, 10, 11, 11, 11, 11, 11, 13, 13, 13, 13, 13, 13, 13, 16]
c=[0, 9, 9, 9, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12, 12, 14]
d=[0, 8, 8, 8, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11, 11, 13]
class NhanVien:
    def __init__(self, ma, ten, luongcb, ngayc, heso):
        self.ma = ma
        self.ten = ten
        self.luongcb = luongcb
        self.ngayc = ngayc
        self.heso = heso

def getLoai(ma):
        return ma[0]
def get_nam(ma):
        return int(ma[1]) * 10 + int(ma[2])
def getpb(ma):
        return ma[3:]

m = []
phongban = {}
for t in range(int(input())):
      pb = input()
      phongban[pb[:2]] = pb[3:]
for t in range(int(input()))   :
    ma = input()
    ten = input()
    luongcb = int(input())
    ngayc = int(input())
    if getLoai(ma) == 'A':
        if get_nam(ma) > 15:
            heso = a[16]
        else:
            heso = a[get_nam(ma)]
    elif getLoai(ma) == 'B':
        if get_nam(ma) > 15:
            heso = b[16]
        else:
            heso = b[get_nam(ma)]
    elif getLoai(ma) == 'C':
        if get_nam(ma) > 15:
            heso = c[16]
        else:
            heso = c[get_nam(ma)]
    else:
        if get_nam(ma) > 15:
            heso = d[16]
        else:
            heso = d[get_nam(ma)]
    m.append(NhanVien(ma, ten, luongcb, ngayc, heso))
for i in m:
     print(i.ma, i.ten, phongban[getpb(i.ma)], i.heso * i.luongcb * i.ngayc * 1000)