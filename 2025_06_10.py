# https://www.acmicpc.net/problem/17829
# 17829
'''
import sys
input=sys.stdin.readline

n=int(input().strip())
mat=[list(map(int,input().strip().split())) for _ in range(n)]
while n>1:
    mat2=[['' for _ in range(n//2)] for _ in range(n//2)]
    for i in range(0,n,2):
        for j in range(0,n,2):
            sector=[mat[i][j],mat[i+1][j],mat[i][j+1],mat[i+1][j+1]]
            sector.remove(max(sector))
            mat2[i//2][j//2]=max(sector)
    mat=mat2
    del mat2
    n//=2
print(mat[0][0])
'''
# https://www.acmicpc.net/problem/6600
# 6600

import sys
from math import sqrt
input=sys.stdin.readline

feed=input().strip()
while feed:
    x1,y1,x2,y2,x3,y3=map(float,feed.split())
    a=sqrt((x1-x2)**2+(y1-y2)**2)
    b=sqrt((x2-x3)**2+(y2-y3)**2)
    c=sqrt((x3-x1)**2+(y3-y1)**2)

    s=(a+b+c)/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    r=(a*b*c)/(4*area)

    pi=3.141592653589793

    print(round(2*r*pi,2))

    feed=input().strip()