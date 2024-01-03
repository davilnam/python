import re

s = "Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin.muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep.moi    CAC BAN danG ky     thaM giA !"
arr = [
    "Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te",
    "co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin", 
    "muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep",
    "moi    CAC BAN danG ky     thaM giA "

]
regex = "[\w\s,:,]+"

# while True:
#     try:
#         pos = input()
#         if pos[len(pos) - 1] != '.' and pos[len(pos) - 1] != '!' and pos[len(pos) - 1] != '?':
#             pos += "."
#         s += pos
#         arr += re.findall(regex, pos)
#     except EOFError:
#         break

pos = []
k = -1
for i in arr:
    k += len(i) + 1
    pos.append(s[k])
ans = [x.strip() + y for x, y in zip(arr, pos)]

for i in ans:
    x = i.lower().split()
    x[0] = x[0].title()
    print(' '.join(x))