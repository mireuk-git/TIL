# https://www.acmicpc.net/problem/25683
# 25683

import sys
input=sys.stdin.readline

n=int(input().strip())
r,c=[0]*n,[0]*n
for i in range(n):
    r[i],c[i]=map(int,input().strip().split())
s=0
for i in range(n-1,0,-1):
    s+=r[i]*c[i]*r[i-1]
    c[i-1]=c[i]
print(s)