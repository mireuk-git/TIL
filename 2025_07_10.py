# https://www.acmicpc.net/problem/23253
# 23253

import sys
input=sys.stdin.readline

n,m=map(int,input().split())
flag=True
for i in range(m):
    k=int(input())
    stack=list(map(int,input().split()))
    if flag:
        for j in range(k-1):
            if stack[j]<stack[j+1]:
                flag=False
                break
if flag: print("Yes")
else: print("No")