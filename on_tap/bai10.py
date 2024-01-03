file = open('CONTACT.txt', 'r')
lines = file.readlines()  # Đọc tất cả các dòng và lưu vào danh sách

myList = list()
for i in range(len(lines)):
    if i == len(lines) - 1:
        x = lines[i].lower()
    else:
        x = lines[i].lower()[:len(lines[i]) - 1]        
    myList.append(x)

myList = list(set(myList))

myList.sort()
for i in myList:
    print(i)