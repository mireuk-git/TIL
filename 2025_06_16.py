# https://www.acmicpc.net/problem/13702
# 13702

import sys
input=sys.stdin.readline

n,k=map(int,input().strip().split())
l=[int(input()) for _ in range(n)]
start,end=1,max(l)

while start<=end:
    mid=(start+end)//2
    c=0
    for i in range(n):
        c+=l[i]//mid
    if c<k:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)