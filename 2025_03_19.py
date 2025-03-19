# https://www.acmicpc.net/problem/21895
# 21895
'''
n=int(input())
A=input()
B=input()
StoI={"S":0, "R":1, "P":2}
ItoS={0:"S", 1:"R", 2:"P"}

for i in range(n):
    a,b=StoI[A[i]],StoI[B[i]]
    if a==b:
        print((ItoS[(a+1)%3]),end='')
    else: 
        r=max(a,b)
        if max(a,b)==2 and min(a,b)==0: r=0
        print((ItoS[r]),end='')
'''
# https://www.acmicpc.net/problem/12645
# 12645
from itertools import permutations

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,str(n)))
    l.insert(0,0)
    l.sort()
    perm=list(permutations(l))
    r=perm[0]
    for i in perm:
        i=int(''.join(map(str,i)))
        if i > n: 
            r=i
            break

    print(f"Case #{_+1}:",r)