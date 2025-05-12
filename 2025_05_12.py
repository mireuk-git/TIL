# https://www.acmicpc.net/problem/1004
# 1004

import sys
from math import sqrt 
input=sys.stdin.readline

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

t=int(input().strip())
for _ in range(t):
    x1,y1,x2,y2=map(int,input().strip().split())
    n=int(input())
    c=0
    for i in range(n):
        cx,cy,r=map(int,input().strip().split())
        flag1,flag2=distance(x1,y1,cx,cy)<r,distance(x2,y2,cx,cy)<r
        if flag1 ^ flag2: c+=1
    print(c)
