class GiangVien:
    def __init__(self, maGv, ten, maXetTuyen, diemTin, diemChuyenMon):
        self.maGv = f"GV{maGv:02d}"
        self.ten = ten
        self.maXetTuyen = maXetTuyen
        self.diemTin = diemTin
        self.diemChuyenMon = diemChuyenMon
        
    def getMon(self):
        maMon = self.maXetTuyen[0]
        if maMon == 'A':
            return "TOAN"
        if maMon == 'B':
            return "LY"
        if maMon == 'C':
            return "HOA"
        
    def tinhDiem(self):
        maUuTien = self.maXetTuyen[1]
        if maUuTien == '1':
            return self.diemTin * 2 + self.diemChuyenMon + 2.0
        elif maUuTien == '2':
            return self.diemTin * 2 + self.diemChuyenMon + 1.5
        elif maUuTien == '3':
            return self.diemTin * 2 + self.diemChuyenMon + 1.0
        elif maUuTien == '4':
            return self.diemTin * 2 + self.diemChuyenMon
    
    
    def getStatus(self):
        tongDiem = self.tinhDiem()
        if tongDiem >= 18.0:
            return "TRUNG TUYEN"
        else:
            return "LOAI"
        
    def __str__(self):
        return f"{self.maGv} {self.ten} {self.getMon()} {self.tinhDiem():.1f} {self.getStatus()}"
    
my_list = []    
t = int(input())
for i in range(1, t + 1):
    ten = input()
    maXetTuyen = input()
    diemTin = float(input())
    diemChuyenMon = float(input())
    gv = GiangVien(i, ten, maXetTuyen, diemTin, diemChuyenMon)
    my_list.append(gv)

def custom(gv):
    return -gv.tinhDiem()

my_list.sort(key=custom)
for i in my_list:
    print(i)