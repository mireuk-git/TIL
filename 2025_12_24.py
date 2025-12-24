# https://www.acmicpc.net/problem/21771
# 21771

r,c=map(int,input().split())
rg,cg,rp,cp=map(int,input().split())
room=[]
flag=True
count=0
for i in range(r):
    room.append(input())
    if 'P' in room[i]: 
        if 'P'*cp in room[i]: count+=1
if count==rp: flag=False
if flag: print(1)
else: print(0)
