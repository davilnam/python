def chuanHoaTen(s):
    res = str(s).strip().lower().split()
    ans = ""
    for i in res:
        ans += i.title() + " "

    return ans[:len(ans) - 1]


class ThiSinh:
    def __init__(self, ma, ten, diem, danToc, khuVuc):
        self.ma = f"TS{ma:02d}"
        self.ten = chuanHoaTen(ten)
        self.diem = diem
        self.danToc = danToc
        self.khuVuc = khuVuc

    def tinhTongDiem(self):
        diemCong = 0
        if self.danToc == 'Kinh':
            diemCong += 0
        else:
            diemCong += 1.5
        if self.khuVuc == 1:
            diemCong += 1.5
        elif self.khuVuc == 2:
            diemCong += 1.0
        elif self.khuVuc == 3:
            diemCong += 0
        return self.diem + diemCong

    def getStatus(self):
        if self.tinhTongDiem() >= 20.5:
            return "Do"
        else:
            return "Truot"

    def __str__(self):
        return f"{self.ma} {self.ten} {self.tinhTongDiem():.1f} {self.getStatus()}"


t = int(input())
my_list = []
for i in range(1, t + 1):
    ten = input()
    diem = float(input())
    danToc = input()
    khuVuc = int(input())
    ts = ThiSinh(i, ten, diem, danToc, khuVuc)
    my_list.append(ts)


def custom(ts):
    return (-ts.tinhTongDiem(), ts.ma)


my_list.sort(key=custom)
for i in my_list:
    print(i)
