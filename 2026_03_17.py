# https://www.acmicpc.net/problem/22993

n=int(input())
a=list(map(int,input().split()))
a1=a[0]
a=sorted(a[1:])
for i in a:
    if a1>i: a1+=i
    else: break
if a1 >= sum(a): print("Yes")
else: print("No")