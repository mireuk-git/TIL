# https://www.acmicpc.net/problem/28432
# 28432

n=int(input())
s=[]
for _ in range(n):
    string=input()
    if string=="?":
        i=_
    s.append(string)
first,end='',''
if i>0: first = s[i-1][-1]
if i<n-1: end = s[i+1][0]

m=int(input())
for i in range(m):
    a=input()
    if first in a[0] and end in a[-1] and a not in s:
        r=a
print(r)
