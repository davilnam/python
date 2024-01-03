class ThiSinh:    
    def __init__(self,ma, ten, diem, dt, kv):        
        self.ma = format(ma, '02d')
        self.ma = "TS" + self.ma
        self.ten = ten
        self.diem = diem
        self.dt = dt
        self.kv = kv
    
    def chuan_hoa(self):
        tmp = self.ten.split()
        self.ten = ' '.join(tmp).title()
    def get_kv(self):
        return self.kv
    def get_dt(self):
        return self.dt
    def infor(self):
        kv = self.get_kv()
        if kv == 1:
            self.diem += 1.5
        if kv == 2:
            self.diem += 1
        dt = self.get_dt()
        if dt == "Kinh":
            self.diem += 0
        else:
            self.diem += 1.5

    def out(self):
        print(self.ma + " " + self.ten + " " + "%.1f"%self.diem, end=" ")
        if(self.diem >= 20.5):
            print("Do")
        else:
            print("Truot")
    def getMa(self):
        return self.ma
    def getDiem(self):
        return self.diem            
        

n = int(input())
a = []
for i in range(n):
    t = ThiSinh(i + 1, input(), float(input()), input(), int(input()))
    t.chuan_hoa()
    t.infor()
    a.append(t)
a.sort(key=lambda x: (-x.getDiem(), x.getMa()))
for x in a:
    x.out()      

    def __str__(self):
        return f"{self.ma} {self.ten} {self.diem} {self.do}"
