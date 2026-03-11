# https://www.acmicpc.net/problem/25576

import sys
input=sys.stdin.readline

n,m=map(int,input().strip().split())
l=list(map(int,input().strip().split()))
count=0
buntang=False
for i in range(n-1):
    k=list(map(int,input().strip().split()))
    diffsum=0
    for j in range(len(l)):
        diffsum+=abs(l[j]-k[j])
    if diffsum>2000: count+=1
    if count>=n/2: buntang=True
if buntang: print("YES")
else: print("NO")
