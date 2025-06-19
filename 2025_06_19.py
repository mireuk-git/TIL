# https://www.acmicpc.net/problem/20551
# 20551

import sys
input=sys.stdin.readline

n,m=map(int,input().strip().split())
a=[int(input().strip()) for _ in range(n)]
a.sort()

index={}
for i in range(n):
    d=a[i]
    try:
        index[d]
    except KeyError:
        index[d]=i

for i in range(m):
    d=int(input().strip())
    try: 
        ans=index[d]
    except KeyError:
        ans=-1
    print(ans)