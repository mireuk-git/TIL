# https://www.acmicpc.net/problem/11663
# 11663
'''n,m=map(int,input().split())
c=list(map(int,input().split())) #점 좌표
c.sort()
for i in range(m):
    l,r=map(int,input().split())

    #선분 위의 가장 좌측 좌표
    p,q=0,n-1
    while p<q:
        mid=(p+q)//2
        if c[mid]<l: p=mid+1
        else: q=mid
    left=p
    if c[left]<=r: left+=1

    #선분 위의 가장 우측 좌표
    p,q=0,n-1
    while p<q:
        mid=(p+q)//2
        if c[mid]<=r: p=mid+1
        else: q=mid
    right=p
    if c[right]<=r: right+=1

    a=right-left
    if a<0: a=0
    print(a)'''

# https://www.acmicpc.net/problem/1406
# 1406

import sys

s=list(input())
cursor=len(s)
m=int(input())
for i in range(m):
    command=input()
    if command=="L":
        if cursor>0: cursor-=1
    elif command=="D":
        if cursor<len(s): cursor+=1
    elif command=="B":
        if cursor>0:
            s.remove(s[cursor-1])
    elif command[0:2]=="P ":
        add=command[2]
        s.insert(cursor,command[2])
        cursor+=1
print(''.join(s))

