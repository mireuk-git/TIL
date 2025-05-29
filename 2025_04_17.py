# https://www.acmicpc.net/problem/16960
# 16960
'''
n,m=map(int,input().split())
switches=[]
for _ in range(n):
    switches.append(list(map(int,input().split()))[1:])

answer=0
for i in range(n):
    lamps=set()
    for j in range(n):
        if i==j:
            continue
        lamps.update(switches[j])
    if len(lamps)==m:
        answer=1
        break
print(answer)
'''
# https://www.acmicpc.net/problem/1491
# 1491
'''
n,m=map(int,input().split())
total=n*m
x,y=0,0

dir=[(1,0),(0,1),(-1,0),(0,-1)]
bound=[n-1,m-1,0,0]
d=0
step=0
while step<total:
    dx,dy=dir[d]
    x+=dx*abs((bound[d]-x))
    y+=dy*abs((bound[d]-y))
    bound[d]+(-1)**(d//2+1)
    step+=max(dx*(bound[d]-x), dy*(bound[d]-y))
    d=(d+1)%4
print(x,y)
'''
n,m=map(int,input().split())
total=n*m
x,y=0,0
dx=[1,0,-1,0]
dy=[0,1,0,-1]

top,bottom,left,right=n-1,0,0,m-1
dir=0
steps=0

while steps<total-1:
    if dir==0:
        move=right-x
        move=min(move,total-steps-1)
        x+=move
        top-=1
    elif dir==1:
        move=top-y
        move=min(move,total-steps-1)
        y+=move
        right-=1
    elif dir==2:
        move=x-left
        move=min(move,total-steps-1)
        x-=move
        bottom+=1
    elif dir==3:
        move=y-bottom
        move=min(move,total-steps-1)
        y-=move
        left+=1
    steps+=move
    dir=(dir+1)%4
print(x,y)


