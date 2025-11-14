# https://www.acmicpc.net/problem/20222
# 20222
'''
n,k=map(int,input().split())
box = n//k
if n%k: box+=1
print(n//box)
'''
#https://www.acmicpc.net/problem/14430
# 14430

n,m = map(int,input().split())
mat = [[]]
for _ in range(n):
    mat.append([0]+list(map(int,input().split())))
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=max(dp[i-1][j],dp[i][j-1])+mat[i][j]
print(dp[n][m])