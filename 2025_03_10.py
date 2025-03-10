# https://www.acmicpc.net/problem/2097
# 2097
'''
from math import sqrt

n=int(input())
w=int(sqrt(n))
h=w
if h*w<n: h+=1
if h*w<n: w+=1
if w>1: w-=1
if h>1: h-=1
print("h:",h)
print("w:",w)
print((w+h)*2)
'''

# https://www.acmicpc.net/problem/11649
# 11649
'''
n=int(input())
l=[]
for i in range(n):
    l.append(input()[::-1])
l.sort()
for i in range(n):
    print(l[i])'
'''

# https://www.acmicpc.net/problem/11663
# 11663
n,m=map(int,input().split())
c=list(map(int,input().split())) #점 좌표
c.sort()
for i in range(m):
    l=list(map(int,input().split()))

    left=int((n-1)/2) #선분 위의 가장 좌측 좌표
    p,q=0,n-1
    while True:
        if c[left]<l[0]:
            if left>=m-1:
                left=m-1
                break
            elif c[left+1]>l[0]: 
                left+=1
                break
            p=left+1
        elif c[left]>l[0]:
            if left<=0:
                left=0
                break
            elif c[left-1]<l[0]: break
            q=left-1
        else: break
        left=int((p+q)/2)

    right=int((n-1)/2) #선분 위의 가장 우측 좌표
    p,q=0,n-1
    while True:
        if c[right]<l[1]:
            if right>=m-1:
                right=m-1
                break
            if c[right+1]>l[1]: break
            p=right+1
        elif c[right]>l[1]:
            if right<=0:
                right=0
                break
            if c[right-1]<l[1]:
                right-=1
                break
            q=right-1
        else: break            
        right=int((p+q)/2)

    a=right-left+1
    if a<0: a=0
    print(a)