# https://www.acmicpc.net/problem/5567
# 5567
'''
n=int(input())
m=int(input())
mat=[[-1]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    mat[a][b],mat[b][a]=1,1

l=[]
for i in range(1,n+1):
    if mat[1][i]==1:
        l.append(i)
        for j in range(2,n+1):
            if mat[i][j]==1: l.append(j)
l=set(l)
print(len(l))
'''
# https://www.acmicpc.net/problem/14620
# 14620

n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]

l=[float('inf')]*3
for i in range(1,n-1):
    for j in range(1,n-1):
        cost=sum(mat[i][j-1:j+2])+mat[i-1][j]+mat[i+1][j]
        if cost<l[-1]:
            l[-1]=cost
            print(f"({i},{j}) cost:{cost}")
            l.sort()

print(sum(l))