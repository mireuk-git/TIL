# https://www.acmicpc.net/problem/6796
# 6796

import sys
input=sys.stdin.readline

line=input().strip()
vars={'A':0,'B':0}
while line!='7':
    op,line=line.split(' ',1)
    if op=='1':
        v,n=line.split()
        vars[v]=int(n)
    elif op=='2':
        print(vars[line])
    elif op=='3':
        a,b=line.split()
        vars[a]+=vars[b]
    elif op=='4':
        a,b=line.split()
        vars[a]*=vars[b]
    elif op=='5':
        a,b=line.split()
        vars[a]-=vars[b]
    elif op=='6':
        a,b=line.split()
        vars[a]//=vars[b]
        if vars[a]<0: vars[a]+=1
    line=input().strip()