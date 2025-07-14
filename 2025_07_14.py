# https://www.acmicpc.net/problem/28138
# 28138
'''
from math import sqrt

n,r=map(int,input().split())
m,s=1,0
t=n-r
while m<=int(sqrt(t)):
    if t%m==0:
        x=t//m
        if m>r: s+=m
        if x>r and x!=m: s+=x
    m+=1
del t,x
print(s)
'''
# https://www.acmicpc.net/problem/28357
# 28357

import sys
input=sys.stdin.readline

n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

for i in range(n):
    x=a[i]-1
    candy=0
    j=i
    while j<n and candy+a[j]-x <= k:
        candy+=a[j]-x
        j+=1
    if j==n and candy<=k: break
x-=(k-candy)//(n-i)
print(x)