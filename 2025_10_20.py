# https://www.acmicpc.net/problem/26123
# 26123
'''
import sys
input=sys.stdin.readline

n,d = map(int,input().strip().split())
h='300000 '*300000
h=list(map(int,h.split()))

count=0
for i in range(d):
    m=max(h)
    if m==0: break
    for j in range(n):
        if h[j]==m:
            h[j]-=1
            count+=1
print(count)
'''

import sys
input = sys.stdin.readline

n,d=map(int,input().strip().split())
h=list(map(int,input().strip().split()))

count=0
m=max(max(h)-d,0)
for i in range(n):
    if h[i]>m:
        count+=h[i]-m
        h[i]=m
print(count)