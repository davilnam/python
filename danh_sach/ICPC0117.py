n = int(input())
my_list = []
while n > 0:
    s = input()
    my_list.append(s)
    n -= 1
my_list = list(set(my_list))
print(len(my_list))