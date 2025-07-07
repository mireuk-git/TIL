# https://www.acmicpc.net/problem/9780
# 9780

import sys
input=sys.stdin.readline

t=int(input().strip())
for testcase in range(t):
    input()
    n,q=map(int,input().strip().split())
    N=list(map(int,input().strip().split()))

    s=[0]*(n+1)
    for i in range(1,n+1):
        s[i]=s[i-1]+N[i-1]

    for _ in range(q):
        i,j=map(int,input().strip().split())
        print(s[j+1]-s[i])
    if testcase<t-1: print()