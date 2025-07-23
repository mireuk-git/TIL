# https://www.acmicpc.net/problem/14592
# 14592
'''
n=int(input())
contestants=[]
for i in range(n):
    s,c,l=map(int,input().split())
    contestants.append((s,c,l,i+1))
del s,c,l

contestants=sorted(contestants,key=lambda x: (-x[0],x[1],x[2]))
print(contestants[0][3])
'''
# https://www.acmicpc.net/problem/11536
# 11536
'''
n=int(input())
names=[input() for _ in range(n)]

r="INCREASING"
increase=sorted(names)
for i in range(n):
    if names[i]!=increase[i]:
        r="DECREASING"
        break

if r=='DECREASING':
    decrease=sorted(names,reverse=True)
    for i in range(n):
        if names[i]!=decrease[i]:
            r='NEITHER'
            break

print(r)
'''
# https://www.acmicpc.net/problem/28282
# 28282

from collections import Counter

x,k=map(int,input().split())
a=list(map(int,input().split()))
right=Counter(a[:x])
left=Counter(a[x:])
c=0
for i in right:
    c+=right[i]*(x-left[i])
print(c)