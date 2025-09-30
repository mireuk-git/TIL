# https://www.acmicpc.net/problem/30155
# 30155

import sys
input=sys.stdin.readline
t=int(input().strip())
for _ in range(t):
    a,b,n=map(int,input().strip().split())
    l=[a,b,b-a,-a,-b,a-b]
    print(l[(n-1)%6]%1000000007)
