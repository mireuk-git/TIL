# https://www.acmicpc.net/problem/16508
# 16508
'''
from collections import Counter

price=float("inf")
def dfs(x,p,a):
    result=True
    for i in t.keys():
        if x[i]>t[i]:
            result=False
            break
    if result:
        price=min(price,p)
        return
    for i in range(a,n):
        
        dfs(x,p,a+1)

t=Counter(input())
n=int(input())
W=[]
for _ in range(n):
    c,w=input.split()
    c=int(c)
    W.append(Counter(w))

x={chr(i):0 for i in range(ord('A'),ord('Z')+1)}
'''

from collections import Counter

t=Counter(input())
n=int(input())
C,W=[],[]
for _ in range(n):
    c,w=input().split()
    C.append(int(c))
    W.append(Counter(w))
x={i:0 for i in t.keys()}

def dfs(x,p,a):
    global p_min
    result=True
    for i in t.keys():
        if t[i]>x[i]:
            result=False
            break
    if result:
        p_min=min(p,p_min)
        return
    for i in range(a,n):
        new_x={j:x[j]+W[i][j] for j in t.keys()}
        dfs(new_x,p+C[i],i+1)

p_min=float("inf")
dfs(x,0,0)
if p_min==float("inf"):print(-1)
else: print(p_min)