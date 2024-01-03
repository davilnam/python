
class TinhToanLuongMua:
    def __init__(self, i, tenTram, thoiGian, luongMuaDoDuoc):
        self.ma = f"T{i:02d}"
        self.tenTram = tenTram
        self.thoiGian = thoiGian        
        self.luongMuaDoDuoc = luongMuaDoDuoc

    def tinhLuongMuaTrungBinh(self):
        return self.luongMuaDoDuoc / self.thoiGian * 60
    
    def __str__(self):
        return f"{self.ma} {self.tenTram} {self.tinhLuongMuaTrungBinh():.2f}"


def tinhThoiGian(thoiGianBd, thoiGianKt):
        time1 = [int(i) for i in thoiGianBd.split(":")]
        time2 = [int(i) for i in thoiGianKt.split(":")]
        return time2[0] * 60 + time2[1] - time1[0] * 60 - time1[1]
    
def get_index(arr, ten):
    for i in range(len(arr)):
        if arr[i].tenTram == ten:
            return i

    
t = int(input())
list_ten_tram = []
my_list = []
cnt = 0
while t > 0:
    ten = input()
    thoiGianBd = input()
    thoiGiankt = input()
    thoiGian = tinhThoiGian(thoiGianBd, thoiGiankt)
    luongMuaDoDuoc = int(input())
    if list_ten_tram.count(ten) == 0:
        list_ten_tram.append(ten)
        cnt += 1
        ttlm = TinhToanLuongMua(cnt, ten, thoiGian, luongMuaDoDuoc)
        my_list.append(ttlm)
    else:
        index = get_index(my_list, ten)        
        tmp = my_list[index]
        ma = int(tmp.ma[2:])
        my_list.pop(index)
        my_list.append(TinhToanLuongMua(ma, ten, tmp.thoiGian + thoiGian, luongMuaDoDuoc + tmp.luongMuaDoDuoc))
    t -= 1

def custom(ttlm):
    return ttlm.ma
my_list.sort(key = custom)
for i in my_list:
    print(i)