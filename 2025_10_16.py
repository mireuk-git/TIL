# https://www.acmicpc.net/problem/20575
# 20575

from math import ceil,floor
import sys
input=sys.stdin.readline

n=int(input().strip())
count=0
for i in range(n):
    x1,y1,x2,y2=map(float,input().strip().split())
    lo,hi = min(x1,x2),max(x1,x2)
    if ceil(lo)<hi: count+=1
print(2*n/count)