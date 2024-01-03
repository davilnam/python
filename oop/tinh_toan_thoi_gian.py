class TinhToanThoiGian:
    def __init__(self, ma, ten, gioVao, gioRa):
        self.ma = ma
        self.ten = ten
        self.gioVao = gioVao
        self.gioRa = gioRa
    
    def tinhThoiGian(self):
        time1 = [int(i) for i in str(self.gioVao).split(':')]
        time2 = [int(i) for i in str(self.gioRa).split(':')]
        tg = time2[0] * 60 + time2[1] - time1[0] * 60 - time1[1]
        gio = tg // 60
        phut = tg % 60
        return f"{gio} gio {phut} phut"
    
    def tinhRaPhut(self):
        time1 = [int(i) for i in str(self.gioVao).split(':')]
        time2 = [int(i) for i in str(self.gioRa).split(':')]
        tg = time2[0] * 60 + time2[1] - time1[0] * 60 - time1[1]
        return tg

    def __str__(self):
        return f"{self.ma} {self.ten} {self.tinhThoiGian()}"    

t = int(input())
my_list = []
while t > 0:
    ma = input()
    ten = input()
    gioVao = input()
    gioRa = input()
    tttg = TinhToanThoiGian(ma, ten, gioVao, gioRa)
    my_list.append(tttg)
    t -= 1

def custom(tttg):
    return -tttg.tinhRaPhut()

my_list.sort(key=custom)
for i in my_list:
    print(i)