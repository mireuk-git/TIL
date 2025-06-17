# https://www.acmicpc.net/problem/1495
# 1495

n,s,m=map(int,input().split())
v=list(map(int,input().split()))
mat=[[0]*(m+1) for _ in range(n+1)]
mat[0][s]=1

for i in range(n):
    for j in range(m+1):
        if mat[i][j]!=0:
            if j-v[i]>=0:
                mat[i+1][j-v[i]]=1
            if j+v[i]<=m:
                mat[i+1][j+v[i]]=1

ans=-1
mat=mat[n]
for i in range(m,-1,-1):
    if mat[i]==1:
        ans=i
        break
print(ans)