from collections import defaultdict,deque

def check(g,ind):
    queue=deque()
    result=[]

    for j in g:
        if ind[j]==0:
            queue.append(j)

    while queue:
        cur=queue.popleft()
        result.append(cur)
        for nei in g[cur]:
            ind[nei] -= 1
            if ind[nei]==0:
                queue.append(nei)
    return result
n=int(input())
dep=defaultdict(list)
ind=defaultdict(int)
for t in range(n):
    com=input().split()
    n1,op,n2=com[0],com[1],com[2]

    if op==">":
        dep[n2].append(n1)
        ind[n1]+=1
    elif op=="<":
        dep[n1].append(n2)
        ind[n2]+=1

sort_ord=check(dep,ind)

if len(sort_ord)==len(dep):
    print("possible")
else:
    print("impossible")