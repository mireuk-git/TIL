# https://www.acmicpc.net/problem/32500
'''
n=int(input())
l=[0 for i in range(51)]
for _ in range(10*n):
    i=list(map(int,input().split()))
    for j in i: l[j]+=1
flag=True
for i in range(1,51):
    if l[i]>2*n:
        print(i, end=' ')
        flag=False
if flag: print(-1)
'''
'''
import sys
from collections import Counter

input=sys.stdin.readline

n=int(input())
cnt=Counter()

for _ in range(10*n):
    cnt.update(map(int,input().split()))
res=[str(num) for num,c in sorted(cnt.items()) if c>2*n]
print(' '.join(res) if res else -1)
'''

# https://www.acmicpc.net/problem/12572

t=int(input())
for _ in t:
    n=int(input())
    wires=[]
    for i in range(n):
        wires.append(list(map(int,input().split())))
    c=0
    for w1 in range(n-1):
        for w2 in range(w1+1,n):
            if (wires[w1][0]<wires[w2][0] and wires[w1][1]>wires[w2][1]) or (wires[w1][0]>wires[w2][0] and wires[w1][1]<wires[w2][1]):
                c+=1



