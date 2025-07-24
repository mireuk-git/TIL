# https://www.acmicpc.net/problem/5705
# 5705
'''
d=[0,1,2]
def sequence(n):
    if len(d)>=n+1:
        return d[n]
    d.append(sequence(n-1)+sequence(n-2))
    return d[n]

n=int(input())
while n!=0:
    print(sequence(n))
    n=int(input())
'''
'''
d=[0,1,2]
n=int(input())
while n!=0:
    while len(d)<n+1:
        d.append(d[-2]+d[-1])
    print(d[n])
    n=int(input())
'''
# https://www.acmicpc.net/problem/3474
# 3474

import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    po5=0
    t=5
    while t<=n:
        po5+=n//t
        t*=5
    print(po5)