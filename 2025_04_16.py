# https://www.acmicpc.net/problem/6246
# 6246

n,q=map(int,input().split())
slots=[False]*n
for _ in range(q):
    l,i=map(int,input().split())
    for j in range(l-1,n,i):
        if not slots[j]: slots[j]=True
print(n-sum(slots))
