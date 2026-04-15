# https://www.acmicpc.net/problem/11070

import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(t):
    n,m = map(int,input().strip().split())
    score=[[0,0] for i in range(n+1)]
    for i in range(m):
        a,b,p,q = map(int,input().strip().split())
        score[a][0] += p
        score[a][1] += q
        score[b][0] += q
        score[b][1] += p
    w=[0]*(n+1)
    for i in range(1,n+1):
        try:
            w[i] = (score[i][0]**2)/(score[i][0]**2+score[i][1]**2)
        except ZeroDivisionError:
            w[i]=0
    w=sorted(w[1:],reverse=True)
    print(int(w[0]*1000))
    print(int(w[-1]*1000))