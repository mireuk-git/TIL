# https://www.acmicpc.net/problem/3000
# 3000
'''
n=int(input())
l=[]
for i in range(n):
    l.append(tuple(map(int,input().split())))

count=0
for p1 in range(n-2):
    for p2 in range(p1+1,n-1):
        for p3 in range(p2+1,n):
            x,y=False,False
            if l[p1][0]==l[p2][0] and l[p3][1] in (l[p1][1],l[p2][1]): count+=1
            elif l[p1][0]==l[p3][0] and l[p2][1] in (l[p1][1],l[p2][1]): count+=1
            elif l[p2][0]==l[p3][0] and l[p1][1] in (l[p2][1],l[p3][1]): count+=1
print(count)
'''

n=int(input())
points=[]
for _ in range(n):
    points.append(tuple(map(int,input().split())))

cnt_x={}
cnt_y={}
for x,y in points:
    try: cnt_x[x]+=1
    except KeyError: cnt_x[x]=1
    try: cnt_y[y]+=1
    except KeyError: cnt_y[y]=1

count=0
for x,y in points:
    count+=(cnt_x[x]-1)*(cnt_y[y]-1)
print(count)