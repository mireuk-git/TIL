# https://www.acmicpc.net/problem/14534
# 14534
'''
from itertools import permutations
t=int(input())
for test_case in range(1,t+1):
    l=input()
    p=set(permutations(l))
    print(f"Case # {test_case}:")
    for i in p:
        r=''
        for j in i:
            r+=j
        print(r)
'''
# https://www.acmicpc.net/problem/13360
# 13360
'''
match=input()
rank=25
star=0
required_star=[-1,5,5,4,3,2]
streak=0
for i in match:
    if i=='W':
        streak+=1
        if rank>=6 and streak>2: star+=2
        else: star+=1
        
        if star>required_star[(rank+4)//5]:
            star-=required_star[(rank+4)//5]
            rank-=1
            if rank==0: 
                rank='Legend'
                break
    
    else: 
        streak=0
        if rank<20: 
            star-=1
            if star<0: 
                rank+=1
                star=required_star[(rank+4)//5]-1
        elif rank==20 and star>0: star-=1
print(rank)
'''
# https://www.acmicpc.net/problem/28256
# 28256

def visit(x,y):
    if x<0 or x>2 or y<0 or y>2 or visited[x][y]: return 0
    visited[x][y]=True
    if chocolate[x][y]=='O':
        return 1+visit(x+1,y)+visit(x-1,y)+visit(x,y+1)+visit(x,y-1)
    else: return 0

t=int(input())
for test_case in range(1,t+1):
    chocolate=[list(input()) for _ in range(3)]
    a=list(map(int,input().split()))
    n=a[0]
    visited=[[False,False,False],[False,True,False],[False,False,False]]
    r=[0]
    for i in range(3):
        for j in range(3):
            tmp=visit(i,j)
            if tmp>0:
                r.append(tmp)
    r.sort()

    flag=1
    if len(r)-1==n:
        for i in range(1,n+1):
            if a[i]!=r[i]:
                flag=0
                break
    else: flag=0
    print(flag)