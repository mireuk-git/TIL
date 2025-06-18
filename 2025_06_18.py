# https://www.acmicpc.net/problem/15701
# 15701
'''
n=int(input())
i=1
c=0
while i**2<=n:
    if n%i==0:
        c+=2
        if i**2==n: c-=1
    i+=1
print(c)
'''
# https://www.acmicpc.net/problem/32365

import sys
from collections import Counter
input=sys.stdin.readline

t,n=map(int,input().strip().split())
for _ in range(t):
    s=input()
    heavy=[0]*n
    c=Counter(s)
    for i in range(n):
        if c[s[i]]>1:
            heavy[i]=1
    
    for i in range(n-1):
        alter=True
        if (heavy[i]+heavy[i+1])%2==0:
            alter=False
            break
    if alter: print("T")
    else: print("F")
