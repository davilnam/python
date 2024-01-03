from datetime import datetime
class LichThi:
    def __init__(self, maCaThi, maMon, ngayThi, gioThi, nhomThi, tenMon):
        self.maCaThi = f"T{maCaThi:03d}"
        self.maMon = maMon
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.nhomThi = nhomThi
        self.tenMon = tenMon
    
    def getNgay(self):
        return datetime.strptime(self.ngayThi, "%d/%m/%Y")

    def __str__(self):
        return f"{self.maCaThi} {self.maMon} {self.tenMon} {self.ngayThi} {self.gioThi} {self.nhomThi}"
    
n, m = [int(i) for i in input().split()]
my_dict = dict()
for i in range(n):
    maMon = input()
    tenMon = input()
    my_dict[maMon] = tenMon

my_list = []
for i in range(1, m + 1):
    a = input().split()
    tenMon = my_dict[a[0]]
    lt = LichThi(i, a[0], a[1], a[2], a[3], tenMon)
    my_list.append(lt)

def custom(lt):
    return (lt.getNgay(), lt.gioThi, lt.maMon)

my_list.sort(key = custom)

for i in my_list:
    print(i)



