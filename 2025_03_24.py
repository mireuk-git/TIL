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
from math import sqrt
from bisect import bisect_right

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=list(map(int,input().split()))

for i in range(m):
    c=bisect_right(a,b[i])-1
    if c==-1: print(0,end=' ')
    else: print(int((3+sqrt(9+12*c))//6),end=' ')

