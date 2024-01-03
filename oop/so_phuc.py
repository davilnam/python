class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    
    def tong(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)
    
    def tich(self, other):
        return SoPhuc(self.thuc * other.thuc - self.ao * other.ao, self.thuc * other.ao + self.ao * other.thuc)
    
    def __str__(self):
        if self.ao < 0:
            return f"{self.thuc} - {self.ao * (-1)}i"
        elif self.ao == 0:
            return f"{self.thuc}"
        else:
            return f"{self.thuc} + {self.ao}i"
        
t = int(input())
while t > 0:
    a = [int(i) for i in input().split()]    
    sp1 = SoPhuc(a[0], a[1])
    sp2 = SoPhuc(a[2], a[3])
    c = sp1.tong(sp2).tich(sp1)
    tmp = sp1.tong(sp2)
    d = tmp.tich(tmp)
    print(f"{c}, {d}")
    t -= 1

