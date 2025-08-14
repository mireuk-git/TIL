# https://www.acmicpc.net/problem/27952
# 27952

import sys
input=sys.stdin.readline

n,x=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count,w=0,0
for i in range(n):
    w+=b[i]
    if w<a[i] and count>0:
        tmp=min((a[i]-w+x-1)//x,count)
        count-=tmp
        w+=tmp*x
    if w>=a[i]:
        tmp=(w-a[i])//x
        w-=tmp*x
        count+=tmp
    if w<a[i]:
        count=-1
        break
print(count)

