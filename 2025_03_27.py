# https://www.acmicpc.net/problem/2164
# 2164
'''
from collections import deque

n=int(input())
d=deque(i for i in range(1,n+1))
while len(d)>1:
    d.popleft()
    d.append(d.popleft())
print(d[0])
'''
'''
n=int(input())
if n==1 or n==2: print(n)
else:
    k=0
    while 2**k<n: k+=1
    print((n-2**(k-1))*2)'
'''
# https://www.acmicpc.net/problem/24465
# 24465
import datetime
bound=[datetime.datetime(2024,2,18),
   datetime.datetime(2024,3,20),
   datetime.datetime(2024,4,19),
   datetime.datetime(2024,5,20),
   datetime.datetime(2024,6,21),
   datetime.datetime(2024,7,22),
   datetime.datetime(2024,8,22),
   datetime.datetime(2024,9,22),
   datetime.datetime(2024,10,22),
   datetime.datetime(2024,11,22),
   datetime.datetime(2024,12,21)
]
EARLY_BOUND=datetime.datetime(2024,1,19)
LATE_BOUND=datetime.datetime(2024,12,22)
constel=[False]*12

for _ in range(7):
    m,d=map(int,input().split())
    dt=datetime.datetime(2024,m,d)
    if dt<=EARLY_BOUND or dt>=LATE_BOUND: 
        constel[11]=True
    else:
        for i in range(11):
            if dt<=bound[i]:
                constel[i]=True
                break

n=int(input())
r=[]
for _ in range(n):
    m,d=map(int,input().split())
    dt=datetime.datetime(2024,m,d)
    if dt<=EARLY_BOUND or dt>=LATE_BOUND: 
        if not constel[11]: 
            r.append(dt)
        continue
    for i in range(11):
        if dt<=bound[i]:
            if not constel[i]:
                r.append(dt)
            break

if r:
    r.sort()
    for i in r:
        print(i.month, i.day)
else: print("ALL FAILED")