# https://www.acmicpc.net/problem/13567
# 13567

m,n=map(int,input().split())
x,y=0,0
dx,dy=1,0
valid=True
for i in range(n):
    command,d=input().split()
    d=int(d)
    if valid:
        if command == 'TURN':
            if d==0:
                if dx==1: dx,dy=0,1
                elif dy==1: dx,dy=-1,0
                elif dx==-1: dx,dy=0,-1
                elif dy==-1: dx,dy=1,0
            elif d==1:
                if dx==1:dx,dy=0,-1
                elif dy==-1: dx,dy=-1,0
                elif dx==-1: dx,dy=0,1
                elif dy==1: dx,dy=1,0
        elif command == 'MOVE':
            if 0<=x+d*dx<=m and 0<=y+d*dy<=m:
                x+=d*dx
                y+=d*dy
            else: valid=False
if not valid: print(-1)
else: print(x,y)

