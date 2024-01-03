class SinhVien:
    def __init__(self, ma, ten, lop, diemChuyenCan = 0):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diemChuyenCan = diemChuyenCan

    def getStatus(self):
        if self.diemChuyenCan == 0:
            return " KDDK"
        else:
            return ""
    
    def __str__(self):
        return f"{self.ma} {self.ten} {self.lop} {self.diemChuyenCan}{self.getStatus()}"
    
    def setDiemChuyenCan(self, value):
        self.diemChuyenCan = value

my_list = []
t = int(input())
tmp = t
while t > 0:
    ma = input()
    ten = input()
    lop = input()
    sv = SinhVien(ma, ten, lop)
    my_list.append(sv)
    t -= 1
    
def getIndex(a, maSv):
    for i in range(len(a)):
        if a[i].ma == maSv:
            return i

def tinhDiem(s):
    res = 10
    for i in s:
        if i == 'm':
            res -= 1
        elif i == 'v':
            res -= 2
    if res <= 0:
        return 0
    else:
        return res

while tmp > 0:
    arr = input().split()
    index = getIndex(my_list, arr[0])
    diem = tinhDiem(arr[1])
    my_list[index].setDiemChuyenCan(diem)    
    tmp -= 1

for i in my_list:
    print(i)    
