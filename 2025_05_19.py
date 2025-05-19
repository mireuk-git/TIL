# https://www.acmicpc.net/problem/23305
# 23305
'''
from collections import Counter
import sys
input=sys.stdin.readline

n=int(input().strip())
a=Counter(map(int,input().strip().split()))
b=Counter(map(int,input().strip().split()))

c=0
for i in b.keys():
    if a[i]<b[i]:
        c+=b[i]-a[i]
print(c)
'''
# greedy

import sys
input=sys.stdin.readline
n=int(input().strip())
a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))

c=n
for i in range(n):
    for j in range(n):
        if b[i]==a[j] and i != j:
            a[i],a[j]==a[j],a[i]
            c-=1
            a[i]=-1
            if a[j]==b[j]:
                c-=1
                a[j]=-1
            break
print(c)
