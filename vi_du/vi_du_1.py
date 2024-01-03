# def isPangram(s):
#     a = [0] * 26
#     for i in s:
#         a[ord(i) - ord('a')] += 1
#     for i in a:
#         if i == 0:
#             return False
#     return True
# if isPangram(input().lower()):
#     print("YES")
# else:
#     print("NO")
import csv    
file = open('vi_du/addresses.csv', 'r')
reader = csv.reader(file)
myList = []
for row in reader:
    myList.append(row[4])

print(*myList)