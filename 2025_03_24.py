# https://www.acmicpc.net/problem/6616
# 6616
'''
import sys
def encode(n,s):
    length=len(s)
    if length<=n:
        return s
    
    r=['']*length
    i=0
    for c in s:
        r[i]=c
        i+=n
        if i>=length:
            i=0
            while i<length and r[i]: i+=1
    return ''.join(r)

n=int(sys.stdin.readline().strip())
while n!=0: 
    s=sys.stdin.readline().strip().upper().replace(" ","")
    print(encode(n,s))
    n=int(sys.stdin.readline().strip())
'''

# https://www.acmicpc.net/problem/33524
# 33524

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=list(map(int,input().split()))
c=[0]*m

for i in range(m):
    p,q=0,len(a)-1
    while p<=q:
        mid=(p+q)//2
        if a[mid]<=b[i]:
            c[i]=mid
            p=mid+1
        else:
            q=mid-1

from math import sqrt
for i in range(m):
    if c[i]==0: print(0,end=' ')
    else: print(int((3+sqrt(9+12*c[i]))//6),end=' ')