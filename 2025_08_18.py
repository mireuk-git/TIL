# https://www.acmicpc.net/problem/12018
# 12018

n,m=map(int,input().split())
mil=[]
for _ in range(n):
    p,l=map(int,input().split())
    t=list(map(int,input().split()))
    if p>=l:
        t.sort(reverse=True)
        mil.append(t[l-1])
    else: mil.append(1)
mil.sort()
use,count=0,0
for cost in mil:
    if use+cost<=m:
        use+=cost
        count+=1
    else: break
print(count)