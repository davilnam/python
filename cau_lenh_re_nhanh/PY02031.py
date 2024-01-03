def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

n, m = [int(i) for i in input().split()]
my_list = []
for i in range(n):
    list = [int(i) for i in input().split()]
    my_list.append(list)
for i in range(0,n):
    list = [int(nt(i)) for i in my_list[i]]    
    print(*list)


    