file_A = open('Tep_tin/a.txt', 'r')
file_B = open('Tep_tin/b.txt', 'r')
lines_1 = file_A.readlines()  # Đọc tất cả các dòng và lưu vào danh sách
lines_2 = file_B.readlines()  # Đọc tất cả các dòng và lưu vào danh sách

for i in range(len(lines_1)):
    try:
        x = int(lines_1[i][:1])
        y = int(lines_2[i][:1])
        ans = x ** y
        print(ans)
    except ValueError:
        print("Oops! That was no valid number.")