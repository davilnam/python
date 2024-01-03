#1 Tao list
#c1
myList = [1, 2, "nam", None, True, False]
#c2 dung ham tao list()
# thisList = list((1, 3, 4, "Dien"))

# print(thisList)

#2 access elements: truy cap den gia tri trong list
# list co index danh tu 0
# print(myList[0]) # 1
# print(myList[-1]) # False

# method index(value) tra ve vi tri cua value
# print(myList.index("nam"))

# method count(value) tra ve so lan xuat hien cua value trong list
# print(myList.count(10)) # 0 vi ko co 10 trong myList

#3 duyet list
for item in myList:
    print(item, end=" ")

'''
    enumerate(iterable, start=0)
    iterable: Dãy dữ liệu bạn muốn lặp qua.
    start: Giá trị bắt đầu của chỉ số. Mặc định là 0.
'''

presidents = ['nam', 'dien', 'hoang', 'phu', 'Anh']

for index, president in enumerate(presidents):
    print(f"President #{index}: {president}")

#4 Slicing 
# syntax list[start:end:step] #step: mac dinh la 1

print(presidents[::2]) # ['nam', 'hoang', 'Anh']
print(presidents[::-1]) # ['Anh', 'phu', 'hoang', 'dien', 'nam']


#5 method in list
#Add to list
#c1 dung toan tu * hoac +
print(myList*2) # [1, 2, 'nam', None, True, False, 1, 2, 'nam', None, True, False]
print(myList + ["3", 4]) # [1, 2, 'nam', None, True, False, '3', 4]
#c2 dung method append(value) giup them 1 gia tri vao cuoi list
myList.append(3)
print(myList) # [1, 2, 'nam', None, True, False, 3]
#c3 dung method insert(index, value) giup them value vao vi tri index chi dinh
myList.insert(1, "Pho")
print(myList) # [1, 'Pho', 2, 'nam', None, True, False, 3]

#Remove from list
#c1 dung ham pop(index) mac dinh neu ko truyen tham so index thi xoa phan tu cuoi trong list
#c2 dung ham remove(value) xoa value di trong list (Chu y chi xoa gia tri dau)
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry', 'banana']
#c3 The del keyword also removes the specified index:
del thislist[0]
print(thislist) # ['cherry', 'banana']

#c4 method clear() giup xoa tat ca cac phan tu trong list
thislist.clear()
print(thislist) # []

#6 Sorting
thislist = [1, 3, 2, 0, 5]
thislist.sort() # mac dinh se la sap xep tang dan
print(thislist) # [0, 1, 2, 3, 5]
thislist.sort(reverse=True) # sap xep giam dan
print(thislist) # [5, 3, 2, 1, 0]

#customize sort function su dung arg key = function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist) # [50, 65, 23, 82, 100]

#7 1 so method thong ke
my_list = [1, 3, 2, 5, 4, 8]
print(max(my_list)) # 8
print(min(my_list)) # 1
print(sum(my_list)) # 23


def palindrome(s):
    s = s.lower().strip()
    ans = ""
    for i in s:
        if i.isalpha():
            ans += i
    return ans == ans[::-1]

s = "A man, a plan, a  canal: Panama"
if palindrome(s):
    print("YES")
else:
    print("NO")
    