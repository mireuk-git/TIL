# https://www.acmicpc.net/problem/30189
# 30189

n,m = map(int,input().split())
r=0
f=1
for s in range(min(n,m)+1):
    r+=f
    f+=1
f-=1
for s in range(min(n,m)+1,max(n,m)+1):
    r+=f
f-=1
for s in range(max(n,m)+1,n+m+1):
    r+=f
    f-=1
print(r)

