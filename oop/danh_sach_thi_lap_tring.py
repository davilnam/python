class Nhom:
    def __init__(self, maNhom, tenNhom, tenTruong):
        self.maNhom = maNhom
        self.tenNhom = tenNhom
        self.tenTruong = tenTruong

class ThiSinh:
    def __init__(self, maTs, ten, nhom):
        self.maTs = f"C{maTs:03d}"
        self.ten = ten
        self.nhom = nhom

    def __str__(self):
        return f"{self.maTs} {self.ten} {self.nhom.tenNhom} {self.nhom.tenTruong}"
    
n = int(input())
my_dict = dict()
for i in range(1, n + 1):
    maNhom = f"Team{i:02d}"
    tenNhom = input()
    tenTruong = input()
    nhom = Nhom(maNhom, tenNhom, tenTruong)
    my_dict[maNhom] = nhom

m = int(input())
my_list = []
for i in range(1, m + 1):
    ten = input()
    maNhom = input()
    nhom = my_dict[maNhom]
    ts = ThiSinh(i, ten, nhom)
    my_list.append(ts)

def custom(ts):
    return ts.ten

my_list.sort(key=custom)
for i in my_list:
    print(i)

