# https://www.acmicpc.net/problem/3724

import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    m,n = map(int,input().strip().split())
    mat=[]
    for i in range(n):
        mat.append(list(map(int,input().strip().split())))
    mult=[1]*m
    for i in range(m):
        for j in range(n):
            mult[i]*=mat[j][i]
    mult,order = zip(*sorted(zip(mult,[i for i in range(1,m+1)]),key=lambda x: (-x[0],-x[1])))
    print(order[0])
    