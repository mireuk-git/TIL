# https://www.acmicpc.net/problem/31670
# 31670

import sys
input=sys.stdin.readline

n=int(input())
r=list(map(int,input().split()))

dp=[[0,0] for _ in range(n)]
dp[0]=[0,r[0]]
for i in range(1,n):
    dp[i]=[dp[i-1][1], min(dp[i-1])+r[i]]
print(min(dp[-1]))