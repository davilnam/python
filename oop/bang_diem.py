class ThiSinh:
    def __init__(self, ma, ten, arr):
        self.ma = f"HS{ma:02d}"
        self.ten = ten
        self.arr = arr
    
    def tinhTb(self):    
        tong = sum(self.arr) + self.arr[0] + self.arr[1]
        return tong / 10 / 1.2
    
    def getHocLuc(self):
        tb = self.tinhTb()
        if tb >= 9:
            return "XUAT SAC"
        elif tb >= 8:
            return "GIOI"
        elif tb >= 7:
            return "KHA"
        elif tb >= 5:
            return "TB"
        else:
            return "YEU"
        
    def __str__(self):
        return f"{self.ma} {self.ten} {self.tinhTb():.1f} {self.getHocLuc()}"
    
t = int(input())
my_list = []
for i in range(1, t + 1):
    ten = input()
    arr = [float(i) for i in input().split()]
    ts = ThiSinh(i, ten, arr)
    my_list.append(ts)

def custom(ts):
    return (-ts.tinhTb(), ts.ma)    

my_list.sort(key = custom)
for i in my_list:
    print(i)
