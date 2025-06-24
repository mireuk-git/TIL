# https://www.acmicpc.net/problem/9215
# 9215

import sys
input=sys.stdin.readline

test_case=0
t=int(input())
while t!=0:
    test_case+=1
    W,N,D=0,0,1
    for i in range(t):
        w,n,d=0,0,1
        feed=input().strip()
        if ',' in feed: 
            w,feed=feed.split(',')
            w=int(w)
        if '/' in feed: 
            n,d=map(int,feed.split('/'))
        else: w=int(feed)
    
        N=N*d+n*D
        D*=d
        W+=w+N//D
        N%=D

        a,b=N,D
        while b!=0:
            a,b=b,a%b
        N//=a
        D//=a

    print(f"Test {test_case}: ",end='')
    if W and N: print(f"{W},{N}/{D}")
    elif W: print(W)
    elif N: print(f"{N}/{D}")
    else: print(0)

    t=int(input())    
    