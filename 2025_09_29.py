# https://www.acmicpc.net/problem/2799
# 2799

import sys
input=sys.stdin.readline

m,n = map(int,input().strip().split())
input()
count=[0]*5
for _ in range(m):
    windows=[0]*n
    for i in range(4):
        line=input().strip()
        for j in range(n):
            if line[j*5+1]=='*': windows[j]+=1
    input()
    for i in range(n):
        count[windows[i]]+=1
for i in count: print(i,end=' ')
