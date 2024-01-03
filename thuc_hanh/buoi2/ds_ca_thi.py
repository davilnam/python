file = open("thuc_hanh/cathi.txt")


class CaThi:
    ma = "C"
    dem = 0
    def __init__(self, ngay, gio, phong):
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.kt_ngay_thi = ""

        if(len(self.gio) == 4):
            self.gio = "0" + self.gio
        if(self.ngay[1] == '/'):
            self.ngay = "0" + self.ngay
        if(self.ngay[4] == '/'):
            self.ngay = self.ngay[0:3] + "0" + self.ngay[3:]
        for i in str(self.ngay).split("/"):
            self.kt_ngay_thi = i + str(self.kt_ngay_thi)

        CaThi.dem += 1
        self.ma += (3 - len(str(self.dem))) * '0' + str(self.dem)


    def __str__(self):
        return f"{self.ma} {self.ngay} {self.gio} {self.phong}"


n = int(file.readline())
dsCaThi = []
while n > 0:
    dsCaThi.append(CaThi(file.readline().strip(), file.readline().strip(),file.readline().strip()))
    n -= 1

def solve(n):
    return (n.ngay, n.gio, n.ma)

dsCaThi.sort(key=solve)
for i in dsCaThi:
    print(i)
