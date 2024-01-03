from datetime import datetime


class ThiSinh:
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = ten
        self.ns = self.chuanHoa(ns)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def chuanHoa(self, ngay_sinh):
        ch = datetime.strptime(ngay_sinh, "%d/%m/%Y")
        # Sử dụng strftime để định dạng lại chuỗi
        return ch.strftime("%d/%m/%Y")

    def tongDiem(self):
        return self.d1 + self.d2 + self.d3

    def __str__(self):
        return f"{self.ten} {self.ns} {self.tongDiem():.1f}"


ten = input()
ns = input()
d1 = float(input())
d2 = float(input())
d3 = float(input())

ts = ThiSinh(ten, ns, d1, d2, d3)
print(ts)
