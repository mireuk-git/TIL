# https://www.acmicpc.net/problem/28357
# 28357
'''
import sys
input=sys.stdin.readline

def check(mid):
    candy=0
    for i in a:
        if i>mid:
            candy+=i-mid
    return candy

n,k=map(int,input().split())
a=list(map(int,input().split()))

left=0
right=max(a)
while left<right:
    mid=(left+right)//2
    candy=check(mid)
    if candy>k: left=mid+1
    else: right=mid
print(left)
'''

# https://www.acmicpc.net/problem/14218
# 14218
'''
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
mat=[[-1]*(n+1) for _ in range(n+1)]
for _ in m:
    i,j=map(int,input().split())
    mat[i][j],mat[j][i]=1,1

q=int(input())
for _ in range(q):
    i,j=map(int,input().split())
    mat[i][j],mat[j][i]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            mat
'''

