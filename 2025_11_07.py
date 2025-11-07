# https://www.acmicpc.net/problem/14809
# 14809

import sys
from math import pi
input=sys.stdin.readline

t=int(input().strip())
for test_case in range(1,t+1):
    n,k = map(int,input().strip().split())
    r,top,side=['']*n,[],[]
    for i in range(n):
        r[i],h=map(int,input().strip().split())
        top.append(r[i]**2)
        side.append(r[i]*2*h)
    pans = sorted(zip(r,top,side),key=lambda x: (-x[2]))
    r,top,side = zip(*pans)

    m=0
    for i in range(n):
        s=top[i]+side[i]
        cnt=1
        for j in range(n):
            if cnt==k: break
            if j!=i and r[j]<=r[i]:
                s+=side[j]
                cnt+=1
        if s>m: m=s
    print(f"Case #{test_case}:", m*pi)
