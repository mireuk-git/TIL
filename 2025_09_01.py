# https://www.acmicpc.net/problem/1850
# 1850

'''def Euclidean(a,b):
    a=max(a,b)
    b=min(a,b)
    while b>0:
        a=b
        b=a%b
    return a'''

from math import gcd
a,b=map(int,input().split())
g=gcd(a,b)
for i in range(g//(10**6)):
    print('1'*10**6,end='')
print('1'*(g%(10**6)))

